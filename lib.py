import os
import time

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

if __name__ == "__main__":
    clear()
    print("I get you are curious, but why did you run the lib.py directly?")
    time.sleep(4)
    print("It would probably be a better use of your time to make some mods for the BAR, it's not that hard you know.")
    time.sleep(4)
    input("> ")
    exit()
