import os
import random
import multiprocessing
import threading
from playsound import playsound
import screenwriter
import AntiCheat
import SC
import time
from memory import r as rea
from memory import w as whi
from memory import cleanup as cla
def play_s(thing):
    def p(thing):
        playsound(os.path.join("thebar", thing))
    t = threading.Thread(target=p, args=(thing,))
    t.start()
def willq1():
    time.sleep(0.3)
    cbg = rea("currentbackground")
    if cbg == "FPloading.bmp":
        pass
    else:
        whi("currentbackground", "will1.bmp")
        time.sleep(1)
        play_s("willsq1.mp3")
        time.sleep(66)
        whi("currentbackground", "lv0.bmp")
def tf():
    whi("physics_yn", "1")
    play_s("trueform.mp3")
    time.sleep(15)
    while True:
        with open(os.path.join("variables", "equipped_cosmetic"), "r") as a:
            ec = a.read()
        if ec == "0":
            whi("physics_yn", "0")
            whi("the_bar_ps0", "bob0.bmp")
        else:
            whi("the_bar_ps0", "trueform_200.bmp")
            whi("the_bar_ps0", "trueform1_200.bmp")
            whi("the_bar_ps0", "trueform2_200.bmp")
def forms():
    xy1 = rea("the_bar_xy-1").split(" ")
    xy2 = rea("the_bar_xy-2").split(" ")
    cbg1 = rea("the_bar_cbg-1")
    cbg2 = rea("the_bar_cbg-2")
    ps1 = rea("the_bar_ps-1")
    ps2 = rea("the_bar_ps-2")
    if random.randint(0, 5) == 0:
        x1, y1 = int(xy1[0]), int(xy1[1])
        x1 = x1 + random.randint(-1, 4)
        x1, y1 = form_physics(x1, y1)
        whi("the_bar_xy-1", f"{x1} {y1}")
    if random.randint(0, 5) == 0:
        x2, y2 = int(xy2[0]), int(xy2[1])
        x2 = x2 + random.randint(-1, 4)
        x2, y2 = form_physics(x2, y2)
        whi("the_bar_xy-2", f"{x2} {y2}")
def level():
    whi("currentbackground", "level.bmp")
    whi("the_bar_ps-6", "p1.bmp")
    whi("the_bar_ps-7", "p2.bmp")
    whi("the_bar_ps-8", "p3.bmp")
    whi("the_bar_ps-9", "p4.bmp")
    whi("the_bar_ps-10", "p5.bmp")
    whi("the_bar_ps-11", "d1.bmp")
    whi("the_bar_ps-12", "d2.bmp")
    whi("the_bar_ps-13", "d3.bmp")
    whi("the_bar_ps-14", "d4.bmp")
    whi("the_bar_ps-15", "d5.bmp")
    for ii in range(-10, -5):
        while True:
            while True:
                xr = random.randint(1, 100)
                if xr > 85:
                    pass
                else:
                    break
            while True:
                yr = random.randint(1, 100)
                if yr > 85:
                    pass
                else:
                    break
            #if ii == -10:
            #    pass
            #else:
            #    asb = abs(ii)
            #    asb = asb - 10
            #    asb = asb - (asb * 2)
            #    for i in range(-10, asb):
            #        xyy = rea(f"the_bar_xy{i}").split(" ")
            #        x = int(xyy[0])
            #        y = int(xyy[1])
            #        xy = rea(f"the_bar_xy{ii}").split(" ")
            #        xo = int(xy[0])
            #        yo = int(xy[1])
            #        x2 = xo
            #        y2 = yo
            #        x1 = xo + 9
            #        y1 = yo + 11
            #        if x2 <= x:
            #            if x <= x1:
            #                if y2 <= y:
            #                    if y <= y1:
            #                        pass
            #                    else:
            #                        break
            #                else:
            #                    break
            #            else:
            #                break
            #        else:
            #            break
            #        break
            break
        whi(f"the_bar_xy{ii}", f"{xr} {yr}")
    for ii in range(-15, -10):
        xr = random.randint(1, 100)
        yr = random.randint(1, 100)
        whi(f"the_bar_xy{ii}", f"{xr} {yr}")
