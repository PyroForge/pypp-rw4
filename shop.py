import os
import screenwriter
import AntiCheat
os.system("cls" if os.name == "nt" else "clear")
while True:
    menu1 = [
        ["Stocks"],
        ["Trading Plaza"],
        ["Exit"]
    ]
    next1 = screenwriter.menu(menu1)
    if next1 == "Stocks":
        menu1 = [
            ["candy-pyramid Corp.     |   null   | Halloween 2024"],
            ["candy-mound Corp.       |   null   | Halloween 2024"],
            ["cash pyramid            |  999999  |               "],
            ["candy mound             |   9999   |               "]
        ]
        next1 = screenwriter.menu(menu1)
        name = next1
        if name == "candy-pyramid Corp.     |   null   | Halloween 2024":
            cost = 0
            can_buy = False
            id = 2
        if name == "candy-mound Corp.       |   null   | Halloween 2024":
            cost = 0
            can_buy = False
            id = 3
        if name == "cash pyramid            |  999999  |               ":
            cost = 999999
            can_buy = True
            id = 4
        if name == "candy mound             |   9999   |               ":
            cost = 9999
            can_buy = True
            id = 5

        if can_buy == True:
            menu1 = [
                ["Buy", "Sell", "Get ev", "Exit"],
            ]
        if can_buy == False:
            menu1 = [
                ["Sell", "Get ev", "Exit"]
            ]
        next1 = screenwriter.menu(menu1)

        if next1 == "Buy":
            print("buying 1...")
            AntiCheat.points("c", "-", 2, cost)
            print("your points have been removed")
            AntiCheat.points("s", "+", id, 1)
            print("your stock has been added")
        if next1 == "Sell":
            print("selling is not available yet please come back soon")
            input()
        if next1 == "Get ev":
            print("estimated value is", cost)
        if next1 == "Exit":
            pass
    if next1 == "Trading Plaza":
        print("cooming soon")
        exit()
    if next1 == "Exit":
        exit()
