"""
Configuration loader for the chatbot.
Reads environment variables and returns config dict.
"""
import os
from dotenv import load_dotenv

load_dotenv()

def get_config():
    return {
        'NLP_PROVIDER': os.getenv('NLP_PROVIDER', 'dialogflow'),
        'DIALOGFLOW_API_KEY': os.getenv('DIALOGFLOW_API_KEY'),
        'RASA_ENDPOINT': os.getenv('RASA_ENDPOINT'),
        'MICROSOFT_APP_ID': os.getenv('MICROSOFT_APP_ID'),
        'MICROSOFT_APP_PASSWORD': os.getenv('MICROSOFT_APP_PASSWORD'),
    }
