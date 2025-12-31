import threading
import time
import os
import sys
import AntiCheat
import pyicon
import screenwriter
import logo
import lib
def logo_t():
    # video loader thread
    logo.main()
    with open(os.path.join("variables", "kill"), "w") as nf:
        nf.write("1")
def screen_logo_t():
    screenwriter.render("current_frame.bmp", False)
t1 = threading.Thread(target=logo_t)
t2 = threading.Thread(target=screen_logo_t)
t1.start()
t2.start()
t1.join()
t2.join()
lib.clear()
# stuff to fix the terminal so it accepts input
sys.stdout.flush()
print("\033[0m", end='')
if sys.stdin.closed:
    sys.stdin = open('CON' if os.name == 'nt' else '/dev/tty', 'r')
print("V0.0.1  pre-release 1 DEV")
d = input()
if d == "new":
    un = input("Username: ")
    AntiCheat.new_account(un , "")
if d == "reset":
    with open(os.path.join("variables", "equipped_cosmetic"), "w") as a:
        a.write(f"0")
    with open(os.path.join("variables", "the_bar_xy0"), "w") as a:
        a.write("1 90")
    with open(os.path.join("variables", "the_bar_xy1"), "w") as a:
        a.write("-10 90")
    with open(os.path.join("variables", "the_bar_xy2"), "w") as a:
        a.write("-10 90")
    with open(os.path.join("variables", "the_bar_xy3"), "w") as a:
        a.write("-10 90")
    with open(os.path.join("variables", "the_bar_xy4"), "w") as a:
        a.write("-10 90")
    with open(os.path.join("variables", "the_bar_xy5"), "w") as a:
        a.write("-10 90")
    with open(os.path.join("variables", "the_bar_xy6"), "w") as a:
        a.write("-10 90")
    with open(os.path.join("variables", "the_bar_xy7"), "w") as a:
        a.write("-10 90")
    with open(os.path.join("variables", "the_bar_xy8"), "w") as a:
        a.write("-10 90")
    with open(os.path.join("variables", "the_bar_xy9"), "w") as a:
        a.write("-10 90")
    with open(os.path.join("variables", "the_bar_xy10"), "w") as a:
        a.write("-10 90")
    with open(os.path.join("variables", "the_bar_xy11"), "w") as a:
        a.write("-10 90")
    with open(os.path.join("variables", "currentbackground"), "w") as a:
        a.write("lv1.bmp")
    with open(os.path.join("variables", "thebar_ps"), "w") as a:
        a.write("bob0.bmp")
    with open(os.path.join("variables", "xy"), "w") as a:
        a.write("0 0")
    with open(os.path.join("variables", "new_frame"), "w") as a:
        a.write("1")
    with open(os.path.join("variables", "kill"), "w") as a:
        a.write("0")
    with open(os.path.join("variables", "currentcolor"), "w") as a:
        a.write("1")
# main Rotator screen
while True:
    pyicon.no_file()
    print("Drawing Battle (2d!)")
    next1 = input()
    if next1 != "":
        os.system("py drawing_battle.py" if os.name == "nt" else "python3 drawing_battle.py")
    pyicon.the_bar_icon_x100_40()
    print("TheBAR (2d!)")
    next1 = input()
    if next1 != "":
        os.system("py thebar.py" if os.name == "nt" else "python3 thebar.py")
    pyicon.setup_icon_x100_40()
    print("Smaller games")
    next1 = input()
    if next1 != "":
        pyicon.no_file()
        print("AFK")
        next1 = input()
        if next1 != "":
            os.system("py afk.py" if os.name == "nt" else "python3 afk.py")
    pyicon.app_store_icon_x100_40()
    print("Other applications")
    next1 = input()
    if next1 != "":
        pyicon.shop_gold_icon_x100_40()
        print("Shop")
        next1 = input()
        if next1 != "":
            os.system("py shop.py" if os.name == "nt" else "python3 shop.py")
        pyicon.py_wrench_icon_x100_40()
        print("Wrench")
        next1 = input()
        if next1 != "":
            os.system("py wrench.py" if os.name == "nt" else "python3 wrench.py")
