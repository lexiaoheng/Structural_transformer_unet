import glob
import os

import numpy as np
import cv2

path_img = r'./seismic_val/*.png'
path_save = r'./Synapse/test_vol_h5/'
for i, path in enumerate(glob.glob(path_img)):
    image = cv2.imread(path, flags=0)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    target_path = path.replace('seismic_val', 'fault_val')
    target = cv2.imread(target_path, flags=0)
    target[target != 255] = 0
    target[target == 255] = 1
    np.savez(path_save+str(i), image=image, label=target)
    print('-----------------', i)
print('ok')
