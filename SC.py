# client.py
import AntiCheat
from memory import *
import time
import os
import threading
import AntiCheat
def thebar(mainun):
    import socket
    import os
    HOST = '165.227.77.62'
    PORT = 12345
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        s.sendall(b"thebar")
        parts = r(f"the_bar_xy0").split(" ")
        xx, yy = int(parts[0]), int(parts[1])
        with open(os.path.join("variables", "currentbackground"), 'r') as f:
            cbg = f.read()
        with open(os.path.join("variables", "equipped_cosmetic"), 'r') as f:
            ec = f.read()
        power = AntiCheat.getthing("c", 3)
        s.sendall((str(xx) + " " + str(yy) + " " + mainun + " " + cbg + " " + power + " " + ec).encode("utf-8"))
        co = 0
        while True:
            co += 1
            data = s.recv(1024)
            if data.decode() == "done":
                break
            data = data.decode().strip("[]").replace("'", "").replace(",", "")
            data = ' '.join(data.split())
            x, y, un, lv, power, ec = data.split(" ")
            if un != mainun:
                pass
            if lv == cbg:
                if un == mainun:
                    w("the_bar_xy1", f"{x} {y}")
                else:
                    w(f"the_bar_xy{co}", f"{x} {y}")
            else:
                w(f"the_bar_xy{co}", f"-10 90")
            s.sendall(b"r")
        if not data:
            print("Server disconnected.")
