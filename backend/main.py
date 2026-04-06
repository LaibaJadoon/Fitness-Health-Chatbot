from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

from agent import agent

print("💬 Health Assistant Chatbot (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Take care! Stay healthy 👋")
        break

    response = agent.run_sync(user_input)

    print("Bot:", response.output)