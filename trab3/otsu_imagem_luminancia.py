import numpy as np
import cv2
import sys


# 1 - Abre imagem colorida
# 2 - Converte para tons de cinza
# 3 - Aplica o otsu (criar função)
# 4 - Pega pixels pretos
# 5 - Normaliza eles

imagem_rgb = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)

image_cinza = cv2.cvtColor(imagem_rgb, cv2.COLOR_BGR2GRAY)


ret, imgT = cv2.threshold(
    image_cinza, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)


# TODO implementar otsu metodo
def Otsu(imagem):
    pass


def Threshold(img, threshold):
    preto = np.abs(img) < threshold
    img[preto] = 0
    branco = np.abs(img) > threshold
    img[branco] = 255
    return img


def CorrecaoDeContrasteLinear(imagem_original, imagem_otsu):
    valores = np.where(imagem_otsu == 0)
    correcao_linear = imagem_original[valores]
    print(np.shape(correcao_linear))
    minimo = np.min(correcao_linear)
    maximo = np.max(correcao_linear)
    a = 255 / (maximo - minimo)
    b = -a*minimo
    correcao = np.uint8(a*correcao_linear + b)
    imagem_original[valores] = correcao
    return imagem_original


B = imagem_rgb[:, :, 0]
G = imagem_rgb[:, :, 1]
R = imagem_rgb[:, :, 2]
imagem_rgb[:, :, 0] = CorrecaoDeContrasteLinear(B, imgT)
imagem_rgb[:, :, 1] = CorrecaoDeContrasteLinear(G, imgT)
imagem_rgb[:, :, 2] = CorrecaoDeContrasteLinear(R, imgT)
# imgTeste = Threshold(image_cinza, 104)

cv2.imshow("Correção de Contraste Linear", imagem_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()
