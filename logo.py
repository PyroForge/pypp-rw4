import os
def main():
    # decompose the video frame by frame and waits for a screenwriter to read it
    folder = 'logo_frames'
    output_image_path = 'current_frame.bmp'
    frame_files = sorted(f for f in os.listdir(folder) if f.endswith('.bmp'))
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
if __name__ == '__main__':
    main()