def key_bins(key):
    power = float(AntiCheat.getthing("c", 3))
    cbg = rea("currentbackground")
    quitkey = "q"
    homekey = "z"
    restkey = "r"
    cosmeticskey = "c"
    # forms
    trueformkey = "t"
    froms_move = "F"
    froms_no_move = "f"
    froms_reset = "h"
    # level type
    ran_level = "0"
    if key == quitkey:
        with open(os.path.join("variables", "kill"), "w") as nf:
            nf.write("1")
        time.sleep(0.2)
        print("Unlinking ram")
        cla()
        time.sleep(0.2)
        exit(0)
    if key == homekey:
        if cbg == "level.bmp":
            whi("the_bar_xy-6", "-10 90")
            whi("the_bar_xy-7", "-10 90")
            whi("the_bar_xy-8", "-10 90")
            whi("the_bar_xy-9", "-10 90")
            whi("the_bar_xy-10", "-10 90")
            whi("the_bar_ps-6", "p1.bmp")
            whi("the_bar_ps-7", "p1.bmp")
            whi("the_bar_ps-8", "p1.bmp")
            whi("the_bar_ps-9", "p1.bmp")
            whi("the_bar_ps-10", "p1.bmp")

            whi("the_bar_xy-11", "-10 90")
            whi("the_bar_xy-12", "-10 90")
            whi("the_bar_xy-13", "-10 90")
            whi("the_bar_xy-14", "-10 90")
            whi("the_bar_xy-15", "-10 90")
            whi("the_bar_ps-11", "d1.bmp")
            whi("the_bar_ps-12", "d1.bmp")
            whi("the_bar_ps-13", "d1.bmp")
            whi("the_bar_ps-14", "d1.bmp")
            whi("the_bar_ps-15", "d1.bmp")
        whi("currentbackground", "lv1.bmp")
        whi("the_bar_xy0", "1 90")
    if key == restkey and power > 1:
        whi("the_bar_xy0", "1 90")
        if cbg == "level.bmp":
            level()
    if key == cosmeticskey and power > 100:
        ps0 = rea("the_bar_ps0")
        if ps0 == "bob0.bmp":
            ps = "bob0c1.bmp"
        if ps0 == "bob0c1.bmp":
            ps = "bob0c2.bmp"
        if ps0 == "bob0c2.bmp":
            ps = "bob0c3.bmp"
        if ps0 == "bob0c3.bmp":
            ps = "bob0c4.bmp"
        if ps0 == "bob0c4.bmp":
            ps = "bob0c5.bmp"
        if ps0 == "bob0c5.bmp":
            ps = "bob0c6.bmp"
        if ps0 == "bob0c6.bmp":
            ps = "bob0c7.bmp"
        if ps0 == "bob0c7.bmp":
            ps = "bob0c8.bmp"
        if ps0 == "bob0c8.bmp":
            ps = "bob0.bmp"
        whi("the_bar_ps0", ps)
    if key == trueformkey and power > 10000:
        with open(os.path.join("variables", "equipped_cosmetic"), "r") as a:
            ec = a.read()
        if ec == "1":
            with open(os.path.join("variables", "equipped_cosmetic"), "w") as a:
                a.write(f"0")
        else:
            with open(os.path.join("variables", "equipped_cosmetic"), "w") as a:
                a.write(f"1")
            threading.Thread(target=tf).start()
    if key == froms_move and power > 4000:
        cbg = rea("currentbackground")
        parts = rea(f"the_bar_xy0").split(" ")
        x, y = int(parts[0]), int(parts[1])
        fm = rea("fm")
        if int(fm) < -2:
            fm = "-1"
            whi(f"the_bar_xy{fm}", f"{x} {y}")
            whi(f"the_bar_cbg{fm}", cbg)
            fm = int(fm) - 1
        else:
            whi(f"the_bar_xy{fm}", f"{x} {y}")
            whi(f"the_bar_cbg{fm}", cbg)
            fm = int(fm) - 1
        whi("fm", str(fm))
    if key == froms_no_move and power > 1000:
        cbg = rea("currentbackground")
        parts = rea(f"the_bar_xy0").split(" ")
        x, y = int(parts[0]), int(parts[1])
        fn = rea("fn")
        if int(fn) < -5:
            fn = "-3"
            whi(f"the_bar_xy{fn}", f"{x} {y}")
            whi(f"the_bar_cbg{fn}", cbg)
            fn = int(fn) - 1
        else:
            whi(f"the_bar_xy{fn}", f"{x} {y}")
            whi(f"the_bar_cbg{fn}", cbg)
            fn = int(fn) - 1
        whi("fn", str(fn))
    if key == froms_reset and power > 0:
        whi("the_bar_cbg-5", "FPloading.bmp")
        whi("the_bar_cbg-4", "FPloading.bmp")
        whi("the_bar_cbg-3", "FPloading.bmp")
        whi("the_bar_cbg-2", "FPloading.bmp")
        whi("the_bar_cbg-1", "FPloading.bmp")
        whi("the_bar_xy-5", "-10 90")
        whi("the_bar_xy-4", "-10 90")
        whi("the_bar_xy-3", "-10 90")
        whi("the_bar_xy-2", "-10 90")
        whi("the_bar_xy-1", "-10 90")
        whi("the_bar_ps-5", "form.bmp")
        whi("the_bar_ps-4", "form.bmp")
        whi("the_bar_ps-3", "form.bmp")
        whi("the_bar_ps-2", "form.bmp")
        whi("the_bar_ps-1", "form.bmp")
        whi("fm", "-1")
        whi("fn", "-3")
    if key == ran_level:
            whi("the_bar_xy0", "1 90")
            level()
