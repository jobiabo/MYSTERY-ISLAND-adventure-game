from effects import typewriter
from config import get_main_menu, get_start_message, get_the_lost_map, get_phase_jungle, get_player_health, get_predator_welcome, get_hollow_embrace, get_old_bridge_welcome, get_bridge_success, get_light_house_welcome, get_find_key_puzzle, get_find_key_success, get_ignite_torch_welcome, get_ignite_torch_success, get_jammed_door_welcome, get_jammed_door_success, get_rescue_beacon_welcome, get_rescue_beacon_success, PLAYER_STATE
import sys
def main_menu(): 
    return typewriter(get_main_menu())

def start_game():
    return typewriter(get_start_message())


def find_map(energy_tracker):
    print(get_the_lost_map())

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
    print(get_phase_jungle())

    print(input("PRESS ENTER TO BOOST YOUR ENERGY: "))
    print("ENERGY LEVEL BOOSTED!!!")

    print(f"Health: ", get_player_health())
    print(input("PRESS ENTER TO CHOOSE YOUR PATH: "))

    energy_tracker = 5
    
    while energy_tracker > 0:

        energy_tracker, success = jungle_path_selection(energy_tracker)

        print(f"ENERGY REMAINING: {energy_tracker}/5")

        # Check if the player succeeded
        if success:
            # Next Phase: PREDATOR ENCOUNTER
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
            sys.exit()

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
            print(hollow_embrace())
            energy_tracker -= 1
            return energy_tracker, False
        elif choice == "2" or choice == "right" or choice == "the predator's trial":
            return energy_tracker, True
        else:
            print("Enter valid response (1/2): ")
            continue

def hollow_embrace():
    return get_hollow_embrace()


 
def predator_trial_welcome():
    print(get_predator_welcome())
    print(input("PRESS ENTER TO BOOST YOUR ENERGY: "))
    print("ENERGY LEVEL BOOSTED!!!")

    print(f"Health: ", get_player_health())
    print(input("PRESS ENTER TO CONTINUE TO THE NEXT LEVEL: "))

    energy_tracker = 5
    
    while energy_tracker > 0:

        energy_tracker, success = predator_engage(energy_tracker)

        print(f"ENERGY REMAINING: {energy_tracker}/5")

        # Check if the player succeeded
        if success:
            # Next Phase: OLD BRIDGE WELCOME
            old_bridge_welcome()
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
            sys.exit()

        else:
            print("Invalid response! Please enter yes or no.")
    

def predator_engage(energy_tracker):
    print("PRESS ENTER TO ENGAGE: ")
    sys_dodge = ["DODGE", "MOVE"]
    sys_attack = ["ATTACK", "STRIKE", "SLASH"]
    _dodged = []
    _attack = []
    print("""The beast launches a powerful strike towards you!
            Quick! Unscramble the words to dodge its attack and survive!""")
    
    userinput1 = input("OGDED: ").strip().upper()
    _dodged.append(userinput1)
    userinput2 = input("VOME: ").strip().upper()
    _dodged.append(userinput2)


    print(_dodged)
    print(_attack)

    if _dodged == sys_dodge:
        print("ARRANGE 3 SCRAMBLED WORDS TO ATTACK")
        userinput3 = input("TATKAC: ").strip().upper()
        _attack.append(userinput3)
        userinput4 = input("KISTRE: ").strip().upper()
        _attack.append(userinput4)
        userinput5 = input("ASHLS: ").strip().upper()
        _attack.append(userinput5)

        if _attack == sys_attack:
            print("YOU HAVE CONQUERED THE BEAST SUCCESSFULLY")
            input("PRESS ENTER TO PICK UP AN INVENTORY: ")
            print("YOU HAVE SUCCESSFULLY PICKED UP A ROPE")
            return energy_tracker, True
        elif _attack != sys_attack:
            print("You couldn't strike the beast")
            print("You missed a word")
            print("And the beast devoured you")
            energy_tracker-=1
            return energy_tracker, False
    else:
        print("You couldn't unscrambled the word")
        print("You are hit")
        energy_tracker-=1
        return energy_tracker, False


def old_bridge_welcome():
    print(get_old_bridge_welcome())
    print(input("PRESS ENTER TO BOOST YOUR ENERGY: "))
    print("ENERGY LEVEL BOOSTED!!!")

    print(f"Health: ", get_player_health())
    print(input("PRESS ENTER TO CONTINUE TO THE NEXT LEVEL: "))

    energy_tracker = 5
    
    while energy_tracker > 0:

        energy_tracker, success = old_bridge_puzzle(energy_tracker)

        print(f"ENERGY REMAINING: {energy_tracker}/5")

        # Check if the player succeeded
        if success:
            # Next Phase: LIGHT HOUSE WELCOME 
            lighthouse_welcome()
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
            sys.exit()

        else:
            print("Invalid response! Please enter yes or no.")

