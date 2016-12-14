# Questão 4

Imagem binária obtinada na questão 2.

![alt tag](https://github.com/LucasHelal/ProcessamentoImagensMestrado/blob/master/prova2/Questao2/OTSU.png?raw=true)


Uma imagem binária é toda imagem que possui apenas duas cores, preferencialmente branco (1) ou preto (0).

Para a contagem dos objetos nesse tipo de imagem binária, basta aplicar uma busca em largura para pixels que possui o nível da cor escolhida. Caso os objetos sejam identificados pela cor branca, será aplicado a busca em largura apenas para esses pixels.

A busca em largura é aplicado em grafos ou árvores, de maneira que é selecionado um nó arbitrário e todos os nós vizinhos desse nó são visitados primeiro, antes de avançar para o próximo nível de vizinhos.

Assim, através da contagem de objetos cria-se uma variável para armazenar a quantidade de objetos encontrados e verifica cada pixel da imagem, de maneira que se a cor desse pixel é branca e não tiver sido pintado (visitado), incrementa-se a quantidade de objetos, aplica o algoritmo de busca em largura (BFS) a partir das coordenadas do pixel encontrado e por fim, incrementa-se o rotulo pintado para que o próximo objeto tenha uma tonalidade diferente.

O BFS inicialmente marca como visitado a coordenada do pixel escolhido e verifica todos os vizinhos desse ponto, de modo que se o vizinho possuir um nível de cinza maior que zero e não tiver sido visitado, pinte esse pixel e adicione em uma fila para que posteriormente seja verificado os vizinhos desse ponto.

A busca dos vizinhos de um nó é feita de acordo pode ser vista abaixo, em que busca-se apenas os 4 pontos adjacentes a ele. Por exemplo, em uma imagem de tamanho 100x100, se o ponto escolhido possuir coordenada em (50, 50) os vizinhos serão: (49, 50), (51, 50), (50, 49), (50, 51).


Observação: Durante a graduação realizei um trabalho de PDI, com o professor Frank, que fazia o mesmo, porém a imagem de entrada era outra.
Mais detalhes de como realizar a contagem basta chegar o blog que eu escrevi para o trabalho da graduação:

[Blog-Medium Lucas Helal: Detecção e Contagem da Área de Objetos em Uma Imagem Binária](https://medium.com/@lucashelal/detec%C3%A7%C3%A3o-e-contagem-da-%C3%A1rea-de-objetos-em-uma-imagem-bin%C3%A1ria-440759a7e034#.pq19w95lj)
