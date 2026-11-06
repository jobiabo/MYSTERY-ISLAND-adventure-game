from game_play import start_game
from config import PLAYER_STATE
from game_play import decide_replay
import sys


def main():
    while True:
        try:
            start_game()
            if PLAYER_STATE["game_progress"] == "completed":
                message = "Would you like to play again?"
                print(message)
                choice = input("(yes/no): ").strip().lower()
                response, success = decide_replay(choice, message)
                if success:
                    print("Welcome back! Let's play again.")
                    continue
                if response == "no":
                    print("Quiting...")
                    print("Goodbye...")
                    return  
            print("")
                
        except KeyboardInterrupt:
            message = "Do you want to quit?"
            print(message)
            try:
                choice = input("yes/no: ").strip().lower()
                message, success = decide_replay(choice, message)
                if success:
                    print("Quiting...")
                    print("goodbye...")
                    return
                continue
            except KeyboardInterrupt:
                print("You forcefully ended the game...")
                sys.exit("Good bye...")

      
main()
