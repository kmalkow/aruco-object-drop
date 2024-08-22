import cv2
import time

def main():
    # Open the video capture with the specified device and backend
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    if not cap.isOpened():
        raise ValueError("Failed to open camera")
    
    # Set the resolution you want
    desired_width = 1920  # Example: 1920 pixels wide
    desired_height = 1080  # Example: 1080 pixels tall

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, desired_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, desired_height)

    # Check if the settings were applied
    actual_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    actual_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print(f"Camera resolution set to: {int(actual_width)}x{int(actual_height)}")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        
        cv2.imshow('frame', frame)

        # Print the resolution of the captured frame
        print(f"Captured frame resolution: {frame.shape[1]}x{frame.shape[0]}")

        time.sleep(0.1)

    cap.release()

if __name__ == "__main__":
    main()