def form_physics(x, y):
    if x < 1:
        x = 99
        y = y + 10
    if x > 99:
        x = 1
        y = y - 10
    if y > 90:
        y = 0
    if y < 0:
        y = 90
    return x, y
def physics(x, y, px, py):
    cbg = rea("currentbackground")
    yn = rea("physics_yn")
    if yn == "1":
        return x, y
    # up and down movements
    if x < 1:
        x = 99
        y = y + 10
    if x > 99:
        x = 1
        y = y - 10

    # level switching
    if y > 90:
        y = 0

        if cbg[:2] == "FP":
            y = 90
        if cbg == "lv1.bmp":
            whi("currentbackground", "lv0.bmp")
    if y < 0:
        y = 90
        if cbg == "lv0.bmp":
            whi("currentbackground", "lv1.bmp")
        if cbg == "lv1.bmp":
            whi("currentbackground", "FPlv2.bmp")
        if cbg == "FPlv5.bmp":
            whi("currentbackground", "FPloading.bmp")
            for s in range(1, 14):
                AntiCheat.points("c", "+", 3, 0.5)
            ran = random.randint(2, 5)
            whi("currentbackground", f"FPlv{ran}.bmp")
        if cbg[:2] == "FP":
            cbg = rea("currentbackground")
            while True:
                ran = random.randint(2, 5)
                if cbg != f"FPlv{ran}.bmp":
                    break
                else:
                    pass
            whi("currentbackground", f"FPlv{ran}.bmp")
        if cbg == "level.bmp":
            level()
    if cbg == "hall.bmp":
        x1, y1, x2, y2 = 98, 93, 90, 29
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        threading.Thread(target=willq1).start()
    if cbg == "lv0.bmp":
        x1, y1, x2, y2 = 98, 93, 91, 72
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        # threading.Thread(target=willq1).start()
                        y = 50
                        x = 1
                        whi("currentbackground", "hall.bmp")
        x1, y1, x2, y2 = 9, 98, 1, 87
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        whi("currentbackground", "palatium.bmp")
        x1, y1, x2, y2 = 98, 98, 90, 87
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        whi("currentbackground", "FPloading.bmp")
                        whi("the_bar_xy0", "1 1")
                        time.sleep(0.7)
                        power = float(AntiCheat.getthing("c", 3))
                        with open(os.path.join("variables", "kill"), "w") as nf:
                            nf.write("1")
                        time.sleep(0.5)
                        os.system("cls" if os.name == "nt" else "clear")
                        print("""
You have """ + str(power) + """ power.
p = power w = cash
Paths:
Path 1:                                                              | Path 2:
p1     :  You’re alive I guess                                       | c1      :  Choose somebody to take after
p10    :  r is unlocked                                              | c10     :  r is unlocked   
p100   :  Colors for your Bob :)                                     | c100    :  Colors for your Bob :)   
p500   :  Speed = 3|Palatium = 1                                     | c500    :  Speed = 3|Palatium = 1| get a sword  
p1000  :  Speed = 4|Palatium = 2|FormsNM = 1|Special = 1|Rank = Minor| c1000   :  Speed = 4|Palatium = 2| choose a weapon
p2000  :  Palatium = 3|FormsNM = 2                                   |
p3000  :  Palatium = 4|FormsNM = 3                                   |
p4000  :  Palatium = 5|FormsCM = 1                                   |
p5000  :  Palatium = 6|FormsCM = 2|Palace = 1                        |
p6000  :  Palatium = 7                                               |
p7000  :  Palatium = 8                                               |
p8000  :  Palatium = 9                                               |
p9000  :  Palatium = 10  TP = 1                                      |
p10000 :  Palatium = All!|TF|Special = 2|Rank = Major                |
p20000 :  Palace = 2                                                 |
p30000 :  TP = 2                                                     |
p40000 :  TP = 3                                                     |
p50000 :  Special = 3| Palace = 3                                    |
p60000 :  TP = 4                                                     |
p70000 :  TP = 5                                                     |
p80000    TP = 6                                                     |
p90000    TP = 7                                                     |
p100000   Special = 4|Palace = 4|Rank = Titan                        |
--------------------------------------------------------------------|-----------------------------------------
The key binds are:
z = Teleport home
r = Reset - Goes back to the start of the level
c = Switch cosmetics
Forms:
t = Activate your True Form    (all forms will be able to earn wealth eventually)
F = Summons Form moving forms
f = Summons non moving forms
h = clears forms

Press q to exit. """)
    if cbg == "lv1.bmp":
        x1, y1, x2, y2 = 95, 95, 88, 86
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = 94
                        y = 4
    if cbg == "FPlv2.bmp":
        # yellow box splitter
        x1, y1, x2, y2 = 92, 80, 2, 70
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = 50
                        y = 62
        # blue one
        x1, y1, x2, y2 = 25, 66, 2, 55
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = 90
                        y = 36
        # red one
        x1, y1, x2, y2 = 98, 66, 75, 55
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = 4
                        y = 45
        # very light blue one
        x1, y1, x2, y2 = 77, 30, 67, 19
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = 98
                        y = 1
        # Collision One
        x1, y1, x2, y2 = 76, 42, 68, 31
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = px
                        y = py
    if cbg == "FPlv3.bmp":
        # yellow box splitter
        x1, y1, x2, y2 = 97, 97, 82, 88
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = 50
                        y = 75
        # lite blue box
        x1, y1, x2, y2 = 70, 80, 60, 70
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = 16
                        y = 75
        # red box
        x1, y1, x2, y2 = 40, 80, 30, 70
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = 83
                        y = 75
        # green box
        x1, y1, x2, y2 = 99, 80, 94, 70
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = 51
                        y = 58
        # purple box
        x1, y1, x2, y2 = 5, 80, 0, 71
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = 50
                        y = 40
        # Gray box
        x1, y1, x2, y2 = 93, 64, 89, 51
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = 49
                        y = 93
        # Brown box
        x1, y1, x2, y2 = 10, 64, 6, 50
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = 9
                        y = 24
        # pink box
        x1, y1, x2, y2 = 97, 43, 93, 33
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = 9
                        y = 24
        # Collision One
        x1, y1, x2, y2 = 6, 44, 1, 33
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = px
                        y = py
    if cbg == "FPlv4.bmp":
        # FPlv4
        # orange box splitter
        x1, y1, x2, y2 = 98, 95, 1, 78
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = 50
                        y = 65
        # purple box
        x1, y1, x2, y2 = 69, 70, 58, 58
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = 50
                        y = 50
        # red box
        x1, y1, x2, y2 = 42, 70, 31, 58
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = 50
                        y = 38
        # yellow box
        x1, y1, x2, y2 = 99, 70, 96, 58
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = 7
                        y = 6
        # green box
        x1, y1, x2, y2 = 3, 70, 0, 58
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = 91
                        y = 5
        # lite blue
        x1, y1, x2, y2 = 68, 43, 63, 33
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = 83
                        y = 64
        # pink box
        x1, y1, x2, y2 = 25, 55, 20, 48
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = 16
                        y = 64
        # green box
        x1, y1, x2, y2 = 56, 13, 44, 1
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = px
                        y = py
    if cbg == "FPlv5.bmp":
        # FPlv5
        x1, y1, x2, y2 = 98, 98, 86, 85
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = 50
                        y = 75
        x1, y1, x2, y2 = 39, 78, 28, 65
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = 87
                        y = 38
        x1, y1, x2, y2 = 73, 79, 62, 65
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = 17
                        y = 38
        x1, y1, x2, y2 = 12, 32, 1, 22
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = 52
                        y = 26
        x1, y1, x2, y2 = 41, 32, 29, 19
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = 6
                        y = 5
        x1, y1, x2, y2 = 75, 32, 63, 19
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = 91
                        y = 5
        x1, y1, x2, y2 = 64, 60, 39, 36
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = px
                        y = py
        x1, y1, x2, y2 = 60, 17, 45, 1
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = px
                        y = py
    if cbg == "palatium.bmp":
        x1, y1, x2, y2 = 98, 38, 92, 26
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        whi("currentbackground", "throneroom.bmp")
    if cbg == "throneroom.bmp":
        pass
    if cbg == "levelC.bmp":
        x1, y1, x2, y2 = 95, 95, 88, 86
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        level()
        x1, y1, x2, y2 = 98, 84, 89, 72
        if x2 <= x:
            if x <= x1:
                if y2 <= y:
                    if y <= y1:
                        x = 94
                        y = 4
    if cbg == "level.bmp":
        for ii in range(-15, -5):
            xy = rea(f"the_bar_xy{ii}").split(" ")
            ps = rea(f"the_bar_ps{ii}")
            if ps == "p1.bmp" or ps == "p2.bmp" or ps == "p3.bmp" or ps == "p4.bmp" or ps == "p5.bmp":
                xo = int(xy[0])
                yo = int(xy[1])

                x2 = xo
                y2 = yo
                x1 = xo + 9
                y1 = yo + 11

                if x2 <= x:
                    if x <= x1:
                        if y2 <= y:
                            if y <= y1:
                                q = rea(f"the_bar_xy{ii - 5}").split(" ")
                                x = int(q[0])
                                y = int(q[1])



        # None
    return x, y
