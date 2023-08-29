import logging
import os
import sys
from pathlib import Path

import openai
import requests
from dotenv import load_dotenv
from llama_index import (
    LLMPredictor,
    ServiceContext,
    SimpleDirectoryReader,
    SimpleKeywordTableIndex,
    VectorStoreIndex,
)
from llama_index.indices.composability.graph import ComposableGraph
from llama_index.llms import OpenAI
from llama_index.storage.storage_context import StorageContext
from llama_index.vector_stores import PineconeVectorStore


def setup_logging():
    """Set up logging."""
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


def download_wikipedia_articles(titles):
    """
    Download Wikipedia articles corresponding to the provided titles.

    Args:
        titles (List[str]): List of Wikipedia titles for articles to download.
    """
    data_path = Path("data")
    if not data_path.exists():
        Path.mkdir(data_path)
    for title in titles:
        url = "https://en.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "format": "json",
            "titles": title,
            "prop": "extracts",
            "explaintext": True,
        }
        response = requests.get(url, params=params).json()
        page = next(iter(response["query"]["pages"].values()))
        wiki_text = page["extract"]
        with open(data_path / f"{title}.txt", "w") as fp:
            fp.write(wiki_text)


def load_city_docs(titles):
    """
    Load city documents from disk.

    Args:
        titles (List[str]): List of titles for articles to load.

    Returns:
        dict: A dictionary of city documents.
    """
    city_docs = {}
    for wiki_title in titles:
        city_docs[wiki_title] = SimpleDirectoryReader(
            input_files=[f"data/{wiki_title}.txt"]
        ).load_data()
    return city_docs


def build_city_indices(
    city_docs, pinecone_titles, wiki_titles, index_name, environment
):
    """
    Build city indices.

    Args:
        city_docs (dict): Dictionary of city documents.
        pinecone_titles (List[str]): List of Pinecone titles.
        wiki_titles (List[str]): List of Wikipedia titles.
        index_name (str): Pinecone index name.
        environment (str): Pinecone environment.

    Returns:
        dict: Dictionary of city indices.
    """
    city_indices = {}
    llm = OpenAI(temperature=0, model="gpt-3.5-turbo")
    service_context = ServiceContext.from_defaults(llm=llm)
    for pinecone_title, wiki_title in zip(pinecone_titles, wiki_titles):
        metadata_filters = {"wiki_title": wiki_title}
        vector_store = PineconeVectorStore(
            index_name=index_name,
            environment=environment,
            metadata_filters=metadata_filters,
        )
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        city_indices[wiki_title] = VectorStoreIndex.from_documents(
            city_docs[wiki_title],
            storage_context=storage_context,
            service_context=service_context,
        )
        city_indices[wiki_title].index_struct.index_id = pinecone_title
    return city_indices


def create_composable_graph(city_indices, wiki_titles):
    """
    Create a composable graph.

    Args:
        city_indices (dict): Dictionary of city indices.
        wiki_titles (List[str]): List of Wikipedia titles.

    Returns:
        ComposableGraph: A composable graph.
    """
    index_summaries = {
        wiki_title: f"Wikipedia articles about {wiki_title}"
        for wiki_title in wiki_titles
    }
    graph = ComposableGraph.from_indices(
        SimpleKeywordTableIndex,
        [index for _, index in city_indices.items()],
        [summary for _, summary in index_summaries.items()],
        max_keywords_per_chunk=50,
    )
    return graph


def main():
    """Main function."""
    setup_logging()
    load_dotenv()
    openai.api_key = os.environ["OPENAI_API_KEY"]

    wiki_titles = [
        "Toronto",
        "Seattle",
        "Chicago",
        "Boston",
    ]
    pinecone_titles = [
        "toronto",
        "seattle",
        "chicago",
        "boston",
    ]

    download_wikipedia_articles(wiki_titles)

    city_docs = load_city_docs(wiki_titles)

    environment = os.getenv("PINECONE_ENVIRONMENT")
    index_name = os.getenv("PINECONE_INDEX")
    os.environ["PINECONE_API_KEY"] = os.getenv("PINECONE_API_KEY")

    city_indices = build_city_indices(
        city_docs, pinecone_titles, wiki_titles, index_name, environment
    )

    response = (
        city_indices["Boston"]
        .as_query_engine(
            service_context=ServiceContext.from_defaults(
                llm=OpenAI(temperature=0, model="gpt-3.5-turbo")
            )
        )
        .query("Tell me about the arts and culture of Chicago")
    )
    print(str(response))
    print(response.get_formatted_sources())


if __name__ == "__main__":
    main()
