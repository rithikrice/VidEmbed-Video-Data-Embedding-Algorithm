import cv2
import sys
import numpy as np

def extract_data_from_video(video_path, num_bits):
    cap = cv2.VideoCapture(video_path)
    extracted_bits = ""
    block_size = 10  # Same block size as in embedding

    for _ in range(num_bits):
        ret, frame = cap.read()
        if not ret:
            break

        # Extract the 10x10 block
        block = frame[:block_size, :block_size, 0]

        # Calculate the average value of the block
        avg_value = np.mean(block)

        # Decide the bit based on the average value
        bit = '1' if avg_value > 127 else '0'  # Threshold at 127 for 8-bit images (0-255 range)
        extracted_bits += bit

    cap.release()
    return extracted_bits

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_data_from_video.py <video_path> <num_bits>")
        sys.exit(1)

    video_path = sys.argv[1]
    num_bits = int(sys.argv[2])

    data = extract_data_from_video(video_path, num_bits)
    print("Extracted data:", data)
