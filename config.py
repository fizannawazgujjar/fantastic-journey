import os
from dotenv import load_dotenv

# Load environment variables from a .env file when present. This keeps API keys out of source code.
load_dotenv()

# API keys (keep empty strings as safe defaults — never hardcode real keys)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
SEARCH_API_KEY = os.getenv("SEARCH_API_KEY", "")

# Assistant configuration
# Wake word (lowercase) — used to trigger the assistant from voice input
WAKE_WORD = "jarvis"
ASSISTANT_NAME = "Jarvis"
USER_NAME = "Fizan"
VOICE_NAME = "en-US-GuyNeural"

# Microphone device index. Users can run mic_test.py to list available devices and set this value.
# Allow overriding via environment variable (useful for different machines or CI).
try:
    MIC_DEVICE_INDEX = int(os.getenv("MIC_DEVICE_INDEX", "1"))
except ValueError:
    MIC_DEVICE_INDEX = 1
