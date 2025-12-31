import hashlib
def verify():
    sa = open("save.txt", "r")
    rl = sa.readlines()
    count = 0
    h = "0"
    # test 1 linking
    for line in rl:
        line = line.strip()
        if count % 2 == 0:
            h = hashlib.sha3_512(line.encode()).hexdigest()
        else:
            if h.strip() == line.strip():
                print(h.strip() + " " + line.strip() + " is linked")
            else:
                print("Good try, but I'm afraid that's not going to work. (linking failed)")
                return False
        count += 1
    # test 2 difficulty
    count = 0
    parts = rl[2].split("  ")
    difficulty = parts[3]
    difficulty = len(difficulty)
    for line in rl:
        if count > 2 and count % 2 != 0:
            t = "00000000000000000000000000000000000000000000000000000000000000000000"
            if line[:int(difficulty)] == t[:int(difficulty)]:
                print("got " + str(difficulty) + " for difficulty")
            else:
                print("You have to at least mine something... (difficulty test came back negative)")
                return False
        count += 1
    # test 3 suspicious activity
    count = -1
    for line in rl:
        if count >= 0:
            try:
                parts = line.split("  ")
                time_value = parts[0]
                name = parts[1]
                previous_hash = parts[2]
                difficulty = parts[3]
                target = parts[4]
                answer = parts[5]
                c = parts[6:6 + 40]
                v = parts[6 + 40:6 + 40 + 80]
                s = parts[6 + 40 + 80:6 + 40 + 80 + 80]

                I2parts = rl[count - 1].split("  ")
                I2time_value = I2parts[0]
                I2name = I2parts[1]
                I2previous_hash = I2parts[2]
                I2difficulty = I2parts[3]
                I2target = I2parts[4]
                I2answer = I2parts[5]
                I2c = I2parts[6:6 + 40]
                I2v = I2parts[6 + 40:6 + 40 + 80]
                I2s = I2parts[6 + 40 + 80:6 + 40 + 80 + 80]

                I3parts = rl[count - 3].split("  ")
                I3time_value = I3parts[0]
                I3name = I3parts[1]
                I3previous_hash = I3parts[2]
                I3difficulty = I3parts[3]
                I3target = I3parts[4]
                I3answer = I3parts[5]
                I3c = I3parts[6:6 + 40]
                I3v = I3parts[6 + 40:6 + 40 + 80]
                I3s = I3parts[6 + 40 + 80:6 + 40 + 80 + 80]
                # AFK
                timed = abs(float(time_value) - float(I2time_value))
                cd = float(c[1]) - float(I2c[1])
                if cd > 0:
                    cd = abs(cd)
                if cd == 0 or timed == 0:
                    pass
                else:
                    afk = cd / timed
                    if afk > 1:
                        print("Time doesn't go that fast... (afk rate test came back negative)")
                        return False
                # shop
                first1 = True
                cc = 0
                while True:
                    cc = cc + 1
                    s[cc] = s[cc].strip()
                    if first1:
                        oldx = s[cc]
                        first1 = False
                    if s[cc] != "0":
                        if s[cc] > oldx:
                            down = float(c[1]) - float(I3c[1])
                            s3 = float(s[cc]) - float(I3s[cc])
                            if down > 9998:
                                print("Nice try :) (stock payment test came back negative)")
                                return False
                            if c[1] == I3c[1]:
                                print("Uhh... You didn't pay? (stock payment test came back negative)")
                                return False
                            if s3 > 1:
                                print("At least you tried :) (stock payment test came back negative)")
                                return False
                    if cc > 79:
                        break
                    oldx = s[cc]


            except Exception as e:
                pass
                #print("An error occurred:", e)
        count = count + 1
    return True
while True:
    print(verify())
    a = input()
    if a != "":
        break