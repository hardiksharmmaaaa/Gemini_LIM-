from dotenv import load_dotenv
import os

load_dotenv()

# Test if the key is loaded
api_key = os.getenv("GOOGLE_API_KEY")
print(f"API Key: {api_key}")  # This should print your actual API key, not 'None'S