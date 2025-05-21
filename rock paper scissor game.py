import random


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win! 🎉"
    else:
        return "You lose! 😔"


def play_game():
    print("Rock-Paper-Scissors Game!")
    player = input("Choose rock, paper, or scissors: ").lower()
    
    if player not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Try again.")
        return
    
    computer = get_computer_choice()
    print(f"Computer chose: {computer}")
    
    print(get_winner(player, computer))

play_game()
