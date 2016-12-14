import cv2
import sys
import numpy as np
from skimage import exposure


# 1. Imagem em Cinza
# 2. Calcular transformada de fourier
# 3. Aplicar filtro passa alta butterworth
# 4. Aplicar inversa de fourier
# 5. Normalizar OTSU

imagem_cinza = cv2.imread(sys.argv[1], 0)

imagem_transformada = np.fft.fftshift(np.fft.fft2(imagem_cinza))


def Butterworth(shape, f, n):
    linha, coluna = shape
    x = np.linspace(-0.5, 0.5, coluna) * coluna
    y = np.linspace(-0.5, 0.5, linha) * linha
    raio = np.sqrt((x**2)[np.newaxis] + (y**2)[:, np.newaxis])
    filtro = 1 / (1.0 + (f / raio)**(2 * n))
    return filtro


def ButterworthPassaAlta(shape, f, n):
    passa_alta = 1. - Butterworth(shape, f, n)
    return passa_alta


imagem_BW_passa_alta = ButterworthPassaAlta(imagem_cinza.shape, 200, 4)

imagem_transformada_filtrada = imagem_transformada * imagem_BW_passa_alta

imagem_transformada_invertida = np.abs(np.fft.ifft2(
    np.fft.ifftshift(imagem_transformada_filtrada)))

imagem_equalizada = exposure.equalize_hist(imagem_transformada_invertida)

cv2.imshow("Original", imagem_cinza)
cv2.imshow("Filtro BW", imagem_BW_passa_alta)
cv2.imshow("Imagem Invertida", imagem_transformada_invertida)
cv2.imwrite("Imagem_Invertida.png", imagem_transformada_invertida)
cv2.imshow("Imagem Equalizada", imagem_equalizada)
cv2.imwrite("Imagem_Equalizada.png", imagem_equalizada)
# ret, imgOTSU = cv2.threshold(imagem_equalizada, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# cv2.imshow("Imagem OTSU", imgOTSU)

cv2.waitKey(0)
cv2.destroyAllWindows()
