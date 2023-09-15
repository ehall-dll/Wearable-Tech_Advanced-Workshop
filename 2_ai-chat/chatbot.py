import openai
import os

# Set your OpenAI API key
openai.api_key = 'Insert API Key Here'

conversation = ""

os.system("clear")

while True:
    # Get the user's message
    message = input("You: ")

    # Append the user's message to the conversation
    conversation += f"You: {message}\n"

    # Get the model's response
    response = openai.Completion.create(
        engine="text-davinci-002",  # Use the davinci model
        prompt=conversation,
        max_tokens=60
    )

    # Append the model's response to the conversation
    chatbot_response = response.choices[0].text.strip()
    conversation += "Chatbot: " + chatbot_response + "\n"

    print("Chatbot: " + chatbot_response)
