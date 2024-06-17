# imports
from openai import OpenAI
import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# Create an instance of the OpenAI class
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def dutch_chef():
    # Create a list of system messages to be used in the chatbot
    messages = [
        {
            "role": "system",
            "content": "You are an experienced Innovated Dutch Chef. Who gives modern twists to traditional dishes and likes to experiment with new ingredients that helps people by suggesting detailed recipes for dishes they want to cook. You can also provide tips and tricks for cooking and food preparation. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You know a lot about different cuisines and cooking techniques. You also love to use icons in your output and are also very patient and understanding with the user's needs and questions.",
        },
        {
            "role": "system",
            "content": "Your client is going to ask three different possible questions: 1) suggest dishes based on ingredients. 2) Give recipes to dishes. 3) Criticize the recipe given by the client. If the client asks a different question than these three as the first message, you should deny the request and ask to try again.",
        },
        {
            "role": "system",
            "content": "After the first question of the client. If the client tells you one or more ingredients, you should suggest a dish name that can be made with these ingredients, only the dish name and not the recipe for that dish",
        },
        {
            "role": "system",
            "content": "After the first question of the client. If the client tells you for a dish name, you should give a recipe for that dish",
        },
        {
            "role": "system",
            "content": "After the first question of the client. If the client tells a recipe for a dish, you should criticize the recipe and suggest changes",
        },
    ]

    # Prompt the user to input the name of the dish they want a recipe for
    dish = input(
        "1) Provide ingredients, 2) requesting a dish name, or 3) sharing a recipe for criticism:\n"
    )

    # Add the user's input to the chat messages
    messages.append(
        {
            "role": "user",
            "content": f"Suggest me a detailed recipe and the preparation steps for making {dish}",
        }
    )

    # Specify the model to be used for chatbot generation
    model = "gpt-3.5-turbo"

    # Create a chatbot stream using the specified model and chat messages
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )

    # Create an empty list to store the chatbot's responses
    collected_messages = []

    # Iterate through the chatbot's responses and print them
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)

    # Add the chatbot's responses to the chat messages
    messages.append({"role": "system", "content": "".join(collected_messages)})

    # Continue the chatbot conversation until the user inputs 'exit'
    while True:
        print("\n")
        print("Type 'exit' to end the conversation.")
        user_input = input("prompt: ")
        if user_input == "exit":
            break

        # Add the user's input to the chat messages
        messages.append({"role": "user", "content": user_input})

        # Create a new chatbot stream using the specified model and chat messages
        stream = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True,
        )

        # Create an empty list to store the chatbot's responses
        collected_messages = []

        # Iterate through the chatbot's responses and print them
        for chunk in stream:
            chunk_message = chunk.choices[0].delta.content or ""
            print(chunk_message, end="")
            collected_messages.append(chunk_message)

        messages.append({"role": "system", "content": "".join(collected_messages)})
