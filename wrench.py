import time
import os
import screenwriter
import AntiCheat
while True:
    m = [
        ["Verify save authenticity"],
        [""],
        ["Exit"]
    ]
    next1 = screenwriter.menu(m)
    if next1 == "Verify save authenticity":
        print("Verifying...")
        time.sleep(2)
        AntiCheat.points("c", "+", 2, 1)
        print(AntiCheat.verify())
        input()