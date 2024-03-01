# Llama Index Experiments

This repository focuses on experimenting with the Llama Index library for building powerful applications with large language models (LLMs).  

[Installation](https://gpt-index.readthedocs.io/en/latest/getting_started/installation.html)

LlamaIndex is a data framework that helps developers build applications with large language models (LLMs). It provides tools for ingesting, structuring, retrieving, and integrating data with various application frameworks. LlamaIndex acts as an interface between external data and LLMs, allowing developers to augment LLMs with private data.

LlamaIndex offers data connectors to ingest data from existing sources and formats, such as APIs, PDFs, documents, SQL, Notion, Slack, Postgres, and MongoDB. It also provides ways to structure data, such as through indices and graphs, so that it can be easily used with LLMs.

LlamaIndex was formerly known as the GPT Index.

## LangChain

The Python-specific portion of LangChain's documentation covers several main modules, each providing examples, how-to guides, reference docs, and conceptual guides. These modules include:

1. Models: Various model types and model integrations supported by LangChain.
3. Prompts: Prompt management, optimization, and serialization.
3. Memory: State persistence between chain or agent calls, including a standard memory interface, memory implementations, and examples of chains and agents utilizing memory.
4. Indexes: Combining LLMs with custom text data to enhance their capabilities.
5. Chains: Sequences of calls, either to an LLM or a different utility, with a standard interface, integrations, and end-to-end chain examples.
6. Agents: LLMs that make decisions about actions, observe the results, and repeat the process until completion, with a standard interface, agent selection, and end-to-end agent examples.

## Use Cases

## Requirements

- [Python 3.6 or higher](https://www.python.org/downloads/)
- [LangChain library](https://python.langchain.com/en/latest/index.html)
- [OpenAI API key](https://platform.openai.com/)

## Installation

### 1. Clone the repository  

```bash
git clone https://github.com/mpazaryna/llamaindex-experiments.git
```

### 2. Create a Python environment

Python 3.6 or higher using `venv` or `conda`. Using `venv`:

``` bash
cd llamaindex-experiments
python3 -m venv env
source env/bin/activate
```

### 3. Install the required dependencies

``` bash
pip install -r requirements.txt
```

### 4. Set up the keys in a .env file

First, create a `.env` file in the root directory of the project. Inside the file, add your OpenAI API key:

```makefile
OPENAI_API_KEY="your_api_key_here"
```

Save the file and close it. In your Python script or Jupyter notebook, load the `.env` file using the following code:

```python
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
```

By using the right naming convention for the environment variable, you don't have to manually store the key in a separate variable and pass it to the function. The library or package that requires the API key will automatically recognize the `OPENAI_API_KEY` environment variable and use its value.

When needed, you can access the `OPENAI_API_KEY` as an environment variable:

```python
import os
api_key = os.environ['OPENAI_API_KEY']
```

Now your Python environment is set up, and you can proceed with running the experiments.

## Refactor and Comment Code Prompt

I want you to act as my coding parter. You will be responsible for adding comments to each line of any code that
I provide.  All code should be wrapped in a try block when possible. You should also review the code and return 
the best Python code that you're capable of writing.
