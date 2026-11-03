from effects import typewriter
import config

def main_menu(): 
    return typewriter(config.MAIN_MENU)

def start_game():
    return typewriter(config.START_MESSAGE)

def find_map():
    print(config.THE_LOST_MAP)
    choice = input("Enter choice either 1 or the text: ").strip().lower()
    if choice == "1" or "drowned secrets":
        print("""The map was soaked up before you reached it
        You died after few minutes on the island due to hunger
        YOU LOST!!!""")
        

    if choice == "2" or "treacherous steps":
        print("""You slipped on the ground due to uncertainty and died
        YOU LOST!!!""")


    if choice == "3" or "sealed fortune":
        print("Congratulations, You have Successfully secured the map")
        jungle_welcome()


    else:
        print("Enter valid opt")

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