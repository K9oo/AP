import numpy as np

###################################################
img_cali = np.load('/home/pi/Desktop/Lee/AprilTag_tello/mtx,dist/real_cali_2.npz')

mtx = img_cali['m']
dist = img_cali['d']

mtx = np.array(mtx, dtype=np.float32)
dist = np.array(dist, dtype=np.float32)

img_cali.close()

####################################################
print("camera matrix: \n")
print(mtx)
print("dist: \n")
print(dist)