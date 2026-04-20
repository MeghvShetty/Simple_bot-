# chatbot/agent.py
from google.adk.agents import LlmAgent
from google.adk.tools import google_search
import os

os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "TRUE"
os.environ["GOOGLE_CLOUD_PROJECT"] = "infantry-480110"
os.environ["GOOGLE_CLOUD_LOCATION"] = "europe-west4"

# -- Simple Chatbot Agent --
chatbot_agent = LlmAgent(
    name="SimpleChatbot",
    model="gemini-2.5-pro",
    instruction="""You are a helpful, friendly chatbot assistant.
    
    Your responsibilities:
    - Answer user questions clearly and concisely
    - Use Google Search when you need up-to-date or factual information
    - Maintain a conversational and helpful tone
    - If you don't know something, say so honestly
    """,
    description="A simple conversational chatbot with search capabilities",
    tools=[google_search],
)

# --- Root Agent for the Runner ---
root_agent = chatbot_agent
