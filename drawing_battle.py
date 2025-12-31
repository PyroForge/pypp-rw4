import os
import random
import sys
import multiprocessing
import screenwriter
# resets color
c = open(os.path.join("variables", "currentcolor"), "w")
c.write("1")
c.close()


def clear_screen():
    og = os.path.join("drawing_battle_frames", "ogbackground.bmp")
    plt = os.path.join("drawing_battle_frames", "background.bmp")
    xc = "xcopy " + og + " " + plt + "/Y"
    cp = "cp -f " + og + " " + plt
    os.system(xc if os.name == "nt" else cp)
def ColorChanger(colortoset):
    c = open(os.path.join("variables", "currentcolor"), "r")
    cu = int(c.read()) + 1
    c.close()
    if colortoset == 1:
        pass
    else:
        cu = int(colortoset)
    c = open(os.path.join("variables", "currentcolor"), "w")
    c.write(str(cu))
    c.close()
def ColorReader():
    c = open(os.path.join("variables", "currentcolor"), "r")
    cu = int(c.read())
    c.close()
    if cu > 9:
        cu = 1
    c = open(os.path.join("variables", "currentcolor"), "w")
    c.write(str(cu))
    c.close()
    if cu == 9:
        # aka rainbow mode
        cu = random.randint(1,8)
    if cu == 0:
        with open(os.path.join("drawing_battle_frames", "black.bmp"), 'rb') as f:
            sprite_data = bytearray(f.read())
    if cu == 1:
        with open(os.path.join("drawing_battle_frames", "red.bmp"), 'rb') as f:
            sprite_data = bytearray(f.read())
    if cu == 2:
        with open(os.path.join("drawing_battle_frames", "orange.bmp"), 'rb') as f:
            sprite_data = bytearray(f.read())
    if cu == 3:
        with open(os.path.join("drawing_battle_frames", "yellow.bmp"), 'rb') as f:
            sprite_data = bytearray(f.read())
    if cu == 4:
        with open(os.path.join("drawing_battle_frames", "green.bmp"), 'rb') as f:
            sprite_data = bytearray(f.read())
    if cu == 5:
        with open(os.path.join("drawing_battle_frames", "skyblue.bmp"), 'rb') as f:
            sprite_data = bytearray(f.read())
    if cu == 6:
        with open(os.path.join("drawing_battle_frames", "blue.bmp"), 'rb') as f:
            sprite_data = bytearray(f.read())
    if cu == 7:
        with open(os.path.join("drawing_battle_frames", "lavender.bmp"), 'rb') as f:
            sprite_data = bytearray(f.read())
    if cu == 8:
        with open(os.path.join("drawing_battle_frames", "white.bmp"), 'rb') as f:
            sprite_data = bytearray(f.read())
    return sprite_data
clear_screen()
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
                            with open(os.path.join("variables", "xy"), "r") as a:
                                parts = a.read().split(" ")
                                x, y = int(parts[0]), int(parts[1])
                            # player movements
                            if key == "UP":
                                y -= 5
                            elif key == "DOWN":
                                y += 5
                            elif key == "LEFT":
                                x -= 5
                            elif key == "RIGHT":
                                x += 5
                            with open(os.path.join("variables", "xy"), "w") as a:
                                a.write(f"{x} {y}")
                        except:
                            with open(os.path.join("variables", "xy"), "w") as a:
                                a.write("1 1")

                elif first == b'\x1b':
                    break
                else:
                    key = first.decode()
                    if key == "z":
                        if confirm_clear == 1:
                            clear_screen()
                            confirm_clear = 0
                        else:
                            confirm_clear = 1
                    if key == "x":
                        # turns on eraser
                        ColorChanger(0)
                    if key == " ":
                        # rotates color
                        ColorChanger(1)
                    if key == "q":
                        with open(os.path.join("variables", "kill"), "w") as nf:
                            nf.write("1")
                        exit(0)



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
                                with open(os.path.join("variables", "xy"), "r") as a:
                                    parts = a.read().split(" ")
                                    x, y = int(parts[0]), int(parts[1])
                                # player movements
                                if key == "UP":
                                    y -= 5
                                elif key == "DOWN":
                                    y += 5
                                elif key == "LEFT":
                                    x -= 5
                                elif key == "RIGHT":
                                    x += 5
                                with open(os.path.join("variables", "xy"), "w") as a:
                                    a.write(f"{x} {y}")
                            except:
                                with open(os.path.join("variables", "xy"), "w") as a:
                                    a.write("1 1")
                    else:
                        break
                elif ch1.isprintable():
                    kkey = ch1
                    if kkey == "z":
                        if cconfirm_clear == 1:
                            clear_screen()
                            cconfirm_clear = 0
                        else:
                            cconfirm_clear = 1
                    if kkey == "x":
                        # turns on eraser
                        ColorChanger(0)
                    if kkey == " ":
                        # rotates color
                        ColorChanger(1)
                    if kkey == "q":
                        with open(os.path.join("variables", "kill"), "w") as nf:
                            nf.write("1")
                        exit(0)

        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
