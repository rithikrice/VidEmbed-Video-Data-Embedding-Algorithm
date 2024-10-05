import cv2
import sys

def extract_data(video_path, data_length):
    # Read the video
    cap = cv2.VideoCapture(video_path)
    extracted_data = []

    # Ensure that data_length is positive
    if data_length <= 0:
        print("Data length must be greater than zero.")
        return ""

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Ensure frame count is not zero
    if frame_count == 0:
        print("The video has no frames.")
        return ""

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Extract data from specific pixels
        for i in range(data_length):
            # Calculate pixel position
            pixel_position = (i % int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                              i // int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) % int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

            # Check if pixel position is within the frame bounds
            if (0 <= pixel_position[0] < frame.shape[1] and
                0 <= pixel_position[1] < frame.shape[0]):
                
                # Check bit
                bit = frame[pixel_position[1], pixel_position[0], 0] % 2
                extracted_data.append(str(bit))

                # Stop extracting if we reach the desired data_length
                if len(extracted_data) == data_length:
                    break

        # Break the outer loop if the desired length is reached
        if len(extracted_data) == data_length:
            break

    cap.release()
    return ''.join(extracted_data)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_data_from_video.py <video_path> <data_length>")
        sys.exit(1)

    video_path = sys.argv[1]
    data_length = int(sys.argv[2])

    extracted_data = extract_data(video_path, data_length)
    print("Extracted data:", extracted_data)
