import random

class Rock_paper_scissors():

    def __init__(self):
        self.computers_choice = ["rock", "paper", "scissors"]
        self.player_score = 0
        self.computer_score = 0

    def play(self):
        computer = random.choice(self.computers_choice)
        selection = input("\nThe computer has chosen. What do you choose? (Rock/Paper/Scissors): ")

        if selection.lower() not in self.computers_choice:
            print("That is not a valid response.")
        else:
            print(f"\nYou chose {selection.upper()}. The computer chose {computer.upper()}. ")  
            if selection.lower() == computer:
                print("Draw.")
            elif selection.lower() == 'rock' and computer == 'scissors':
                self.player_score += 1
                print("You win!")
            elif selection.lower() == 'paper' and computer == 'rock':
                self.player_score += 1
                print("You win!")
            elif selection.lower() == 'scissors' and computer == 'paper':
                self.player_score += 1
                print("You win!")
            else:
                self.computer_score += 1
                print("You lose.")

    def scores(self):
        dict_one = {"Player" : self.player_score, "Computer" : self.computer_score}
        print(f"\nThe current score is {dict_one}")

game = Rock_paper_scissors()

def run_game():
    print("\nWelcome to Rock-Paper-Scissors! You will be playing against a computer opponent!")
    while True:
        response = input("\nWhat would you like to do? (Play/Score/Quit): ")
        if response.lower() == 'play':
            game.play()
        elif response.lower() == 'score':
            game.scores()
        elif response.lower() == 'quit':
            print(f"\nThank you for playing!")
            break
        else:
            print("That is not a valid response.")

run_game()