def Animation():
    while True:
        with open(os.path.join("drawing_battle_frames", "background.bmp"), 'rb') as f:
            bg_data = bytearray(f.read())
        sprite_data = ColorReader()
        # blending / merging Sprites
        header_size = 54
        bg_header = bg_data[:header_size]
        bg_pixels = bg_data[header_size:]
        sprite_pixels = sprite_data[header_size:]
        bg_width = int.from_bytes(bg_data[18:22], byteorder='little')
        bg_height = int.from_bytes(bg_data[22:26], byteorder='little')
        sp_width = int.from_bytes(sprite_data[18:22], byteorder='little')
        sp_height = int.from_bytes(sprite_data[22:26], byteorder='little')
        bg_pad = (4 - (bg_width * 3) % 4) % 4
        sp_pad = (4 - (sp_width * 3) % 4) % 4
        for y in range(sp_height):
            for x in range(sp_width):
                row_size = sp_width * 3 + sp_pad
                sp_idx = (sp_height - 1 - y) * row_size + x * 3
                b, g, r = sprite_pixels[sp_idx:sp_idx + 3]
                if (r, g, b) == (255, 0, 255):
                    continue
                try:
                    with open(os.path.join("variables", "xy"), "r") as a:
                        parts = a.read().split(" ")
                        xx, yy = int(parts[0]), int(parts[1])
                        # frame by frame XY manipulation here
                except:
                    xx, yy = 0, 0
                # more blending stuff
                dst_x, dst_y = xx + x, yy + y
                if 0 <= dst_x < bg_width and 0 <= dst_y < bg_height:
                    row_size = bg_width * 3 + bg_pad
                    bg_idx = (bg_height - 1 - dst_y) * row_size + dst_x * 3
                    bg_pixels[bg_idx:bg_idx + 3] = bytes([b, g, r])
        with open(os.path.join("drawing_battle_frames", "background.bmp"), 'wb') as f:
            f.write(bg_header + bg_pixels)
        with open(os.path.join("variables", "new_frame"), "w") as nf:
            nf.write("0")
        while True:
            with open(os.path.join("variables", "kill"), "r") as nf:
                if nf.read() == "1":
                    exit(0)
            with open(os.path.join("variables", "new_frame"), "r") as nf:
                if nf.read() == "1":
                    break
def main():
    screenwriter.render(os.path.join("drawing_battle_frames", "background.bmp"), False)
if __name__ == "__main__":





    os.makedirs("variables", exist_ok=True)
    with open(os.path.join("variables", "xy"), "w") as a:
        a.write("1 1")
    with open(os.path.join("variables", "kill"), "w") as nf:
        nf.write("0")
    processes = [
        multiprocessing.Process(target=Animation),
        multiprocessing.Process(target=main),
        multiprocessing.Process(target=log_arrow_keys)
    ]
    for p in processes:
        p.start()
