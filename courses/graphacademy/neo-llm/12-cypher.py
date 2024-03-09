import os

import dotenv
from langchain_community.graphs import Neo4jGraph
from langchain_openai import ChatOpenAI

from langchain.chains import GraphCypherQAChain
from langchain.prompts import PromptTemplate

dotenv_path = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_path)

llm = ChatOpenAI()

graph = Neo4jGraph(
    url="bolt://localhost:7687",
    username="neo4j",
    password="",
)

CYPHER_GENERATION_TEMPLATE = """
You are an expert Neo4j Developer translating user questions into Cypher to answer questions about movies and provide recommendations.
Convert the user's question based on the schema.

Schema: {schema}
Question: {question}
"""

cypher_generation_prompt = PromptTemplate(
    template=CYPHER_GENERATION_TEMPLATE,
    input_variables=["schema", "question"],
)

cypher_chain = GraphCypherQAChain.from_llm(
    llm, graph=graph, cypher_prompt=cypher_generation_prompt, verbose=True
)

# cypher_chain.invoke({"query": "What role did Tom Hanks play in Toy Story?"})
cypher_chain.invoke({"query": "What movies has Tom Hanks acted in?"})
