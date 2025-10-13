import random

class Game:
    def get_user_item(self):
        """Demande le choix de l'utilisateur et valide l'entrée."""
        while True:
            user_input = input("Choose rock, paper, or scissors: ").lower()
            if user_input in ["rock", "paper", "scissors"]:
                return user_input
            print("Invalid choice. Please choose again.")

    def get_computer_item(self):
        """Génère un choix aléatoire pour l'ordinateur."""
        return random.choice(["rock", "paper", "scissors"])

    def get_game_result(self, user_item, computer_item):
        """Compare les choix et détermine le gagnant."""
        if user_item == computer_item:
            return "draw"
        elif (user_item == "rock" and computer_item == "scissors") or \
             (user_item == "paper" and computer_item == "rock") or \
             (user_item == "scissors" and computer_item == "paper"):
            return "win"
        else:
            return "loss"

    def play(self):
        """Lance une partie complète et retourne le résultat."""
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        print(f"You selected {user_item}. The computer selected {computer_item}.")
        if result == "win":
            print("You won!")
        elif result == "loss":
            print("You lost.")
        else:
            print("It's a draw.")
        return result