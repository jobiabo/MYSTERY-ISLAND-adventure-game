from effects import typewriter
import config

def main_menu(): 
    return typewriter(config.MAIN_MENU)

def start_game():
    return typewriter(config.START_MESSAGE)


def find_map(energy_tracker):
    print(config.THE_LOST_MAP)

    while True:
        choice = input("Enter your choice: ").strip().lower()

        if choice == "1" or choice == "drowned secrets":
            print("The map was washed away!")
            print("You lost 1 energy point.")
            energy_tracker -= 1
            return energy_tracker, False

        elif choice == "2" or choice == "treacherous steps":
            print("You slipped on the unstable ground!")
            print("You lost 1 energy point.")
            energy_tracker -= 1
            return energy_tracker, False

        elif choice == "3" or choice == "sealed fortune":
            print("Congratulations! You secured the map.")
            return energy_tracker, True

        else:
            print("Invalid option! Please try again.")
            energy_tracker -= 1
            return energy_tracker, False
        


def jungle_welcome():
    print(config.PHASE_JUNGLE)

    print(input("PRESS ENTER TO BOOST YOUR ENERGY: "))
    print("ENERGY LEVEL BOOSTED!!!")

    print(f"Health: {config.PLAYER_STATE["health"]}")
    print(input("PRESS ENTER TO CHOOSE YOUR PATH: "))

    energy_tracker = 5
    
    while energy_tracker > 0:

        energy_tracker, success = jungle_path_selection(energy_tracker)

        print(f"ENERGY REMAINING: {energy_tracker}/5")

        # Check if the player succeeded
        if success:
            # Next Phase
            predator_trial_welcome()
            return

        # Check if the player has run out of energy
        if energy_tracker <= 0:
            print("YOU HAVE RUN OUT OF ENERGY!")
            print("GAME OVER!")
            return

        # Ask whether the player wants to retry
        retry = input(
            "Would you like to try again? (yes/no): ").strip().lower()

        if retry == "yes":
            print("You gather your strength and try again...")
            continue
        
        elif retry == "no":
            print("You have chosen to give up.")
            print("GAME OVER!")
            return

        else:
            print("Invalid response! Please enter yes or no.")



def jungle_path_selection(energy_tracker):
    print("""YOUR NEXT CHALLENGE: CHOOSE YOUR PATH!
            Two directions. Two different dangers. One chance to move forward.
            
            LEFT: The Hollow's Embrace : A silent path conceals a potentially deadly secret.
            RIGHT: The Predator's Trial: Something dangerous may be waiting among the shadows.
            Choose wisely. Your survival depends on it.""")
    while True:
        choice = input("Choose path: ").strip().lower()
        if choice == "1" or choice == "left" or choice == "hollow embrace":
            hollow_embrace()
            energy_tracker -= 1
            return energy_tracker, False
        elif choice == "2" or choice == "right" or choice == "the Predator's trial":
            return energy_tracker, True

def hollow_embrace():
    return config.HOLLOW_EMBRACE
 
def predator_trial_welcome():
    print("Predator trials responded")

def old_bridge_welcome():
    pass

def old_bridge_puzzle():
    pass

def lighthouse_welcome():
    pass

def find_key():
    pass

def ignite_torch():
    pass

def select_door_action():
    pass

def activate_rescue_beacon():
    pass