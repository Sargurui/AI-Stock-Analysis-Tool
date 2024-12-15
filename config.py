import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in the .env file.")
