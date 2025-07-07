import os
import openai
import PyPDF2
from newspaper import Article
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
