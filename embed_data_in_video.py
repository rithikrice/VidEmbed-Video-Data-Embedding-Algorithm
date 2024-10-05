import cv2
import sys
import numpy as np

def embed_data(video_path, data, output_path):
    # Read the video
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    data_length = len(data)

    # Check for zero data length
    if data_length == 0:
        print("No data to embed.")
        return

    # Prepare to write the new video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, cap.get(cv2.CAP_PROP_FPS), 
                          (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), 
                           int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

    index = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Embed data into specific pixels
        for i in range(data_length):
            # Calculate the pixel position
            pixel_position = (i % int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                              i // int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) % int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

            # Check if pixel position is within the frame bounds
            if (0 <= pixel_position[0] < frame.shape[1] and
                0 <= pixel_position[1] < frame.shape[0]):
                
                # Embed bit
                bit = data[i]
                if bit == '1':
                    if frame[pixel_position[1], pixel_position[0], 0] < 255:
                        frame[pixel_position[1], pixel_position[0], 0] += 1  # Modify Red channel

        # Write the modified frame
        out.write(frame)

    cap.release()
    out.release()
    print("Data embedded successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 embed_data_in_video.py <video_path> <data> <output_path>")
        sys.exit(1)

    video_path = sys.argv[1]
    data = sys.argv[2]
    output_path = sys.argv[3]

    embed_data(video_path, data, output_path)
