from messages import get_main_menu, find_map, jungle_welcome, ask_retry, move_to
from config import get_game_intro, get_start_message, player_signup, reset_player_state
from effects import typewriter

def start_game():
    reset_player_state()

    while True:
        print(get_main_menu())

        input("PRESS ENTER OR ANY KEY TO CONTINUE: ")
        if not player_signup():
            print("Please provide a username")
            continue
        return game_progress()


def game_progress():
    typewriter(get_start_message())
    input("PRESS ENTER OR ANY KEY TO CONTINUE: ")
    typewriter(get_game_intro())
    print("\n")
    input("PRESS ENTER TO BEGIN ADVENTURE: ")
    move_to("beach")
    
    

    energy_tracker = 5

    while energy_tracker > 0:
    
        energy_tracker, success = find_map(energy_tracker)
        from config import PLAYER_STATE
        PLAYER_STATE["health"] = energy_tracker
        
        

        print(f"ENERGY REMAINING: {energy_tracker}/5")

        # Check if the player succeeded
        # Next Phase: JUNGLE WELCOME
        if success:
            jungle_welcome()
            return

        # Check if the player has run out of energy
        if energy_tracker <= 0:
            print("YOU HAVE RUN OUT OF ENERGY!")
            print("GAME OVER!")
            return

        # Ask whether the player wants to retry
        ask_retry()


def decide_replay(choice, message):
    while True:
        try:
            if choice == "yes":
                return "yes", True

            elif choice == "no":
                return "no", False

            print("Invalid response! Please enter yes or no.")
            choice = input(f"{message} (yes/no): ").strip().lower()
            continue
        except KeyboardInterrupt:
            err_message = "You forcefully ended the game..."
            return err_message, False

