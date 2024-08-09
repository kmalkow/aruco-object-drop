import numpy as np
import time

K0 = 0.0001  # Initial state variance
Kp = 1  # Variance of position
Kv = 0.0001  # Variance of velocity
Kpv = 0  # Covariance
Km = 100  # Variance of measurement

def tracking_KF(xyz_observation, bool_initialize, previous_time, x, P):
    x_obs, y_obs, z_obs = xyz_observation

    # Initialize position and P matrix
    if bool_initialize:
        x = np.asarray([x_obs,
                        y_obs,
                        z_obs,
                        0,
                        0,
                        0]).T
        
        # Estimation covariance
        P = np.asarray([[K0, 0, 0, 0, 0, 0],
                        [0, K0, 0, 0, 0, 0],
                        [0, 0, K0, 0, 0, 0],
                        [0, 0, 0, 0, 0,  0],
                        [0, 0, 0, 0, 0,  0],
                        [0, 0, 0, 0, 0,  0]])
        
        previous_time = time.time()
        return x, P, previous_time

    # Calculate time step
    dt = time.time() - previous_time

    # Update the previous time
    previous_time = time.time()

    # A matrix
    A = np.asarray([[1,  0,  0,  dt,  0,  0],
                    [0,  1,  0,  0,  dt,  0],
                    [0,  0,  1,  0,  0,  dt],
                    [0,  0,  0,  1,  0,   0],
                    [0,  0,  0,  0,  1,   0],
                    [0,  0,  0,  0,  0,   1]])

    # H matrix (observation matrix)
    H = np.asarray([[1,  0, 0, 0, 0, 0],
                    [0,  1, 0, 0, 0, 0],
                    [0,  0, 1, 0, 0, 0]])

    # Process covariance
    Q = np.asarray([[Kp, 0, 0, Kpv, 0, 0],
                    [0, Kp, 0, 0, Kpv, 0],
                    [0, 0, Kp, 0, 0, Kpv],
                    [Kpv, 0, 0, Kv, 0, 0],
                    [0, Kpv, 0, 0, Kv, 0],
                    [0, 0, Kpv, 0, 0, Kv]])
    
    # Measurement covariance
    R = np.asarray([[Km, 0, 0],
                    [0, Km, 0],
                    [0, 0, Km]])

    # Predicted state estimate
    x = A @ x

    # Predicted estimate covariance
    P = ((A @ P) @ A.T) + Q

    # Observation
    zk = np.array([x_obs, y_obs, z_obs]).T

    # Innovation
    yk = zk - (H @ x)

    # Innovation covariance
    S = H @ P @ H.T + R
    S_inv = np.linalg.inv(S)

    # Kalman gain
    K = (P @ H.T) @ S_inv

    # Updated state estimate
    x = x + (K @ yk)

    # Updated estimate covariance
    P = (np.eye(6) - (K @ H)) @ P

    return x, P, previous_time
