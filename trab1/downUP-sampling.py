import numpy as np

# imagem 4x4 para teste 2D 2UP 4D 4UP
imagem = np.matrix([[0, 1, 2, 3], [10, 11, 12, 13], [
                   20, 21, 22, 23], [30, 31, 32, 33]])

print (imagem)


def downsample(s, n, phase=0):
    """Decrementa a taxa de amostragem pelo fator n. """
    return s[::n, ::n]

print ("downsample")
a = [0, 1, 2, 3, 4]
operacao_one = downsample(imagem, 2)
print (operacao_one)


def upsample(s, n, phase=0):
    """Aumenta a taxa de amostragem pelo fator n. """
    return np.repeat(np.repeat(s, n, axis=0), n, axis=1)

print (upsample(operacao_one, 2, 2))
