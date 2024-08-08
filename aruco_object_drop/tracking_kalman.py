import numpy as np

dt = 0.01

x = np.asarray([[x_pos],
                [y_pos],
                [z_pos],
                [0],
                [0],
                [0]])


A = np.asarray([[1,  0,  0,  dt,  0,  0],
                [0,  1,  0,  0,  dt,  0],
                [0,  0,  1,  0,  0,  dt],
                [0,  0,  0,  1,  0,   0]
                [0,  0,  0,  0,  1,   0]
                [0,  0,  0,  0,  0,   1]])

H = np.asarray([[1,  0, 0 ,0, 0, 0], # It's actually the C matrix
                [0,  1, 0 ,0, 0, 0]
                [0,  0, 1 ,0, 0, 0]] )


print('A',A)
print('H',H)

K0 = 1e5
Kp = 1
Kv = 0.0001
Kpv = 0
Km = 1e5

Q = np.asarray([[Kp, 0, 0, Kpv, 0, 0],
                [0, Kp, 0, 0, Kpv, 0]
                [0, 0, Kp, 0, 0, Kpv],
                [Kpv, 0, 0, Kp, 0, 0],
                [0, Kpv, 0, 0, Kp, 0],
                [0, 0, Kpv, 0, 0, Kp]])
R = np.asarray([[Km],[Km],[Km]])
P = np.asarray([[K0, 0, 0, 0, 0, 0],
                [0, K0, 0, 0, 0, 0],
                [0, 0, K0, 0, 0, 0],
                [0, 0, 0, K0, 0, 0]
                [0, 0, 0, 0, K0, 0]
                [0, 0, 0, 0, 0, K0]])

print('P', P)
print('Q', Q)
print('R', R)


x = np.asarray([[0],
                [0],
                [0],
                [0],
                [0],
                [0]])

