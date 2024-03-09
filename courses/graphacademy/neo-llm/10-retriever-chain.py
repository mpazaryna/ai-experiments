import os

import dotenv
from langchain_community.vectorstores.neo4j_vector import Neo4jVector
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from langchain.chains import RetrievalQA

dotenv_path = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_path)

chat_llm = ChatOpenAI()
embedding_provider = OpenAIEmbeddings()

movie_plot_vector = Neo4jVector.from_existing_index(
    embedding_provider,
    url="bolt://localhost:7687",
    username="neo4j",
    password="",
    index_name="moviePlots",
    embedding_node_property="embedding",
    text_node_property="plot",
)

plot_retriever = RetrievalQA.from_llm(
    llm=chat_llm, retriever=movie_plot_vector.as_retriever()
)

result = plot_retriever.invoke({"query": "A movie where a hotel caretaker goes crazy."})

print(result)
