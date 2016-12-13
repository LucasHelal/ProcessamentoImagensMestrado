# Trabalho 3
O terceiro trabalho de processamento de imagens consistiu em aplicar o método de OTSU para limiarização de uma imagem colorida, seguida de uma metodo de correção de contrates, no caso foi adotado uma correção de contrates linear, o detalhamento dos métodos bem como sua funçõeso em python seguem abaixo:

* OTSU

O método de Otsu é um algoritmo de limiarização. Seu objetivo é, a partir de uma imagem em tons de cinza, determinar o valor ideal de um threshold que separe os elementos do fundo e da frente da imagem em dois
clusters,   atribuindo   a   cor   branca   ou   preta   para   cada   um   deles.   Devido   à   essa
característica, funciona especialmente bem para casos de imagens  com histogramas
bimodais, podendo ser divididas adequadamente com um único valor.

Abaixo esta implementando o metodo Otsu em python para obter o melhor valor para ser feito um threshold, que apartir do valor obtido é aplicado na função seguinte de threshold.

```python
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
```

A imagem Original de entrada é convertida de para tons de cinza, para se obter o valor para o threshold.

```python
valor_otsu = Otsu(image_cinza)
imgT = Threshold(image_cinza, valor_otsu)
```

* Correção de Contraste Linear

O aumento de contraste por uma transformação linear é a forma mais simples das opções. A função de transferência é uma reta e apenas dois parâmetros são controlados: a inclinação da reta e o ponto de interseção com o eixo X. A inclinação controla a quantidade de aumento de contraste e o ponto de interseção com o eixo X controla a intensidade média da imagem final.
A função de mapeamento linear pode ser representada por:

Y = AX + B

onde:

Y = novo valor de nível de cinza;

X = valor original de nível de cinza;

A = inclinação da reta (tangente do ângulo);

B = fator de incremento, definido pelos limites mínimo e máximo fornecidos pelo usuário.

O método em python foi aplicado nas regiões destacadas na imagem em foi calculado o Threshold apartir do valor calculado com o otsu.

```python
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
```


Foram separada as bandas da imagem colorida para aplicar a correção linear. Conforme segue.

```python
B = imagem_rgb[:, :, 0]
G = imagem_rgb[:, :, 1]
R = imagem_rgb[:, :, 2]
imagem_rgb[:, :, 0] = CorrecaoDeContrasteLinear(B, imgT)
imagem_rgb[:, :, 1] = CorrecaoDeContrasteLinear(G, imgT)
imagem_rgb[:, :, 2] = CorrecaoDeContrasteLinear(R, imgT)
```

Abaixo temos a imagem Original e a aplicação da correção de contraste apartir da em que foi aplicado o otsu.

Imagem Original


![alt tag](https://github.com/LucasHelal/ProcessamentoImagensMestrado/blob/master/arvore.jpg?raw=true)

Imagem com Correção de Contrates Linear

![alt tag](https://github.com/LucasHelal/ProcessamentoImagensMestrado/blob/master/trab3/ContrasteLinear.png?raw=true)
