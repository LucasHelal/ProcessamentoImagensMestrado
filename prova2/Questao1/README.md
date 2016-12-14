# Questão 1

A primeira questão da prova 2 de processamento de imagens consistiu em aplicar o filtro Butterworth em uma convertida para em tons de cinza, o detalhamento do método bem como sua funções em python seguem abaixo:


Para resolver essa questão inicialmete foi feito um a conversão da imagem para tons de cinza, com a imagem convertida foi aplicado a transformada de fourier, em seguinda foi criado um filtro passa alta de Butterworth, assim podendo realizar a aplicação do filtro na imagem transformada, em seguinda é feito a inversa da transformada e equalização da imagem, para um melhor resultado final. A imagem a seguir mostra uma esquematização de com foi resolvido a questão.

Esquematização do Problema

![alt tag](https://github.com/LucasHelal/ProcessamentoImagensMestrado/blob/master/prova2/Questao1/passos.png?raw=true)


Assim utilizar a transformada de fourier na imagem original, foi utilizado o seguinte metodo da biblioteca numpy:

```python
imagem_transformada = np.fft.fftshift(np.fft.fft2(imagem_cinza))

```

O filtro passa alta da função Butterworth foi obtido com o seguinte metodo:

```python
def Butterworth(shape, f, n):
    linha, coluna = shape
    x = np.linspace(-0.5, 0.5, coluna) * coluna
    y = np.linspace(-0.5, 0.5, linha) * linha
    raio = np.sqrt((x**2)[np.newaxis] + (y**2)[:, np.newaxis])
    filtro = 1 / (1.0 + (f / raio)**(2 * n))
    return filtro

```
O valor de n (ordem do filtro) determina a
“suavidade” do filtro e o valor de f é o corte da frequencia. Para esse exemplo foram adotados n=4 e f=200.

Após o calculo do filtro é realizado uma multiplicada entre as imagens, a transformada e o filtro. Para que seja feita a transformada inversa, conforme segue respectivamente o metodo e a imagem.

```python
imagem_transformada_invertida = np.abs(np.fft.ifft2(
    np.fft.ifftshift(imagem_transformada_filtrada)))
```

Imagem Invertida

![alt tag](https://github.com/LucasHelal/ProcessamentoImagensMestrado/blob/master/prova2/Questao1/Imagem_Invertida.png?raw=true)


Após o calculo da inversa foi realizado o calculo do histograma equalizado e depois o calculo de limiriazação, seguem as imagens obtidas:

Imagem Equalizada

![alt tag](https://github.com/LucasHelal/ProcessamentoImagensMestrado/blob/master/prova2/Questao1/res.png?raw=true)

Imagem Threshold - OTSU

![alt tag](https://github.com/LucasHelal/ProcessamentoImagensMestrado/blob/master/prova2/Questao1/otsu.png?raw=true)
