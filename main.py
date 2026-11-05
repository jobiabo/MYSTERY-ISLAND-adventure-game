from game_play import start_game
import sys



def main():
    while True:
        try:
            start_game()
        except:
            KeyboardInterrupt
            print("Do you want to quit?")
            choice = input("yes/no: ").strip().lower()
            if choice == "yes":
                print("Quiting...")
                print("Goodbye...")
                return
            elif choice == "no":
                continue
            else:
                if count == 3:
                    print("You failed to provide a valid input")
                    print("Game quiting...")
                    return
                count = 1
                print("invalid choice (yes/no)")
                count+=1
                continue
                
main()
