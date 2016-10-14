import numpy as np
import cv2
import sys

imagem_cinza = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)


def downsample(s, n):
    """Decrementa a taxa de amostragem pelo fator n. """
    return s[::n, ::n]


def upsample(s, n):
    """Aumenta a taxa de amostragem pelo fator n. """
    return np.repeat(np.repeat(s, n, axis=0), n, axis=1)


lena_ds = downsample(imagem_cinza, 2)
lena_us = upsample(lena_ds, 2)

cv2.imshow("original", imagem_cinza)
cv2.imshow("lena_ds", lena_ds)
cv2.imshow("lena_us", lena_us)

lena_ds = downsample(lena_us, 4)
lena_us = upsample(lena_ds, 4)

cv2.imshow("lena_ds4", lena_ds)
cv2.imshow("lena_us4", lena_us)


lena_ds = downsample(lena_us, 8)
lena_us = upsample(lena_ds, 8)

cv2.imshow("lena_ds8", lena_ds)
cv2.imshow("lena_us8", lena_us)
cv2.waitKey(0)
cv2.destroyAllWindows()
