import cv2
import sys

def embed_data(video_path, data, output_path):
    cap = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4
    out = cv2.VideoWriter(output_path, fourcc, cap.get(cv2.CAP_PROP_FPS),
                          (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    data_length = len(data)

    current_data_index = 0

    for _ in range(frame_count):
        ret, frame = cap.read()
        if not ret or current_data_index >= data_length:
            break

        # Embed one bit per frame in the top-left 10x10 block
        block_size = 10
        bit = data[current_data_index]

        # If bit is '0', set 10x10 block to 0, if '1', set it to 255
        value = 0 if bit == '0' else 255

        for dy in range(block_size):
            for dx in range(block_size):
                frame[dy, dx, 0] = value

        out.write(frame)
        current_data_index += 1

    cap.release()
    out.release()
    print("Data embedded successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python embed_data_in_video.py <video_path> <data> <output_path>")
        sys.exit(1)

    video_path = sys.argv[1]
    data = sys.argv[2]
    output_path = sys.argv[3]

    embed_data(video_path, data, output_path)
