import os
import openai
import PyPDF2
from newspaper import Article
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_pdf_text(file_path):
    try:
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = "".join([page.extract_text() for page in reader.pages])
        return text
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

def extract_article_text(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        return f"Error reading URL: {str(e)}"

def summarize_content(input_str):
    if input_str.strartswith("http"):
        content = extract_article_text(input_str)
    else:
        content = extract_pdf_text(input_str)

    if not content:
        return "No content found to summarize"

    prompt = f"Summerize this for me:\n\n{content[:2000]}"

    try:
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [{"role":"user","content": prompt}],
            max_token = 300
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error during summarization: {str(e)}"
