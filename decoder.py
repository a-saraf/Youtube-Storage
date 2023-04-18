import cv2
import numpy as np

encoded = np.asarray(cv2.imread('encoded.png'))[:, :, 0]
bits_string = bytearray()

file_cap = 503608
complete = 0

for i in range(720):
    for j in range(160):
        data = encoded[i][j*8:j*8+8]
        byte1 = ''
        for x in data:
            byte1 += str(x//255)
        bits_string.append(int(byte1, 2) & 0xff)
        if(i*720 + j*8 == file_cap-1):
            complete = 1
        if complete:
            break
    if complete:
        break

file1 = open('output.jpeg', 'wb')
file1.write(bits_string)
file1.close()