from src.Chief import Chief

personality = "You are wise and experienced italian chef that loves make pasta . You can also provide tips and tricks for cooking and food preparation. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You know a lot about italian cuisines and cooking techniques. You are also very patient and understanding with the user's needs and questions."


def italian_chef(prompt: str) -> str:
    chief = Chief(personality)
    chief.add_user_message(prompt)
    return chief.get_response()


if __name__ == "__main__":

    chief = Chief(personality)

    # First question
    question = input("Type the first question:\n")
    chief.add_user_message(question)
    response = chief.get_response()
    print(response)

    while True:
        print("\n")
        user_input = input()
        chief.add_user_message(user_input)
        response = chief.get_response()
        print(response)