def log_arrow_keys():
    if os.name == 'nt':
        import msvcrt
        confirm_clear = 0
        while True:
            if msvcrt.kbhit():
                first = msvcrt.getch()
                if first == b'\xe0':
                    second = msvcrt.getch()
                    key = None
                    if second == b'H':
                        key = 'UP'
                    elif second == b'P':
                        key = 'DOWN'
                    elif second == b'K':
                        key = 'LEFT'
                    elif second == b'M':
                        key = 'RIGHT'

                    if key:
                        try:
                            parts = rea("the_bar_xy0").split(" ")
                            x, y = int(parts[0]), int(parts[1])
                            px = x
                            py = y
                            # player controls and speeds
                            cbg = rea("currentbackground")
                            if cbg == "lv0.bmp" or cbg == "palatium.bmp" or cbg == "throneroom.bmp" or cbg == "will.bmp" or cbg == "will1.bmp" or cbg == "hall.bmp" or cbg == "levelC.bmp":
                                if key == "UP":
                                    y -= 2
                                elif key == "DOWN":
                                    y += 2
                                elif key == "LEFT":
                                    x -= 2
                                elif key == "RIGHT":
                                    x += 2
                            else:
                                if key == "UP":
                                    y -= 0
                                elif key == "DOWN":
                                    y += 0
                                elif key == "LEFT":
                                    x -= 2
                                elif key == "RIGHT":
                                    x += 2
                            x, y = physics(x, y, px, py)
                            whi("the_bar_xy0", f"{x} {y}")
                        except:
                            whi("the_bar_xy0", f"1 1")

                elif first == b'\x1b':
                    break
                else:
                    keyy = first.decode()
                    key_bins(keyy)



    else:
        import termios
        import tty
        cconfirm_clear = 0
        tty_in_out = open('/dev/tty', 'rb+', buffering=0)
        fd = tty_in_out.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setcbreak(fd)
            while True:
                ch1 = tty_in_out.read(1).decode('utf-8')
                if ch1 == '\x1b':
                    ch2 = tty_in_out.read(1).decode('utf-8')
                    if ch2 == '[':
                        ch3 = tty_in_out.read(1).decode('utf-8')
                        key = None
                        if ch3 == 'A':
                            key = 'UP'
                        elif ch3 == 'B':
                            key = 'DOWN'
                        elif ch3 == 'D':
                            key = 'LEFT'
                        elif ch3 == 'C':
                            key = 'RIGHT'

                        if key:
                            try:
                                parts = rea("the_bar_xy0").split(" ")
                                x, y = int(parts[0]), int(parts[1])
                                px = x
                                py = y
                                # player controls and speeds
                                cbg = rea("currentbackground")
                                if cbg == "lv0.bmp" or cbg == "palatium.bmp" or cbg == "throneroom.bmp" or cbg == "will.bmp" or cbg == "will1.bmp" or cbg == "hall.bmp" or cbg == "levelC.bmp":
                                    if key == "UP":
                                        y -= 2
                                    elif key == "DOWN":
                                        y += 2
                                    elif key == "LEFT":
                                        x -= 2
                                    elif key == "RIGHT":
                                        x += 2
                                else:
                                    if key == "UP":
                                        y -= 0
                                    elif key == "DOWN":
                                        y += 0
                                    elif key == "LEFT":
                                        x -= 2
                                    elif key == "RIGHT":
                                        x += 2
                                x, y = physics(x, y, px, py)
                                whi("the_bar_xy0", f"{x} {y}")
                            except:
                                whi("the_bar_xy0", f"1 1")
                    else:
                        break
                elif ch1.isprintable():
                    keyy = ch1
                    key_bins(keyy)

        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
