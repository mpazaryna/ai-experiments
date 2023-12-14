"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import os

import google.generativeai as genai
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
API_KEY = os.environ.get("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)


# Set up the model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]

model = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config=generation_config,
    safety_settings=safety_settings,
)

prompt_parts = [
    "What can you tell me about establishing a yoga practice?",
]

response = model.generate_content(prompt_parts)
print(response.text)
