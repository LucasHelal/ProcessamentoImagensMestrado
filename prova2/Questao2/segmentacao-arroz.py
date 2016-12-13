import cv2
import sys

# 1 Converter para Cinza
# 2 Obter elemento estruturante
# 3 Fazer Abertura e Fechamento (Dilatação e Erosão)
# 4 Aplicar TOP HAT
# 5 Aplicar OTSU


imagem = cv2.imread(sys.argv[1])

imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (65, 65))


def Dilatacao(img, kernel):
    return cv2.dilate(img, kernel, iterations=1)


def Erosao(img, kernel):
    return cv2.erode(img, kernel, iterations=1)


def Abertura(img, kernel):
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)


def Fechamento(img, kernel):
    return cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)


def TopHat(img, kernel):
    return cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)


imagem_dilatacao = Dilatacao(imagem_cinza, kernel)
imagem_erosao = Erosao(imagem_cinza, kernel)
imagem_abertura = Abertura(imagem_cinza, kernel)
imagem_fechamento = Fechamento(imagem_cinza, kernel)
imagem_top_hat = TopHat(imagem_cinza, kernel)

ret, imgOTSU = cv2.threshold(
    imagem_top_hat, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("Dilatação", imagem_dilatacao)
cv2.imshow("Erosão", imagem_erosao)
cv2.imshow("Abertura", imagem_abertura)
cv2.imshow("Fechamento", imagem_fechamento)
cv2.imshow("Top Hat", imagem_top_hat)
cv2.imshow("OTSU", imgOTSU)
cv2.imshow("Grão de Arroz", imagem_cinza)

cv2.imwrite("Dilatação.png", imagem_dilatacao)
cv2.imwrite("Erosão.png", imagem_erosao)
cv2.imwrite("Abertura.png", imagem_abertura)
cv2.imwrite("Fechamento.png", imagem_fechamento)
cv2.imwrite("Top Hat.png", imagem_top_hat)
cv2.imwrite("OTSU.png", imgOTSU)
cv2.imwrite("Grão de Arroz.png", imagem_cinza)


cv2.waitKey(0)
cv2.destroyAllWindows()