def Animation():
    cbg = rea("currentbackground")
    while True:
        forms()
        # Load background
        cbg = rea("currentbackground")
        while True:
            try:
                with open(os.path.join("thebar", str(cbg)), 'rb') as f:
                    bg_data = bytearray(f.read())
                break
            except:
                pass
        header_size = 54
        bg_header = bg_data[:header_size]
        bg_pixels = bg_data[header_size:]
        bg_width = int.from_bytes(bg_data[18:22], byteorder='little')
        bg_height = int.from_bytes(bg_data[22:26], byteorder='little')
        bg_pad = (4 - (bg_width * 3) % 4) % 4

        for i in range(-15, 12):  # bob1.bmp to bob10.bmp
            sprite_path = rea(f"the_bar_ps{i}")
            parts = rea(f"the_bar_xy{i}").split(" ")
            xx, yy = int(parts[0]), int(parts[1])
            if i < 0 and i >= -5:
                cbgg = rea(f"the_bar_cbg{i}")
                if cbg != cbgg:
                    xx = -10
                    yy = 90
            while True:
                try:
                    with open(os.path.join("thebar", str(sprite_path)), 'rb') as f:
                        sprite_data = bytearray(f.read())
                    break
                except:
                    pass
            sprite_pixels = sprite_data[header_size:]
            sp_width = int.from_bytes(sprite_data[18:22], byteorder='little')
            sp_height = int.from_bytes(sprite_data[22:26], byteorder='little')
            sp_pad = (4 - (sp_width * 3) % 4) % 4

            for y in range(sp_height):
                for x in range(sp_width):
                    sp_row_size = sp_width * 3 + sp_pad
                    sp_idx = (sp_height - 1 - y) * sp_row_size + x * 3
                    b, g, r = sprite_pixels[sp_idx:sp_idx + 3]

                    if (r, g, b) == (255, 0, 255):  # Transparent pixel
                        continue
                    dst_x = x + xx
                    dst_y = y + yy

                    if 0 <= dst_x < bg_width and 0 <= dst_y < bg_height:
                        bg_row_size = bg_width * 3 + bg_pad
                        bg_idx = (bg_height - 1 - dst_y) * bg_row_size + dst_x * 3
                        bg_pixels[bg_idx:bg_idx + 3] = bytes([b, g, r])

        # Save result
        with open("current_frame.bmp", 'wb') as f:
            f.write(bg_header + bg_pixels)

        with open(os.path.join("variables", "new_frame"), "w") as nf:
            nf.write("0")

        # Wait for frame update or exit
        while True:
            with open(os.path.join("variables", "kill"), "r") as nf:
                if nf.read().strip() == "1":
                    exit(0)
            with open(os.path.join("variables", "new_frame"), "r") as nf:
                if nf.read().strip() == "1":
                    break
