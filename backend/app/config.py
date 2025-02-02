import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration settings for the application."""
    
    # OpenAI API Key
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    # Application Settings
    APP_NAME = "Makers Tech Chatbot"
    DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"

config = Config()
