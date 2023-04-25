import cv2
import numpy as np

bin_data = open('pilkit.jpeg', 'rb').read()
file_size = len(bin_data)
pic1 = np.zeros((720, 1280))

x, y = 0, 0

for i in range(file_size):
    byte_data = bin_data[i]
    bits_string = bin(byte_data)[2:]
    if len(bits_string) < 8:
        bits_string = '0'*(8-len(bits_string)) + bits_string
    for j in range(8):
        pic1[x][y] = int(bits_string[j])*255
        y += 1
    if y == 1280:
        x += 1
        y = 0

cv2.imwrite('encoded.png', pic1)