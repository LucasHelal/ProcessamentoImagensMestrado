# Trabalho 2
O segundo trabalho de processamento de imagens consistiu em aplicar o método de ChromaSample em uma imagem colorida, o detalhamento do método bem como sua função em python seguem abaixo:


* ChromaSample

É um esquema de codificação de imagens e vídeos através da implementação de componentes para mais informações de cores do que a luminância, aproveitando-se assim do sistema de visão humana que tem menor capacidade para diferenciar cores do que luminosidades. Este método de codificação faz com que imagens e vídeos tenham um tamanho menor em bits.

O seguinte método em python, consiste em reduzir a quatidade de cores de dado uma banda de cor, no as banda utilizadas foram (H e S) de uma de uma imagem convertida para HSV.

```python
def ChromaSample(banda, valor):
    bloco = np.uint8(180 / valor)
    quantizado = np.uint8(banda / bloco)
    banda = np.uint8((quantizado * bloco) + bloco / 2)

    return banda
```
A seguir é feita a conversão da imagem RGB para HSV, logo depois é feito a separação das bandas no caso apenas a hue e saturation, mantendo o value.
Após feito a separação é feito a aplicação do ChromaSample nas duas bandas.
Os valores adotados para o K foram 4, 8 e 16 para comparações.

```python
img_HSV = cv2.cvtColor(imagem_rgb, cv2.COLOR_BGR2HSV)

hue = img_HSV[:, :, 0]
saturation = img_HSV[:, :, 1]

img_HSV[:, :, 0] = ChromaSample(hue, k_cores)
img_HSV[:, :, 1] = ChromaSample(saturation, k_cores)

img_final = cv2.cvtColor(img_HSV, cv2.COLOR_HSV2BGR)
```
A baixo seguente as imagens geradas com o metodo de ChromaSample, para os K = 4, K = 8 e K =16.
As imagens da esquerda são as originais e as da direita com seus respectivos K.


K = 4
![alt tag](https://github.com/LucasHelal/ProcessamentoImagensMestrado/blob/master/trab2/final-k=4.png?raw=true)
K = 8
![alt tag](https://raw.githubusercontent.com/LucasHelal/ProcessamentoImagensMestrado/master/trab2/final-k%3D8.png)
K = 16
![alt tag](https://github.com/LucasHelal/ProcessamentoImagensMestrado/blob/master/trab2/final-k=16.png?raw=true)
