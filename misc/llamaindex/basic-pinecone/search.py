import logging
import os
import sys
from pathlib import Path

import openai
import pinecone
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
from llama_index.vector_stores import Pinecone

# Load the stored environment variables
load_dotenv()

PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

# initialize pinecone
pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_ENVIRONMENT,  # find at app.pinecone.io
)
index_name = "test001"


docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)


llm = OpenAI(temperature=0, openai_api_key=os.environ["OPENAI_API_KEY"])
chain = load_qa_chain(llm, chain_type="stuff")

query = "What are the room categories of the hotel?"
docs = docsearch.similarity_search(query, include_metadata=True)

chain.run(input_documents=docs, question=query)
