from picamera2 import Picamera2
import cv2
from datetime import datetime
import os


def SaveImage(frame):
    # Save images in the pictures directory using the local time as a marker
    save_dir = '/home/imav/IMAV/photos'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    local_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = os.path.join(save_dir, 'imgcapture_{}.jpg'.format(local_time))
    print(f"saving {filename}")
    cv2.imwrite(filename, frame)


picam2 = Picamera2()
config = picam2.create_still_configuration(main={"size": (1920, 1080)})
picam2.configure(config)
picam2.start()

while True:
    image_array = picam2.capture_array()
    image_array_rgb = cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)

    key = input("Press 'q' to quit or ' ' (space) to save the image: ")

    if key == 'q':
        break
    elif key == '':
        SaveImage(image_array_rgb)

