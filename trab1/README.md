# Trabalho 1


O primeiro trabalho de processamento de imagens consistiu em aplicar Downsampling e Upsampling em uma imagem em tons de cinza, o detalhamento de ambos método bem como sua funções em python seguem abaixo:


 * Downsampling

  Ou também chamada de decimação é a técnica de redução da taxa de amostragem. Isso é feito simplesmente separando uma amostra a cada N.
```python
"""Decrementa a taxa de amostragem pelo fator n. """
 def downsample(s, n):
     return s[::n, ::n]
```
 * Upsampling

 É um técnica de processamento digital de sinais utilizada para aumentar artificialmente a taxa de amostragem em N vezes, inserindo um número N-1 de zeros entre as amostras originais do sinal, e passando o conjunto obtido por um filtro de reconstrução, que nada mais é que um filtro do tipo passa-baixas.
```python
    """Aumenta a taxa de amostragem pelo fator n. """
def upsample(s, n):
    return np.repeat(np.repeat(s, n, axis=0), n, axis=1)
```

A imagem original de entrada é a imagem da lena com tamanho de 512x512, nesta imagem foi aplicado o downsample e o upsampling 7 vezes, sendo os seguintes valores para o n = [2, 4, 8, 16, 32, 64, 128, 256].

As 8 imagens, sendo a original e as 7 aplicações dos métodos podem ser obeservado no gif abaixo.

![Lena :d] (https://raw.githubusercontent.com/LucasHelal/ProcessamentoImagensMestrado/master/trab1/lena-animation.gif)