def main():
    screenwriter.render("current_frame.bmp", False)
if __name__ == "__main__":
    whi("the_bar_xy-6", "-10 90")
    whi("the_bar_xy-7", "-10 90")
    whi("the_bar_xy-8", "-10 90")
    whi("the_bar_xy-9", "-10 90")
    whi("the_bar_xy-10", "-10 90")
    whi("the_bar_ps-6", "p1.bmp")
    whi("the_bar_ps-7", "p1.bmp")
    whi("the_bar_ps-8", "p1.bmp")
    whi("the_bar_ps-9", "p1.bmp")
    whi("the_bar_ps-10", "p1.bmp")

    whi("the_bar_xy-11", "-10 90")
    whi("the_bar_xy-12", "-10 90")
    whi("the_bar_xy-13", "-10 90")
    whi("the_bar_xy-14", "-10 90")
    whi("the_bar_xy-15", "-10 90")
    whi("the_bar_ps-11", "d1.bmp")
    whi("the_bar_ps-12", "d1.bmp")
    whi("the_bar_ps-13", "d1.bmp")
    whi("the_bar_ps-14", "d1.bmp")
    whi("the_bar_ps-15", "d1.bmp")


    whi("the_bar_cbg-5", "FPloading.bmp")
    whi("the_bar_cbg-4", "FPloading.bmp")
    whi("the_bar_cbg-3", "FPloading.bmp")
    whi("the_bar_cbg-2", "FPloading.bmp")
    whi("the_bar_cbg-1", "FPloading.bmp")
    whi("the_bar_xy-5", "-10 90")
    whi("the_bar_xy-4", "-10 90")
    whi("the_bar_xy-3", "-10 90")
    whi("the_bar_xy-2", "-10 90")
    whi("the_bar_xy-1", "-10 90")
    whi("the_bar_xy0", "-10 90")
    whi("the_bar_xy1", "-10 90")
    whi("the_bar_xy2", "-10 90")
    whi("the_bar_xy3", "-10 90")
    whi("the_bar_xy4", "-10 90")
    whi("the_bar_xy5", "-10 90")
    whi("the_bar_xy6", "-10 90")
    whi("the_bar_xy7", "-10 90")
    whi("the_bar_xy8", "-10 90")
    whi("the_bar_xy9", "-10 90")
    whi("the_bar_xy10", "-10 90")
    whi("the_bar_xy11", "-10 90")
    whi("the_bar_xy12", "-10 90")
    whi("the_bar_ps-5", "form.bmp")
    whi("the_bar_ps-4", "form.bmp")
    whi("the_bar_ps-3", "form.bmp")
    whi("the_bar_ps-2", "form.bmp")
    whi("the_bar_ps-1", "form.bmp")
    whi("the_bar_ps0", "bob0.bmp")
    whi("the_bar_ps1", "hitbox.bmp")
    whi("the_bar_ps2", "bob1.bmp")
    whi("the_bar_ps3", "bob1.bmp")
    whi("the_bar_ps4", "bob1.bmp")
    whi("the_bar_ps5", "bob1.bmp")
    whi("the_bar_ps6", "bob1.bmp")
    whi("the_bar_ps7", "bob1.bmp")
    whi("the_bar_ps8", "bob1.bmp")
    whi("the_bar_ps9", "bob1.bmp")
    whi("the_bar_ps10", "bob1.bmp")
    whi("the_bar_ps11", "bob1.bmp")
    whi("the_bar_ps12", "bob1.bmp")
    whi("currentbackground", "lv1.bmp")
    whi("physics_yn", "0")
    whi("fm", "-1")
    whi("fn", "-3")
    a = input("""!Warning! This game is in alpha. Bugs and crashes are to be expected.
if you are new type "path" to pic a path
Press enter to continue...""")
    if a == "path":
        print("cooming soon")
        input()
    os.makedirs("variables", exist_ok=True)
    with open(os.path.join("variables", "kill"), "w") as nf:
        nf.write("0")
    processes = [
        multiprocessing.Process(target=Animation),
        multiprocessing.Process(target=main),
        multiprocessing.Process(target=log_arrow_keys)
        #multiprocessing.Process(target=sever)
    ]
    for p in processes:
        p.start()
