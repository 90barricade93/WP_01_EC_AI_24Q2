# from indian_chef import indian_chef
from ChefGPT_alessio import italian_chef
# from french_chef import french_chef
# from mexican_chef import mexican_chef
from innovative_dutch_chef import innovative_dutch_chef
from src.Chief import Chief
from src.personalities import ITALIAN_CHEF, DUTCH_CHEF

italian_chief = Chief(ITALIAN_CHEF)
dutch_chief = Chief(DUTCH_CHEF)


def add_prompt_to_chiefs(prompt: str) -> None:
    italian_chief.add_user_message(prompt)
    dutch_chief.add_user_message(prompt)


def select_chief() -> Chief:
    print("Choose your chef:")
    print("1. Indian Chef")
    print("2. Italian Chef")
    print("3. French Chef")
    print("4. Mexican Chef")
    print("5. Dutch Chef")

    chief = None

    while not chief:
        choice = input("Enter the number of your choice: ")
        # prompt = input("Enter your prompt: ")
        chief = None
        if choice == "1":
            print(indian_chef(prompt))
        elif choice == "2":
            chief = italian_chief
        elif choice == "3":
            print(french_chef(prompt))
        elif choice == "4":
            print(mexican_chef(prompt))
        elif choice == "5":
            chief = dutch_chief
        else:
            print("Invalid choice. Please try again.")

    return chief


def main():
    # First question
    dish = input("Provide ingredients, requesting a dish name, or sharing a recipe for criticism:\n")
    add_prompt_to_chiefs(dish)
    chief = select_chief()
    print(chief.get_response())

    while True:
        print("\n")
        print("Type 'exit' to end the conversation.")
        user_input = input("prompt: ")
        if user_input == "exit":
            break

        add_prompt_to_chiefs(user_input)
        chief = select_chief()
        print(chief.get_response())


if __name__ == "__main__":
    main()
