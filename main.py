# from indian_chef import indian_chef
import ChefGPT_alessio
# from french_chef import french_chef
# from mexican_chef import mexican_chef
from innovative_dutch_chef import innovative_dutch_chef  

def main():
    print("Choose your chef:")
    print("1. Indian Chef")
    print("2. Italian Chef")
    print("3. French Chef")
    print("4. Mexican Chef")
    print("5. Dutch Chef")  
    choice = input("Enter the number of your choice: ")

    prompt = input("Enter your prompt: ")

    if choice == "1":
        print(indian_chef(prompt))
    elif choice == "2":
        print(italian_chef(prompt))
    elif choice == "3":
        print(french_chef(prompt))
    elif choice == "4":
        print(mexican_chef(prompt))
    elif choice == "5":
        print(innovative_dutch_chef(prompt))  
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
