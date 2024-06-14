# from norwegian_chief import norwegian_chief
# from german Chief import german_chief
# from also_german_chief import also_german_chief
# from ---_chief import ---_chief
from src.Chief import Chief
from src.personalities import ITALIAN_CHIEF, DUTCH_CHIEF

italian_chief = Chief(ITALIAN_CHIEF)
dutch_chief = Chief(DUTCH_CHIEF)


def add_prompt_to_chiefs(prompt: str) -> None:
    italian_chief.add_user_message(prompt)
    dutch_chief.add_user_message(prompt)


def select_chief() -> Chief:
    print("Choose your chief:")
    print("1. Norwegian Chief")
    print("2. Italian Chief")
    print("3. German Chief")
    print("4. Also German Chief")
    print("5. --- Chief")
    print("6. Dutch Chief")

    chief = None

    while not chief:
        choice = input("Enter the number of your choice: ")
        # prompt = input("Enter your prompt: ")
        chief = None
        if choice == "1":
            print(norwegian_chef(prompt))
        elif choice == "2":
            chief = italian_chief
        elif choice == "3":
            print(german_chef(prompt))
        elif choice == "4":
            print(also_german_chef(prompt))
        elif choice == "5":
            print(---_chief(prompt))    
        elif choice == "6":
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
