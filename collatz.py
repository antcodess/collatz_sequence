# -------------------------------------------
#      The Simple Collatz Sequence App
# -------------------------------------------
import os


def clear_screeen():
    os.system('cls' if os.name == 'nt' else 'clear')


def collatz(number):
    if number % 2 == 0:
        return number // 2
    if number % 2 == 1:
        return 3 * number + 1


def main_menu():
    print("-" * 40)
    print("The Simple Collatz Sequence Console App")
    print("-" * 40)
    print("\nWelcome to this super simple Collatz Sequence Console app!")
    print("""
Start with any positive number and I will tell you(and show you!) how many
steps it will take to reach 1 using the Collatz sequence theory.
""")


def sequence():

    run = True
    attempts = 0

    while True:

        try:
            user_number = int(input("Enter a number: "))

            while run:

                if user_number <= 0:
                    print("** Whoops! Input must be positive! **")
                    break

                elif user_number != 1:
                    user_number = collatz(user_number)
                    print(user_number)
                    attempts += 1

                elif user_number == 1:
                    run = False
                    print("\nIt took {} steps to reach 1!".format(attempts))

        except ValueError:
            print("** Input must be integer! **")

        user_input = input("\nWhat you like to play again? (Y/N): ").lower()

        if user_input == "y" or user_input == "yes":
            run = True
            attempts = 0
            clear_screeen()
            continue

        elif user_input == "n" or user_input == "no":
            clear_screeen()
            print("Thank you for using the app!\n")
            break

        else:
            clear_screeen()
            print("I don't understand that! If you want to play again, please rerun me. Quiting program...")
            print("\nThank you for using the app!\n")
            break


if __name__ == "__main__":

    main_menu()
    sequence()