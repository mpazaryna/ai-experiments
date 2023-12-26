import os

os.environ[
    "ACTIVELOOP_TOKEN"
] = "eyJhbGciOiJIUzUxMiIsImlhdCI6MTcwMzYwNTQ5NiwiZXhwIjoxNzM1MjI3ODc4fQ.eyJpZCI6Im1wYXphcnluYSJ9.rngFQEYsq54ApWTfi9JGw5dBFHzTdJdMZ3EnUMy2e9JWc4AOyHY2RQ38jggOlZEL6ljZeIhMaBLZl1OLp6Jmng"

from langchain.chains import RetrievalQA
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import DeepLake

llm = OpenAI(model="text-davinci-003", temperature=0)
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

# create documents
texts = [
    "Napoleon Bonaparte was born on 15 August 1769 in Corsica into a gentry family.",
    "Louis XIV, known as Louis the Great or the Sun King, was King of France from 14 May 1643 until his death in 1715.",
]

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.create_documents(texts)

# create deep lake dataset
my_activeloop_org_id = "mpazaryna"
my_activeloop_dataset_name = "langchain_course_from_zero_to_hero"
dataset_path = f"hub://{my_activeloop_org_id}/{my_activeloop_dataset_name}"

db = DeepLake.from_documents(docs, embeddings, dataset_path=dataset_path)
