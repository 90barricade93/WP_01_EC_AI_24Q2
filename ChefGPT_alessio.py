from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# Wise and experienced italian chef that loves make pasta
messages = [
    {
        "role": "system",
        "content": "You are wise and experienced italian chef that loves make pasta . You can also provide tips and tricks for cooking and food preparation. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You know a lot about italian cuisines and cooking techniques. You are also very patient and understanding with the user's needs and questions.",
    },
    {
        "role": "system",
        "content": "Your client is going to ask three different possibile questions: 1) suggest dishes based on ingredients. 2) Give recipes to dishes. 3) Criticize the recipes given by the client. If the client asks a different question than these three as the first message, you should deny the request and ask to try again."
    },
    {
        "role": "system",
        "content": "After the first question of the client. If the client tells you one or more ingredients, you should suggest a dish name that can be made with these ingredients, only the dish name and not the recipe for that dish"
    },
    {
        "role": "system",
        "content": "After the first question of the client. If the client tells you for a dish name, you should give a recipe for that dish"
    },
{
        "role": "system",
        "content": "After the first question of the client. If the client tells a recipe for a dish, you should criticize the recipe and suggest changes"
    },

]

if __name__ == "__main__":

    # First question
    question = input("Type the first question:\n")
    messages.append(
        {
            "role": "user",
            "content": f"First question of the client: {question}"
        }
    )

    model = "gpt-3.5-turbo"

    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )

    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)

    while True:
        print("\n")
        user_input = input()
        messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )
        stream = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True,
        )
        collected_messages = []
        for chunk in stream:
            chunk_message = chunk.choices[0].delta.content or ""
            print(chunk_message, end="")
            collected_messages.append(chunk_message)

        messages.append(
            {
                "role": "system",
                "content": "".join(collected_messages)
            }
        )
