# Questão 2

A segunda questão da prova 2 de processamento de imagens consistiu em aplicar a segmentação em grãos de arroz, utilizado o metodo de tophat, o detalhamento do método bem como sua funções em python seguem abaixo:

A seguinte imagem foi utilizada para fazer os calculos de morfologia citados abaixo, foi utilizado o seguinte kernel como elemento estruturante, para os calculos.

```python
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (65, 65))
```

* Imagem Original

![alt tag](https://github.com/LucasHelal/ProcessamentoImagensMestrado/blob/master/prova2/Questao2/Gr%C3%A3o%20de%20Arroz.png?raw=true)

* Dilatação

Esta operação consiste em convolucionar uma imagem A com um kernel (B), que pode ter qualquer forma ou tamanho, geralmente um quadrado ou círculo, no caso uma elipse.

```python
def Dilatacao(img, kernel):
    return cv2.dilate(img, kernel, iterations=1)
```

Segue a imagem feita a dilatação da imagem Original:
![alt tag](https://github.com/LucasHelal/ProcessamentoImagensMestrado/blob/master/prova2/Questao2/Dilata%C3%A7%C3%A3o.png?raw=true)

* Erosão

Esta operação é a irmã da dilatação. Ela calcula um mínimo local sobre a área do kernel.

```python

def Erosao(img, kernel):
    return cv2.erode(img, kernel, iterations=1)
```
Segue a imagem feita a erosão da imagem Original:

![alt tag](https://github.com/LucasHelal/ProcessamentoImagensMestrado/blob/master/prova2/Questao2/Eros%C3%A3o.png?raw=true)

* Abertura

É obtida pela erosão de uma imagem seguida por uma dilatação.

```python
def Abertura(img, kernel):
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
```
Segue a imagem feita a Abertura da imagem Original:

![alt tag](https://github.com/LucasHelal/ProcessamentoImagensMestrado/blob/master/prova2/Questao2/Abertura.png?raw=true)

* Fechamento

Obtém-se pela dilatação de uma imagem seguida de erosão.

```python
def Fechamento(img, kernel):
    return cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
```
Segue a imagem feita a Fechamento da imagem Original:

![alt tag](https://github.com/LucasHelal/ProcessamentoImagensMestrado/blob/master/prova2/Questao2/Fechamento.png?raw=true)

* TopHat

É a diferença entre uma imagem de entrada e sua abertura.

```python
def TopHat(img, kernel):
    return cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
```
Segue a imagem feita a TopHat da imagem Original:

![alt tag](https://github.com/LucasHelal/ProcessamentoImagensMestrado/blob/master/prova2/Questao2/Top%20Hat.png?raw=true)

* Segmentação OTSU

Assim com o calculo do TopHat feito é possivel obter uma melhor limirização da imagem, com o otsu. Assim conseguindo segmentar de forma mais adqueda os grãos de arroz.

Segue a imagem feita a OTSU do TopHat:

![alt tag](https://github.com/LucasHelal/ProcessamentoImagensMestrado/blob/master/prova2/Questao2/OTSU.png?raw=true)
