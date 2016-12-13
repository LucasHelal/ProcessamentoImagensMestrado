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


def Otsu(img):
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    hist_norm = hist.ravel() / hist.max()
    Q = hist_norm.cumsum()

    bins = np.arange(256)

    fn_min = np.inf
    thresh = -1

    for i in range(1, 256):
        p1, p2 = np.hsplit(hist_norm, [i])  # probabilities
        q1, q2 = Q[i], Q[255] - Q[i]  # cum sum of classes
        b1, b2 = np.hsplit(bins, [i])  # weights

        # finding means and variances
        m1, m2 = np.sum(p1 * b1) / q1, np.sum(p2 * b2) / q2
        v1, v2 = np.sum(((b1 - m1)**2) * p1) / \
            q1, np.sum(((b2 - m2)**2) * p2) / q2

        # calculates the minimization function
        fn = v1 * q1 + v2 * q2
        if fn < fn_min:
            fn_min = fn
            thresh = i
    return thresh


def Threshold(img, threshold):
    preto = np.abs(img) < threshold
    img[preto] = 0
    branco = np.abs(img) > threshold
    img[branco] = 255
    return img


valor_otsu = Otsu(image_cinza)
imgT = Threshold(image_cinza, valor_otsu)


def CorrecaoDeContrasteLinear(imagem_original, imagem_otsu):
    valores = np.where(imagem_otsu == 0)
    correcao_linear = imagem_original[valores]
    minimo = np.min(correcao_linear)
    maximo = np.max(correcao_linear)
    a = 255 / (maximo - minimo)
    b = -a * minimo
    correcao = np.uint8(a * correcao_linear + b)
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
cv2.imwrite("ContrasteLinear.png", imagem_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()
