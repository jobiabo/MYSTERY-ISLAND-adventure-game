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
            continue


def jungle_welcome():
    print("Jungle responded")

def jungle_path_selection():
    pass

def hollow_embrace():
    pass

def predator_trial():
    pass

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