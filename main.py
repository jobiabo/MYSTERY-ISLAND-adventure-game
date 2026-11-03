from messages import main_menu
from config import GAME_INTRO
from effects import typewriter

def main():
    main_menu()
    START_COMMAND = input("PRESS ENTER OR ANY KEY TO CONTINUE: ")
    typewriter(START_COMMAND)
    typewriter(GAME_INTRO)    


    

main()
