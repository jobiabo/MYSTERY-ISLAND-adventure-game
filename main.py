from game_play import start_game
from config import PLAYER_STATE
from game_play import decide_replay


def main():
    while True:
        try:
            start_game()
            if PLAYER_STATE["game_progress"] == "completed":
                message = "Would you like to play again?"
                choice = input("(yes/no): ").strip().lower()
                if decide_replay(choice, message):
                    continue
                return
            print("")
                
        except KeyboardInterrupt:
            message = "Do you want to quit?"
            choice = input("yes/no: ").strip().lower()
            if decide_replay(choice, message):
                print("Quiting...")
                print("goodbye...")
                return
            continue
                
main()
