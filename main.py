import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

system_instruction = """
You are a friendly, helpful, and welcoming AI assistant.
Always respond in a warm, polite, and encouraging tone.
Keep your responses helpful and concise.
"""

chat = client.chats.create(
    model="gemini-2.5-flash",
    config=genai.types.GenerateContentConfig(
        system_instruction=system_instruction,
    )
)

print("Bot : Hey there! How can I help you today? Type 'bye' to exit.")

while True:
    you = input("you : ")
    if you.lower() == "bye":
        print("Bot : Goodbye! Have a great day!")
        break
    reply = chat.send_message(you)
    print("bot : ", reply.text)

