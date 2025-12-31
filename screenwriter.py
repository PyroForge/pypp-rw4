import os #line:1
import sys #line:2
import time #line:3
from PIL import Image #line:4
ASCII_CHARS ="@%#*+=-:. "#line:5
def render (O0OOO00OO00O0OO00 ,use_ascii =False ):#line:6
    with open (os .path .join ("variables","kill"),"w")as OO0O0OO0O00OO0O00 :#line:7
        OO0O0OO0O00OO0O00 .write ("0")#line:8
    OOOO00O000O0OO0O0 =0 #line:9
    OO0O000OOO0O00O0O =None #line:10
    O0OOO0O000OO0O0OO ="\033"#line:11
    OOOOOOOO0O00OOOO0 =f"{O0OOO0O000OO0O0OO}["#line:12
    OO000O0OOOO0O0O0O =f"{O0OOO0O000OO0O0OO}[0m"#line:13
    os .system ("cls"if os .name =="nt"else "clear")#line:14
    while True :#line:15
        try :#line:16
            try :#line:17
                OOO0000OOOOO0OOO0 =os .path .getmtime (O0OOO00OO00O0OO00 )#line:18
                if OOO0000OOOOO0OOO0 !=OOOO00O000O0OO0O0 :#line:19
                    OOOO00O000O0OO0O0 =OOO0000OOOOO0OOO0 #line:20
                    OO0O000OOO0O00O0O =Image .open (O0OOO00OO00O0OO00 ).convert ("RGB")#line:21
            except Exception :#line:22
                continue #line:23
            if OO0O000OOO0O00O0O :#line:24
                O00O0O0O00OO0OO0O ,OOOOO0000OO0O0OO0 =os .get_terminal_size ()#line:25
                O00OO00OO0000O000 =O00O0O0O00OO0OO0O -1 #line:27
                OO000OO00O000O00O =OOOOO0000OO0O0OO0 -1 #line:28
                if use_ascii :#line:29
                    OOO000OO000O0OOO0 =OO0O000OOO0O00O0O .resize ((O00OO00OO0000O000 ,OO000OO00O000O00O ))#line:30
                    OOO0OO00O0O00O00O =OOO000OO000O0OOO0 .load ()#line:31
                    sys .stdout .flush ()#line:33
                    for OOOOOO0O0O00OOO00 in range (OO000OO00O000O00O ):#line:34
                        O0O0OO0OOO0O0OOOO =""#line:35
                        for OOO000O0OO00O00O0 in range (O00OO00OO0000O000 ):#line:36
                            OOOOOOO0OO000OO00 ,OO00O0OO000O0000O ,O00OO0OO00O0O0OO0 =OOO0OO00O0O00O00O [OOO000O0OO00O00O0 ,OOOOOO0O0O00OOO00 ]#line:37
                            O000OOOOOOOOO000O =0.299 *OOOOOOO0OO000OO00 +0.587 *OO00O0OO000O0000O +0.114 *O00OO0OO00O0O0OO0 #line:38
                            OOOO0O0O0OOOOO000 =int (O000OOOOOOOOO000O /255 *(len (ASCII_CHARS )-1 ))#line:39
                            O0O0OO0OOO0O0OOOO +=ASCII_CHARS [OOOO0O0O0OOOOO000 ]#line:40
                        print (O0O0OO0OOO0O0OOOO )#line:41
                else :#line:42
                    OOO000OO000O0OOO0 =OO0O000OOO0O00O0O .resize ((O00OO00OO0000O000 ,OO000OO00O000O00O *2 ))#line:43
                    OOO0OO00O0O00O00O =OOO000OO000O0OOO0 .load ()#line:44
                    sys .stdout .write (f"{OOOOOOOO0O00OOOO0}H")#line:45
                    sys .stdout .flush ()#line:46
                    for OOOOOO0O0O00OOO00 in range (0 ,OOO000OO000O0OOO0 .height -1 ,2 ):#line:47
                        O0O0OO0OOO0O0OOOO =""#line:48
                        for OOO000O0OO00O00O0 in range (OOO000OO000O0OOO0 .width ):#line:49
                            O0O00OO0OOOOO0O00 ,OO00O0O0OOO0O0OO0 ,OO0O00OOOO000OOOO =OOO0OO00O0O00O00O [OOO000O0OO00O00O0 ,OOOOOO0O0O00OOO00 ][:3 ]#line:50
                            O0OO0OOO0000OOO00 ,O0O0O00O000000O00 ,O0O00O0OO00000000 =OOO0OO00O0O00O00O [OOO000O0OO00O00O0 ,OOOOOO0O0O00OOO00 +1 ][:3 ]#line:51
                            O0O0OO0OOO0O0OOOO +=f"\033[38;2;{O0O00OO0OOOOO0O00};{OO00O0O0OOO0O0OO0};{OO0O00OOOO000OOOO}m\033[48;2;{O0OO0OOO0000OOO00};{O0O0O00O000000O00};{O0O00O0OO00000000}m▀"#line:52
                        O0O0OO0OOO0O0OOOO +=OO000O0OOOO0O0O0O #line:53
                        print (O0O0OO0OOO0O0OOOO )#line:54
            with open (os .path .join ("variables","new_frame"),"w")as OO0O0OO0O00OO0O00 :#line:55
                OO0O0OO0O00OO0O00 .write ("1")#line:56
            while True :#line:57
                with open (os .path .join ("variables","kill"),"r")as OO0O0OO0O00OO0O00 :#line:58
                    O0000O0OOO00O00O0 =OO0O0OO0O00OO0O00 .read ()#line:59
                with open (os .path .join ("variables","new_frame"),"r")as OO0O0OO0O00OO0O00 :#line:60
                    O0O0O0OOO000O0OO0 =OO0O0OO0O00OO0O00 .read ()#line:61
                if O0O0O0OOO000O0OO0 =="0":#line:62
                    break #line:63
                if O0000O0OOO00O00O0 =="1":#line:64
                    exit ()#line:65
                time .sleep (0.01 )#line:66
            time .sleep (0 )#line:68
        except KeyboardInterrupt :#line:69
            break #line:70
