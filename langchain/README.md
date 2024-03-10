# LangChain Experiments

This repository focuses on experimenting with the LangChain library for building powerful applications with large language models (LLMs). By leveraging state-of-the-art language models like OpenAI's GPT-3.5 Turbo (and soon GPT-4), this project showcases how to create a searchable database from a YouTube video transcript, perform similarity search queries using the FAISS library, and respond to user questions with relevant and precise information.

LangChain is a comprehensive framework designed for developing applications powered by language models. It goes beyond merely calling an LLM via an API, as the most advanced and differentiated applications are also data-aware and agentic, enabling language models to connect with other data sources and interact with their environment. The LangChain framework is specifically built to address these principles.

## Use Cases

With LangChain, developers can create various applications, such as customer support chatbots, automated content generators, data analysis tools, and intelligent search engines. These applications can help businesses streamline their workflows, reduce manual labor, and improve customer experiences.

## Requirements

- [Python 3.6 or higher](https://www.python.org/downloads/)
- [LangChain library](https://python.langchain.com/en/latest/index.html)
- [OpenAI API key](https://platform.openai.com/)
- [SerpAPI API Key](https://serpapi.com/)

## OpenAI API Models

The OpenAI API is powered by a diverse set of [models](https://platform.openai.com/docs/models) with different capabilities and price points. You can also make limited customizations to our original base models for your specific use case with fine-tuning.

## Installation

### Create a Python environment

Python 3.6 or higher using `venv` or `conda`

```bash
conda create -n langchain-001 python=3.9
conda activate langchain-001
```

#### Install the required dependencies

``` bash
pip install -r requirements.txt
```

#### Set up the keys in a .env file

First, create a `.env` file in the root directory of the project. Inside the file, add your OpenAI API key:

```makefile
OPENAI_API_KEY="your_api_key_here"
```
