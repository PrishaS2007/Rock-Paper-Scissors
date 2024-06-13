import random
def rock_paper_scissors():
    print("Welcome to Rock-Paper-Scissors.")

    choices = ['rock', 'paper', 'scissors']

    while True:
        # Computer's choice
        computer_choice = random.choice(choices)

        # User's choice
        user_choice = input("Enter your choice (rock/paper/scissors) or 'q' to quit: ").lower()

        if user_choice == 'q':
            print("Thanks for playing!")
            break

        if user_choice not in choices:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == 'rock':
            if computer_choice == 'scissors':
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif user_choice == 'paper':
            if computer_choice == 'rock':
                print("Paper covers rock! You win!")
            else:
                print("Scissors cut paper! You lose.")
        elif user_choice == 'scissors':
            if computer_choice == 'paper':
                print("Scissors cut paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")

        print("--------------------")

if __name__ == "__main__":
    rock_paper_scissors()