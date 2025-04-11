import openai
import os
from dotenv import load_dotenv
import pandas as pd


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


import json

def load_symptom_data():
    with open("symptoms_data.json", "r") as f:
        return json.load(f)

symptom_data = load_symptom_data()


# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with API key
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_chatbot(user_input):
    """Sends user input to OpenAI and returns a chatbot response"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  
            messages=[
                {"role": "system", "content": "You are a helpful medical chatbot for symptom analysis."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content  # Corrected response access
    except Exception as e:
        return f"Error: {str(e)}"

# Run the chatbot in terminal
while True:
    print("Hi")
    user_input = input("Enter your symptoms (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    response = ask_chatbot(user_input)
    print("Chatbot:", response)
