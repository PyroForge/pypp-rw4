import time
from lib import *

while True:
    print("""
pretend  :)
this     :D
is       :/
an       :(
image    :)
""")
    print("RW1 games")
    print("(y:open, newline:next, q:exit)")
    i = input("> ").strip().lower()
    if i == "y":
        clear()
        print("Uhh sorry not yet :(")
        time.sleep(2)
        input("> ")
    elif i == "q":
        exit()
