import cv2


def extract_frames(filename, outfile, skip_frames: int=4):
    cap = cv2.VideoCapture(filename)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    out = cv2.VideoWriter(outfile + '.mp4',
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


if __name__ == "__main__":
    in_file = "sample.mp4"
    out_file = "sample_skipped"
    extract_frames(in_file, out_file)
