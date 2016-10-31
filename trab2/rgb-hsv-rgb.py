import numpy as np
import cv2
import sys

imagem_rgb = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)

img_HSV = cv2.cvtColor(imagem_rgb, cv2.COLOR_BGR2HSV)

hue = img_HSV[:, :, 0]
saturation = img_HSV[:, :, 1]
value = img_HSV[:, :, 2]


# def downsample(s, n):
#     """Decrementa a taxa de amostragem pelo fator n. """
#     return s[::n, ::n]
#
#
# def upsample(s, n):
#     """Aumenta a taxa de amostragem pelo fator n. """
#     return np.repeat(np.repeat(s, n, axis=0), n, axis=1)
#
# novo_hue = downsample(hue, 2)
# novo_saturation = downsample(saturation, 2)
# novo_hue = upsample(novo_hue, 2)
# novo_saturation = upsample(novo_saturation, 2)
# novo_hue = downsample(hue, 4)
# novo_saturation = downsample(saturation, 4)
# novo_hue = upsample(novo_hue, 4)
# novo_saturation = upsample(novo_saturation, 4)
# novo_hue = downsample(hue, 8)
# novo_saturation = downsample(saturation, 8)
# img_HSV[:, :, 0] = upsample(novo_hue, 8)
# img_HSV[:, :, 1] = upsample(novo_saturation, 8)

def quantiz(img, n):
    nmin = np.min(img)
    nmax = np.max(img)

    b = np.float32(img) / (nmax - nmin)
    c = np.round(b * (n - 1))

    d = np.round(c / (n - 1) * (nmax - nmin))
    d = d + nmin
    return d


def AlteraCor(img, n):
    b = quantiz(img, n)
    b = np.uint8(b)
    return b


def quantizacao_simples(img, K):
    a = np.float32(img)
    bucket = 256 / K
    quantizado = (a / (256 / K))
    return np.uint8(quantizado) * bucket

cor = 17
# img_HSV[:, :, 0] = quantizacao_simples(hue, cor)
# img_HSV[:, :, 1] = quantizacao_simples(saturation, cor)
img_HSV[:, :, 0] = AlteraCor(hue, cor)
img_HSV[:, :, 1] = AlteraCor(saturation, cor)
img_HSV[:, :, 0] = np.uint8(hue/cor)*cor
img_HSV[:, :, 1] = np.uint8(saturation/cor)*cor


img_final = cv2.cvtColor(img_HSV, cv2.COLOR_HSV2BGR)

cv2.imshow("Imagem Final", img_final)
cv2.imshow("Imagem Original", imagem_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
