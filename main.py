from messages import main_menu
from config import GAME_INTRO, START_MESSAGE
from effects import typewriter


def main():
    main_menu()
    input("PRESS ENTER OR ANY KEY TO CONTINUE: ")
    typewriter(START_MESSAGE)
    input("PRESS ENTER OR ANY KEY TO CONTINUE: ")
    typewriter(GAME_INTRO)
    typewriter(input("PRESS ENTER OR ANY KEY TO BEGIN ADVENTURE: "))

    

main()
