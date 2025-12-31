import time
import hashlib
import random
def new_account(name, password):
    previous_hash = "None"
    difficulty = "None"
    target = "None"
    answer = "None"
    c1 = "0"
    c2 = "0"
    c3 = "0"
    c4 = "0"
    c5 = "0"
    c6 = "0"
    c7 = "0"
    c8 = "0"
    c9 = "0"
    c10 = "0"
    c11 = "0"
    c12 = "0"
    c13 = "0"
    c14 = "0"
    c15 = "0"
    c16 = "0"
    c17 = "0"
    c18 = "0"
    c19 = "0"
    c20 = "0"
    c21 = "0"
    c22 = "0"
    c23 = "0"
    c24 = "0"
    c25 = "0"
    c26 = "0"
    c27 = "0"
    c28 = "0"
    c29 = "0"
    c30 = "0"
    c31 = "0"
    c32 = "0"
    c33 = "0"
    c34 = "0"
    c35 = "0"
    c36 = "0"
    c37 = "0"
    c38 = "0"
    c39 = "0"
    c40 = "0"
    v1 = "0"
    v2 = "0"
    v3 = "0"
    v4 = "0"
    v5 = "0"
    v6 = "0"
    v7 = "0"
    v8 = "0"
    v9 = "0"
    v10 = "0"
    v11 = "0"
    v12 = "0"
    v13 = "0"
    v14 = "0"
    v15 = "0"
    v16 = "0"
    v17 = "0"
    v18 = "0"
    v19 = "0"
    v20 = "0"
    v21 = "0"
    v22 = "0"
    v23 = "0"
    v24 = "0"
    v25 = "0"
    v26 = "0"
    v27 = "0"
    v28 = "0"
    v29 = "0"
    v30 = "0"
    v31 = "0"
    v32 = "0"
    v33 = "0"
    v34 = "0"
    v35 = "0"
    v36 = "0"
    v37 = "0"
    v38 = "0"
    v39 = "0"
    v40 = "0"
    v41 = "0"
    v42 = "0"
    v43 = "0"
    v44 = "0"
    v45 = "0"
    v46 = "0"
    v47 = "0"
    v48 = "0"
    v49 = "0"
    v50 = "0"
    v51 = "0"
    v52 = "0"
    v53 = "0"
    v54 = "0"
    v55 = "0"
    v56 = "0"
    v57 = "0"
    v58 = "0"
    v59 = "0"
    v60 = "0"
    v61 = "0"
    v62 = "0"
    v63 = "0"
    v64 = "0"
    v65 = "0"
    v66 = "0"
    v67 = "0"
    v68 = "0"
    v69 = "0"
    v70 = "0"
    v71 = "0"
    v72 = "0"
    v73 = "0"
    v74 = "0"
    v75 = "0"
    v76 = "0"
    v77 = "0"
    v78 = "0"
    v79 = "0"
    v80 = "0"
    s1 = "0"
    s2 = "0"
    s3 = "0"
    s4 = "0"
    s5 = "0"
    s6 = "0"
    s7 = "0"
    s8 = "0"
    s9 = "0"
    s10 = "0"
    s11 = "0"
    s12 = "0"
    s13 = "0"
    s14 = "0"
    s15 = "0"
    s16 = "0"
    s17 = "0"
    s18 = "0"
    s19 = "0"
    s20 = "0"
    s21 = "0"
    s22 = "0"
    s23 = "0"
    s24 = "0"
    s25 = "0"
    s26 = "0"
    s27 = "0"
    s28 = "0"
    s29 = "0"
    s30 = "0"
    s31 = "0"
    s32 = "0"
    s33 = "0"
    s34 = "0"
    s35 = "0"
    s36 = "0"
    s37 = "0"
    s38 = "0"
    s39 = "0"
    s40 = "0"
    s41 = "0"
    s42 = "0"
    s43 = "0"
    s44 = "0"
    s45 = "0"
    s46 = "0"
    s47 = "0"
    s48 = "0"
    s49 = "0"
    s50 = "0"
    s51 = "0"
    s52 = "0"
    s53 = "0"
    s54 = "0"
    s55 = "0"
    s56 = "0"
    s57 = "0"
    s58 = "0"
    s59 = "0"
    s60 = "0"
    s61 = "0"
    s62 = "0"
    s63 = "0"
    s64 = "0"
    s65 = "0"
    s66 = "0"
    s67 = "0"
    s68 = "0"
    s69 = "0"
    s70 = "0"
    s71 = "0"
    s72 = "0"
    s73 = "0"
    s74 = "0"
    s75 = "0"
    s76 = "0"
    s77 = "0"
    s78 = "0"
    s79 = "0"
    s80 = "0"
    o = "  "
    c = c1 + o + c2 + o + c3 + o + c4 + o + c5 + o + c6 + o + c7 + o + c8 + o + c9 + o + c10 + o + c11 + o + c12 + o + c13 + o + c14 + o + c15 + o + c16 + o + c17 + o + c18 + o + c19 + o + c20 + o + c21 + o + c22 + o + c23 + o + c24 + o + c25 + o + c26 + o + c27 + o + c28 + o + c29 + o + c30 + o + c31 + o + c32 + o + c33 + o + c34 + o + c35 + o + c36 + o + c37 + o + c38 + o + c39 + o + c40
    v = v1 + o + v2 + o + v3 + o + v4 + o + v5 + o + v6 + o + v7 + o + v8 + o + v9 + o + v10 + o + v11 + o + v12 + o + v13 + o + v14 + o + v15 + o + v16 + o + v17 + o + v18 + o + v19 + o + v20 + o + v21 + o + v22 + o + v23 + o + v24 + o + v25 + o + v26 + o + v27 + o + v28 + o + v29 + o + v30 + o + v31 + o + v32 + o + v33 + o + v34 + o + v35 + o + v36 + o + v37 + o + v38 + o + v39 + o + v40 + o + v41 + o + v42 + o + v43 + o + v44 + o + v45 + o + v46 + o + v47 + o + v48 + o + v49 + o + v50 + o + v51 + o + v52 + o + v53 + o + v54 + o + v55 + o + v56 + o + v57 + o + v58 + o + v59 + o + v60 + o + v61 + o + v62 + o + v63 + o + v64 + o + v65 + o + v66 + o + v67 + o + v68 + o + v69 + o + v70 + o + v71 + o + v72 + o + v73 + o + v74 + o + v75 + o + v76 + o + v77 + o + v78 + o + v79 + o + v80
    s = s1 + o + s2 + o + s3 + o + s4 + o + s5 + o + s6 + o + s7 + o + s8 + o + s9 + o + s10 + o + s11 + o + s12 + o + s13 + o + s14 + o + s15 + o + s16 + o + s17 + o + s18 + o + s19 + o + s20 + o + s21 + o + s22 + o + s23 + o + s24 + o + s25 + o + s26 + o + s27 + o + s28 + o + s29 + o + s30 + o + s31 + o + s32 + o + s33 + o + s34 + o + s35 + o + s36 + o + s37 + o + s38 + o + s39 + o + s40 + o + s41 + o + s42 + o + s43 + o + s44 + o + s45 + o + s46 + o + s47 + o + s48 + o + s49 + o + s50 + o + s51 + o + s52 + o + s53 + o + s54 + o + s55 + o + s56 + o + s57 + o + s58 + o + s59 + o + s60 + o + s61 + o + s62 + o + s63 + o + s64 + o + s65 + o + s66 + o + s67 + o + s68 + o + s69 + o + s70 + o + s71 + o + s72 + o + s73 + o + s74 + o + s75 + o + s76 + o + s77 + o + s78 + o + s79 + o + s80
    sa = open("save.txt", "w")
    data = str(time.time()) + o + name + o + previous_hash + o + difficulty + o + target + o + answer + o + c + o + v + o + s
    sa.write(data + "\n")
    sa.write(hashlib.sha3_512(data.encode()).hexdigest() + "\n")
    sa.close()
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
                pass
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
                pass
            else:
                print("You have to mine at least something... (difficulty test came back negative)")
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
def points(type, mode, id, amount):
    sa = open("save.txt", "r")
    rl = sa.readlines()
    sa.close()
    lasthash = rl[-1]
    lastlog = rl[-2]
    o = "  "
    parts = lastlog.split(o)
    time_value = parts[0]
    name = parts[1]
    previous_hash = parts[2]
    difficulty = parts[3]
    target = parts[4]
    answer = parts[5]
    c = parts[6:6 + 40]
    v = parts[6 + 40:6 + 40 + 80]
    s = parts[6 + 40 + 80:6 + 40 + 80 + 80]
    if type == "c":
        if mode == "o":
            c[int(id) - 1] = amount
        if mode == "+":
            c[int(id) - 1] = float(c[int(id) - 1]) + amount
        if mode == "-":
            c[int(id) - 1] = float(c[int(id) - 1]) - amount
    if type == "v":
        if mode == "o":
            v[int(id) - 1] = amount
        if mode == "+":
            v[int(id) - 1] = float(v[int(id) - 1]) + amount
        if mode == "-":
            v[int(id) - 1] = float(v[int(id) - 1]) - amount
    if type == "s":
        if mode == "o":
            s[int(id) - 1] = amount
        if mode == "+":
            s[int(id) - 1] = float(s[int(id) - 1]) + amount
        if mode == "-":
            s[int(id) - 1] = float(s[int(id) - 1]) - amount
    target = "10000"
    difficulty = "0000"
    answer = int(target)
    while True:
        answer = answer + 1
        newlog = str(time.time()) + o + name + o + lasthash.strip() + o + difficulty + o + target + o + str(answer) + o
        for x in c:
            newlog = newlog + str(x) + o
        for x in v:
            newlog = newlog + str(x) + o
        for x in s:
            newlog = newlog + str(x) + o
        h = (hashlib.sha3_512(newlog.strip().encode()).hexdigest())
        if h[:4] == difficulty:
            break
    sa = open("save.txt", "a")
    sa.write(newlog.strip() + "\n")
    sa.write(h + "\n")
    sa.close()
def getthing(type, id):
    sa = open("save.txt", "r")
    rl = sa.readlines()
    sa.close()
    lasthash = rl[-1]
    lastlog = rl[-2]
    o = "  "
    parts = lastlog.split(o)
    time_value = parts[0]
    name = parts[1]
    previous_hash = parts[2]
    difficulty = parts[3]
    target = parts[4]
    answer = parts[5]
    c = parts[6:6 + 40]
    v = parts[6 + 40:6 + 40 + 80]
    s = parts[6 + 40 + 80:6 + 40 + 80 + 80]
    if type == "c":
        a = str(c[int(id) - 1])
    if type == "v":
        a = str(v[int(id) - 1])
    if type == "s":
        a = str(s[int(id) - 1])
    return a