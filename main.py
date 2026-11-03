from messages import main_menu, find_map, jungle_welcome, predator_trial_welcome
from config import GAME_INTRO, START_MESSAGE
from effects import typewriter



def main():
    main_menu()

    input("PRESS ENTER OR ANY KEY TO CONTINUE: ")
    typewriter(START_MESSAGE)

    input("PRESS ENTER OR ANY KEY TO CONTINUE: ")
    typewriter(GAME_INTRO)

    input("PRESS ENTER TO BEGIN ADVENTURE: ")
    
    predator_trial_welcome()

    # energy_tracker = 5

    # while energy_tracker > 0:

    #     energy_tracker, success = find_map(energy_tracker)
    #     from config import PLAYER_STATE
    #     PLAYER_STATE["health"] = energy_tracker
        
        

    #     print(f"ENERGY REMAINING: {energy_tracker}/5")

    #     # Check if the player succeeded
    #     if success:
    #         jungle_welcome()
    #         return

    #     # Check if the player has run out of energy
    #     if energy_tracker <= 0:
    #         print("YOU HAVE RUN OUT OF ENERGY!")
    #         print("GAME OVER!")
    #         return

    #     # Ask whether the player wants to retry
    #     retry = input(
    #         "Would you like to try again? (yes/no): ").strip().lower()

    #     if retry == "yes":
    #         print("You gather your strength and try again...")
    #         continue

    #     elif retry == "no":
    #         print("You have chosen to give up.")
    #         print("GAME OVER!")
    #         return

    #     else:
    #         print("Invalid response! Please enter yes or no.")


main()
