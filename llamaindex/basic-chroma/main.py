# Import necessary modules and classes:
# - TextLoader: Used to load text documents.
# - SentenceTransformerEmbeddings: Provides embeddings using sentence transformers.
# - CharacterTextSplitter: Splits text into smaller chunks based on characters.
# - Chroma: A vector store to save and query document embeddings.

from langchain.document_loaders import TextLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

# Load the document:
# 1. Create an instance of TextLoader with the path to the "state_of_the_union.txt" file.
# 2. Use the `load` method of the loader to read the content of the document into memory.
loader = TextLoader("./data/state_of_the_union.txt")
documents = loader.load()

# Split the loaded document into smaller chunks:
# 1. Create an instance of CharacterTextSplitter with a specified chunk size and overlap.
#    - chunk_size=1000: Each chunk will have 1000 characters.
#    - chunk_overlap=0: Chunks won't overlap with each other.
# 2. Use the `split_documents` method to split the loaded document into smaller chunks.
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# Create embeddings for the document chunks:
# 1. Create an instance of SentenceTransformerEmbeddings with a specified model name.
#    This will use the "all-MiniLM-L6-v2" model to generate embeddings for sentences.
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# Load the document chunks and their embeddings into Chroma:
# 1. Use the `from_documents` method of Chroma to load the chunks and their embeddings.
#    This creates a searchable database of the document chunks.
db = Chroma.from_documents(docs, embedding_function)

# Query the Chroma database:
# 1. Define a query string to search for relevant document chunks.
# 2. Use the `similarity_search` method of the Chroma instance to find the most similar chunks to the query.
query = "What did the president say about Ketanji Brown Jackson"
docs = db.similarity_search(query)

# Display the result:
# Print the content of the most relevant document chunk found in the search.
print(docs[0].page_content)
