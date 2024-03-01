import os

import pinecone
from dotenv import load_dotenv

# Load the stored environment variables
load_dotenv()

PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")


pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_ENVIRONMENT,
)

index_description = pinecone.describe_index(PINECONE_INDEX)
print(index_description)
