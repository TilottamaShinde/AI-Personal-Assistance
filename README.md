 #  AI-Powered Personal Assistant (Python Project)

An intelligent, voice-based personal assistant built with Python. It understands your voice commands, summarizes PDFs or news articles using OpenAI GPT, schedules tasks using Google Calendar API, and responds to you with spoken output. All powered by modern AI tools and APIs.

---

##  Features

-  Voice command recognition  
-  Summarize PDFs or news articles using OpenAI GPT  
-  Schedule events using Google Calendar API  
-  Speak responses with Text-to-Speech  

---

##  Tech Stack

Python, OpenAI API, Google Calendar API, SpeechRecognition, PyPDF2, pyttsx3, newspaper3k, dotenv

---

##  How to Run the Project

1. Clone this repository and navigate to the folder:
   ```bash
   git clone https://github.com/yourusername/ai-personal-assistant.git
   cd ai-personal-assistant```

2.Create a virtual environment and activate it:

   ```
python -m venv .venv
source .venv/bin/activate        # For Linux/macOS
.venv\Scripts\activate           # For Windows
```

3. Install all required dependencies:
```
pip install -r requirements.txt
```
4. Add your environment variables:

Create a .env file in the project root:
```
OPENAI_API_KEY=your_openai_api_key
```
5. Run the personal assistant:
   ```
   python personal_assistant.py

   ```