def old_bridge_puzzle(energy_tracker):
    print("UNSCRAMBLED WORDS TO REMOVE ROPE AND SET THE BRIDGE")
    sys_list = ["ROPE", "PULL", "PLACE"]
    user_list = []
    userinput1 = input("EOPR: ").strip().upper()
    user_list.append(userinput1)
    userinput2 = input("LUPL: ").strip().upper()
    user_list.append(userinput2)
    userinput3 = input("ACPLE: ").strip().upper()
    user_list.append(userinput3)

    if user_list == sys_list:
        print(get_bridge_success())
        return energy_tracker, True
    else:
        print("Puzzled failed")
        print("Bridge was not placed successfully")
        energy_tracker-=1
        return energy_tracker, False
    


def lighthouse_welcome():
    print(get_light_house_welcome())
    print(input("PRESS ENTER TO BOOST YOUR ENERGY: "))
    print("ENERGY LEVEL BOOSTED!!!")

    print(f"Health: ", get_player_health())
    print(input("PRESS ENTER TO CONTINUE TO THE NEXT LEVEL: "))

    energy_tracker = 5
    
    while energy_tracker > 0:

        energy_tracker, success = find_key(energy_tracker)

        print(f"ENERGY REMAINING: {energy_tracker}/5")

        # Check if the player succeeded
        if success:
            # Next Phase: IGNITE TORCH INTRO
            ignite_torch_welcome()
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
            sys.exit()

        else:
            print("Invalid response! Please enter yes or no.")
    

def find_key(energy_tracker):
    print(get_find_key_puzzle())
    userinput = input("Enter choice here: ").strip().lower()
    if userinput == "1" or userinput == "the silent guardian":
        energy_tracker -= 1
        return energy_tracker, False
    elif userinput == "2" or userinput == "the brittle relic":
        energy_tracker -= 1
        return energy_tracker, False

    elif userinput == "3" or userinput == "the keeper's fortune":
        print(get_find_key_success())
        return energy_tracker, True
    else:
        print("invalid input enter option 1 or 2 or 3")
        energy_tracker -= 1
        return energy_tracker, False

def ignite_torch_welcome():
    print(get_ignite_torch_welcome())

    print(input("PRESS ENTER TO BOOST YOUR ENERGY: "))
    print("ENERGY LEVEL BOOSTED!!!")

    print(f"Health: ", get_player_health())
    print(input("PRESS ENTER TO CONTINUE TO THE NEXT LEVEL: "))

    energy_tracker = 5
    
    while energy_tracker > 0:

        energy_tracker, success = ignite_touch_puzzle(energy_tracker)

        print(f"ENERGY REMAINING: {energy_tracker}/5")

        # Check if the player succeeded
        if success:
            # Next Phase: IGNITE TORCH INTRO
            jam_door_welcome()
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
            sys.exit()

        else:
            print("Invalid response! Please enter yes or no.")

def ignite_touch_puzzle(energy_tracker):
    input("PRESS ENTER TO BEGIN YOUR PUZZLE: ")
    sys_data = ["STICK", "GAS", "FLAME", "TORCH", "LIGHT"]
    user_data = []

    input_I = input("KISCT: ").strip().upper()
    user_data.append(input_I)
    input_II = input("AGS: ").strip().upper()
    user_data.append(input_II)
    input_III = input("MAEFL: ").strip().upper()
    user_data.append(input_III)
    input_IV = input("HTROC: ").strip().upper()
    user_data.append(input_IV)
    input_V = input("THGIL: ").strip().upper()
    user_data.append(input_V)

    if user_data == sys_data:
        print(get_ignite_torch_success())
        return energy_tracker, True
    
    print("Puzzle failed! Your attempt to ignite the torch was unsuccessful.")
    energy_tracker-=1
    return energy_tracker, False


def jam_door_welcome():
    print(get_jammed_door_welcome())

    print(input("PRESS ENTER TO BOOST YOUR ENERGY: "))
    print("ENERGY LEVEL BOOSTED!!!")

    print(f"Health: ", get_player_health())
    print(input("PRESS ENTER TO CONTINUE TO THE NEXT LEVEL: "))

    energy_tracker = 5
    
    while energy_tracker > 0:

        energy_tracker, success = jam_door_action(energy_tracker)

        print(f"ENERGY REMAINING: {energy_tracker}/5")

        # Check if the player succeeded
        if success:
            # Next Phase: ACTIVATE RESCUE BEACON
            activate_rescue_beacon()
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
            sys.exit()

        else:
            print("Invalid response! Please enter yes or no.")



def jam_door_action(energy_tracker):
    input("PRESS ENTER TO BEGIN YOUR PUZZLE: ")
    sys_data = ["PUSH", "PULL", "BLAST"]
    user_data = []

    input_I = input("SUHP: ").strip().upper()
    user_data.append(input_I)
    input_II = input("LULP: ").strip().upper()
    user_data.append(input_II)
    input_III = input("ASBLT: ").strip().upper()
    user_data.append(input_III)

    if user_data == sys_data:
        print(get_jammed_door_success())
        return energy_tracker, True

    print("Puzzle failed! Your attempt to get through the door was unsuccessful.")
    energy_tracker-=1
    return energy_tracker, False

def activate_rescue_beacon():
    print(get_rescue_beacon_welcome())
    input("PRESS ENTER TO ACTIVATE THE RESCUE BEACON...")
    print(get_rescue_beacon_success())
    PLAYER_STATE["game_progress"] = "completed"
    return
    