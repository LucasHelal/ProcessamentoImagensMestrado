import numpy as np
import cv2
import sys

imagem_rgb = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)
k_cores = 16

def ChromaSample(banda, valor):
    bloco = np.uint8(180 / valor)
    quantizado = np.uint8(banda / bloco)
    banda = np.uint8((quantizado * bloco) + bloco / 2)

    return banda

img_HSV = cv2.cvtColor(imagem_rgb, cv2.COLOR_BGR2HSV)

hue = img_HSV[:, :, 0]
saturation = img_HSV[:, :, 1]

img_HSV[:, :, 0] = ChromaSample(hue, k_cores)
img_HSV[:, :, 1] = ChromaSample(saturation, k_cores)

img_final = cv2.cvtColor(img_HSV, cv2.COLOR_HSV2BGR)

cv2.imshow("Original e Final", np.hstack([imagem_rgb, img_final]))
cv2.imwrite("final-k=16.png ", np.hstack([imagem_rgb, img_final]))
cv2.waitKey(0)
cv2.destroyAllWindows()