def menu (O0000000O00O0OOO0 ):#line:71
    import os #line:73
    import sys #line:74
    OOO00OOOOO0OOO0O0 =len (O0000000O00O0OOO0 )#line:75
    O000OOOO0O0OOOO00 =len (O0000000O00O0OOO0 [0 ])#line:76
    O000000OO00OOO00O ,OOO00OOO0OO00OO0O =0 ,0 #line:77
    if os .name =='nt':#line:78
        import msvcrt #line:79
    else :#line:80
        import tty #line:81
        import termios #line:82
    while True :#line:83
        os .system ("cls"if os .name =="nt"else "clear")#line:84
        for O0OO0O00O0O00OO00 in range (OOO00OOOOO0OOO0O0 ):#line:85
            for OO0OOO00O0O00000O in range (O000OOOO0O0OOOO00 ):#line:86
                OOOO0000OOOOO0O0O =O0000000O00O0OOO0 [O0OO0O00O0O00OO00 ][OO0OOO00O0O00000O ]#line:87
                if O0OO0O00O0O00OO00 ==O000000OO00OOO00O and OO0OOO00O0O00000O ==OOO00OOO0OO00OO0O :#line:88
                    print (f"[{OOOO0000OOOOO0O0O}]",end =' ')#line:89
                else :#line:90
                    print (f" {OOOO0000OOOOO0O0O} ",end =' ')#line:91
            print ()#line:92
        O0OO0O0OO0OO00OO0 =None #line:93
        if os .name =='nt':#line:94
            OOO0000O00OO0OOOO =msvcrt .getch ()#line:95
            if OOO0000O00OO0OOOO ==b'\xe0':#line:96
                OO0O000OO0O000O0O =msvcrt .getch ()#line:97
                if OO0O000OO0O000O0O ==b'H':#line:98
                    O000000OO00OOO00O =(O000000OO00OOO00O -1 )%OOO00OOOOO0OOO0O0 #line:99
                elif OO0O000OO0O000O0O ==b'P':#line:100
                    O000000OO00OOO00O =(O000000OO00OOO00O +1 )%OOO00OOOOO0OOO0O0 #line:101
                elif OO0O000OO0O000O0O ==b'K':#line:102
                    OOO00OOO0OO00OO0O =(OOO00OOO0OO00OO0O -1 )%O000OOOO0O0OOOO00 #line:103
                elif OO0O000OO0O000O0O ==b'M':#line:104
                    OOO00OOO0OO00OO0O =(OOO00OOO0OO00OO0O +1 )%O000OOOO0O0OOOO00 #line:105
            elif OOO0000O00OO0OOOO ==b'\r':#line:106
                O0OO0O0OO0OO00OO0 =O0000000O00O0OOO0 [O000000OO00OOO00O ][OOO00OOO0OO00OO0O ]#line:107
            elif OOO0000O00OO0OOOO ==b'q':#line:108
                break #line:109
        else :#line:110
            O0000OO000000O0O0 =sys .stdin .fileno ()#line:111
            OO0O00O0O0O000O0O =termios .tcgetattr (O0000OO000000O0O0 )#line:112
            try :#line:113
                tty .setraw (O0000OO000000O0O0 )#line:114
                OOOO000O0OOOOOO0O =sys .stdin .read (1 )#line:115
                if OOOO000O0OOOOOO0O =='q':#line:116
                    break #line:117
                elif OOOO000O0OOOOOO0O =='\r'or OOOO000O0OOOOOO0O =='\n':#line:118
                    O0OO0O0OO0OO00OO0 =O0000000O00O0OOO0 [O000000OO00OOO00O ][OOO00OOO0OO00OO0O ]#line:119
                elif OOOO000O0OOOOOO0O =='\x1b':#line:120
                    OO0O00OO0O0000OOO =sys .stdin .read (1 )#line:121
                    O00O00OO00OOOOOO0 =sys .stdin .read (1 )#line:122
                    if OO0O00OO0O0000OOO =='[':#line:123
                        if O00O00OO00OOOOOO0 =='A':#line:124
                            O000000OO00OOO00O =(O000000OO00OOO00O -1 )%OOO00OOOOO0OOO0O0 #line:125
                        elif O00O00OO00OOOOOO0 =='B':#line:126
                            O000000OO00OOO00O =(O000000OO00OOO00O +1 )%OOO00OOOOO0OOO0O0 #line:127
                        elif O00O00OO00OOOOOO0 =='D':#line:128
                            OOO00OOO0OO00OO0O =(OOO00OOO0OO00OO0O -1 )%O000OOOO0O0OOOO00 #line:129
                        elif O00O00OO00OOOOOO0 =='C':#line:130
                            OOO00OOO0OO00OO0O =(OOO00OOO0OO00OO0O +1 )%O000OOOO0O0OOOO00 #line:131
            finally :#line:132
                termios .tcsetattr (O0000OO000000O0O0 ,termios .TCSADRAIN ,OO0O00O0O0O000O0O )#line:133
        if O0OO0O0OO0OO00OO0 :#line:134
            if os .name =='nt':#line:135
                msvcrt .getch ()#line:136
            else :#line:137
                O0000OO000000O0O0 =sys .stdin .fileno ()#line:138
                OO0O00O0O0O000O0O =termios .tcgetattr (O0000OO000000O0O0 )#line:139
                try :#line:140
                    tty .setraw (O0000OO000000O0O0 )#line:141
                    sys .stdin .read (1 )#line:142
                finally :#line:143
                    termios .tcsetattr (O0000OO000000O0O0 ,termios .TCSADRAIN ,OO0O00O0O0O000O0O )#line:144
            return O0OO0O0OO0OO00OO0 