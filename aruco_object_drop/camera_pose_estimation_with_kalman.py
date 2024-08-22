import numpy as np
import cv2
import os
import time
from datetime import datetime
import tracking_kalman


def SaveImage(frame):
    # Save images in the pictures directory using the local time as a marker
    save_dir = '/home/orangepi/Pictures/ImageCaptures'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    local_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = os.path.join(save_dir, 'imgcapture_{}.jpg'.format(local_time))
    print(f"saving {filename}")
    cv2.imwrite(filename, frame)

# The different ArUco dictionaries built into the OpenCV library.
ARUCO_DICT = {
    "DICT_4X4_50": cv2.aruco.DICT_4X4_50,
    "DICT_4X4_100": cv2.aruco.DICT_4X4_100,
    "DICT_4X4_250": cv2.aruco.DICT_4X4_250,
    "DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
    "DICT_5X5_50": cv2.aruco.DICT_5X5_50,
    "DICT_5X5_100": cv2.aruco.DICT_5X5_100,
    "DICT_5X5_250": cv2.aruco.DICT_5X5_250,
    "DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
    "DICT_6X6_50": cv2.aruco.DICT_6X6_50,
    "DICT_6X6_100": cv2.aruco.DICT_6X6_100,
    "DICT_6X6_250": cv2.aruco.DICT_6X6_250,
    "DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
    "DICT_7X7_50": cv2.aruco.DICT_7X7_50,
    "DICT_7X7_100": cv2.aruco.DICT_7X7_100,
    "DICT_7X7_250": cv2.aruco.DICT_7X7_250,
    "DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
    "DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL
}

def load_cam_para():
    cv_file = cv2.FileStorage(pathLoad, cv2.FILE_STORAGE_READ)
    camera_Matrix = cv_file.getNode("cM").mat()
    distortion_Coeff = cv_file.getNode("dist").mat()
    cv_file.release()
    return camera_Matrix, distortion_Coeff

def main():
    # Define global variables for Kalman
    global previous_time
    global x
    global P
    global pixel_w
    global pixel_h

    # Check that we have a valid ArUco marker
    if ARUCO_DICT.get(desired_aruco_dictionary, None) is None:
        print(f"[INFO] ArUCo tag of '{desired_aruco_dictionary}' is not supported")
        os.sys.exit(0)
    
    # Load the ArUco dictionary
    print(f"[INFO] detecting '{desired_aruco_dictionary}' markers...")
    this_aruco_dictionary = cv2.aruco.getPredefinedDictionary(ARUCO_DICT[desired_aruco_dictionary])
    this_aruco_parameters = cv2.aruco.DetectorParameters()

    cap = cv2.VideoCapture(usb_num, cv2.CAP_DSHOW)
    # Set input resolution to 1920x1440 for Mapir
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, pixel_w)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, pixel_h)

    XYZ_ARUCO_cam_ref = []

    detection_counter = 0

    while True:
        # Set refresh rate
        #time.sleep(0.05)

        # Capture frame-by-frame
        ret, frame = cap.read()
        if frame.shape[0] != pixel_h or frame.shape[1] != pixel_w:
            print(frame.shape)
            raise ValueError(f'Input and requested frame dims do not agree!')

        # Detect ArUco markers in the video frame
        (corners, ids, rejected) = cv2.aruco.detectMarkers(frame, this_aruco_dictionary, parameters=this_aruco_parameters)

        # Check that at least one ArUco marker was detected
        if len(corners) > 0:
            # Flatten the ArUco IDs list
            ids = ids.flatten()

            # Loop over the detected ArUco corners
            for (marker_corner, marker_id) in zip(corners, ids):
                # Identify the desired marker
                if marker_id == Marker_id_truth:
                    # Extract the marker corners
                    marker_corner_reshaped = marker_corner.reshape((4, 2))
                    (top_left, top_right, bottom_right, bottom_left) = marker_corner_reshaped
                    
                    # Convert the (x,y) coordinate pairs to integers
                    top_right = (int(top_right[0]), int(top_right[1]))
                    bottom_right = (int(bottom_right[0]), int(bottom_right[1]))
                    bottom_left = (int(bottom_left[0]), int(bottom_left[1]))
                    top_left = (int(top_left[0]), int(top_left[1]))
                    
                    # Draw the bounding box of the ArUco detection
                    cv2.line(frame, top_left, top_right, (0, 255, 0), 2)
                    cv2.line(frame, top_right, bottom_right, (0, 255, 0), 2)
                    cv2.line(frame, bottom_right, bottom_left, (0, 255, 0), 2)
                    cv2.line(frame, bottom_left, top_left, (0, 255, 0), 2)
                    
                    # Calculate and draw the center of the ArUco marker
                    center_x = int((top_left[0] + bottom_right[0]) / 2.0)
                    center_y = int((top_left[1] + bottom_right[1]) / 2.0)
                    cv2.circle(frame, (center_x, center_y), 4, (0, 0, 255), -1)
                    
                    # Draw the ArUco marker ID on the video frame
                    # The ID is always located at the top_left of the ArUco marker
                    #cv2.putText(frame, 'ID: '+ str(marker_id), (top_left[0], top_left[1] - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                    # Get rotation and translation of the marker in the camera Frame
                    rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(marker_corner, MARKER_SIZE, camera_Matrix, distortion_Coeff)
                    X_ARUCO = tvec[0][0][0]
                    Y_ARUCO = tvec[0][0][1]
                    Z_ARUCO = tvec[0][0][2]
                    XYZ_ARUCO_cam_ref.append((X_ARUCO, Y_ARUCO, Z_ARUCO))

                    # Calculate rotation matrix from rotation vector
                    Rot_mat_marker_in_cam, _ = cv2.Rodrigues(np.array(rvec[0][0]))
                    Rot_mat_cam_in_marker = np.transpose(Rot_mat_marker_in_cam)
                    new_XYZ = np.dot(Rot_mat_cam_in_marker, np.array((X_ARUCO, Y_ARUCO, Z_ARUCO)).T)
                    
                    # Initialize Kalman filter on the first detection
                    if detection_counter == 0:
                        bool_initialize = True
                        previous_time = None
                        x = None
                        P = None
                    else:
                        bool_initialize = False

                    # Apply tracking Kalman
                    x, P, previous_time, dt = tracking_kalman.tracking_KF(new_XYZ, bool_initialize, previous_time, x, P)
                    new_XYZ = x.T[0:3]
                    detection_counter = detection_counter + 1

                    # Draw the ArUco offset on the video frame
                    cv2.putText(frame, str((round(new_XYZ[0],3), round(new_XYZ[1],3), round(new_XYZ[2],3))), (top_right[0], top_right[1] - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    print(f"Aruco X/Y/Z: {new_XYZ}, dt={round(dt,3)}")


        # Display the resulting frame
        cv2.imshow('frame', frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        
        if key == ord(' '):
            SaveImage(frame)

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


# -------------------All parameters--------------------
MARKER_SIZE = 0.147 # meters
Marker_id_truth = 420
timestep = None
desired_aruco_dictionary = "DICT_5X5_1000"
pathLoad = 'cameraCalibration_random_480p.xml'
pixel_w = 640 # width
pixel_h = 480 # height
camera_Matrix, distortion_Coeff = load_cam_para()
usb_num = 1
# -------------------All parameters--------------------


# -------------------Run the code--------------------
if __name__ == '__main__':
    #print(__doc__)
    main()
# -------------------Run the code--------------------
