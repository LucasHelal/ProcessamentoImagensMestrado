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


def salvar(imagem):
    abacate = [2, 4, 8, 16, 32, 64, 128, 256]
    lena_us = imagem
    for i in abacate:
        lena_ds = downsample(lena_us, i)
        # cv2.imwrite('lena_ds' + str(i) + '.png', lena_ds)
        lena_us = upsample(lena_ds, i)
        cv2.imwrite('lena_us' + str(i) + '.png', lena_us)


salvar(imagem_cinza)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
