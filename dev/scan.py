import numpy as np
import cv2

BOX_SIZE = 42
image = cv2.imread('output.png', cv2.IMREAD_GRAYSCALE)
bitmap = np.zeros((13, 13))
for x in range(13):
    for y in range(13):
        x1, x2 = x * BOX_SIZE, (x+1) * BOX_SIZE
        y1, y2 = y * BOX_SIZE, (y+1) * BOX_SIZE
        crop_image = image[x1:x2, y1:y2]
        if np.sum(crop_image > 128) > 0.8 * crop_image.size:
            # white block
            bitmap[x][y]=0
        else:
            # black block
            bitmap[x][y]=1

print(bitmap[1:-1, 1:-1])
