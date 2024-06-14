from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


class Chief:

    def __init__(self, personality: str):
        self.client = OpenAI()
        self.messages = [
            {
                "role": "system",
                "content": f"{personality}",
            },
            {
                "role": "system",
                "content": "Your client is going to ask three different possible questions: 1) suggest dishes based on ingredients. 2) Give recipes to dishes. 3) Criticize the recipes given by the client. If the client asks a different question than these three as the first message, you should deny the request and ask to try again."
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

    def add_user_message(self, user_input) -> str:
        self.messages.append({
            "role": "user",
            "content": user_input
        })

    def get_response(self) -> str:
        model = "gpt-3.5-turbo"
        stream = self.client.chat.completions.create(
            model=model,
            messages=self.messages,
            stream=True,
        )
        collected_messages = []
        for chunk in stream:
            chunk_message = chunk.choices[0].delta.content or ""
            collected_messages.append(chunk_message)

        response = "".join(collected_messages)
        self.messages.append({
            "role": "system",
            "content": response
        })
        return response
