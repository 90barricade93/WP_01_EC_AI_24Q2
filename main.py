import src.norwegian_chef as norwegian_chef
import src.german_chef as german_chef
import src.swiss_chef as swiss_chef
import src.korean_chef as korean_chef
import src.dutch_chef as dutch_chef
from src.chef import Chef
from src.personalities import ITALIAN_CHEF

italian_chef = Chef(ITALIAN_CHEF)


def add_prompt_to_chefs(prompt: str) -> None:
    italian_chef.add_user_message(prompt)


def select_chef() -> Chef:
    print("Choose your chief:")
    print("1. Norwegian Chief")
    print("2. Italian Chief")
    print("3. German Chief")
    print("4. Swiss Chief")
    print("5. korean Chief")
    print("6. Dutch Chief")

    chef = None

    while not chef:
        choice = input("Enter the number of your choice: ")
        # prompt = input("Enter your prompt: ")
        chef = None
        if choice == "1":
            chef = norwegian_chef.norwegian_chef()
        elif choice == "2":
            chef = italian_chef
        elif choice == "3":
            chef = german_chef.german_chef()
        elif choice == "4":
            chef = swiss_chef.swiss_chef()
        elif choice == "5":
            chef = korean_chef.korean_chef()
        elif choice == "6":
            chef = dutch_chef.dutch_chef()
        else:
            print("Invalid choice. Please try again.")

    return chef


def main():
    # First question
    dish = input(
        "Provide ingredients, requesting a dish name, or sharing a recipe for criticism:\n"
    )
    add_prompt_to_chefs(dish)
    chef = select_chef()
    print(chef.get_response())

    while True:
        print("\n")
        print("Type 'exit' to end the conversation.")
        user_input = input("prompt: ")
        if user_input == "exit":
            break

        add_prompt_to_chefs(user_input)
        chef = select_chef()
        print(chef.get_response())


if __name__ == "__main__":
    main()
