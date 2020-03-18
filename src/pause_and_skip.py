import cv2

# References:
# https://www.learnopencv.com/read-write-and-display-a-video-using-opencv-cpp-python/
# https://www.learnopencv.com/how-to-find-frame-rate-or-frames-per-second-fps-in-opencv-python-cpp/

def pause_and_skip(filename, outfile, skip_frames: int = 4):
    cap = cv2.VideoCapture(str(filename))
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    out = cv2.VideoWriter(
        str(outfile) + '.mp4',
        cv2.VideoWriter_fourcc(*'mp4v'),
        frame_rate,
        (frame_width, frame_height)
    )
    count = 0
    prev_frame = None
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        if prev_frame is None:
            prev_frame = frame

        if count % skip_frames == 0:
            prev_frame = frame

        out.write(prev_frame)
        count += 1

    cap.release()
    out.release()
