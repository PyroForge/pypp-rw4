import time
import threading
import os
import AntiCheat
import screenwriter
def getafkcoin():
    while True:
        time.sleep(120)
        AntiCheat.points("c", "+", 2, 120)
def afkAnimation():
    folder = 'afk_frames'
    output_image_path = 'current_frame.bmp'
    frame_files = sorted(f for f in os.listdir(folder) if f.endswith('.bmp'))
    while True:
        for frame_count, frame_file in enumerate(frame_files):
            frame_path = os.path.join(folder, frame_file)
            with open(frame_path, 'rb') as src, open(output_image_path, 'wb') as dst:
                dst.write(src.read())
            nf = open(os.path.join("variables", "new_frame"), "w")
            nf.write("0")
            nf.close()
            while True:
                nf = open(os.path.join("variables", "new_frame"), "r")
                i = nf.read()
                nf.close()
                if i == "1":
                    break
def screen_logo_t():
    screenwriter.render("current_frame.bmp", False)
threading.Thread(target=getafkcoin).start()
threading.Thread(target=afkAnimation).start()
threading.Thread(target=screen_logo_t).start()
x = 0
while True:
    time.sleep(1)
    x = x + 1
    #print("You got one afk coin! (" + str(x) + ") this session")