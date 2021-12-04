    1. Problema dos missionários e canibais

Três missionários e três canibais estão em um lado do rio, juntamente com um barco que pode conter uma ou duas pessoas. Descubra um meio de fazer todos atravessarem o rio, sem deixar que um grupo de missionários de um lado fique em número menor que o número de canibais nesse lado do rio. Esse problema é famoso em IA, porque foi assunto do primeiro artigo que abordou a formulação de problemas a
partir de um ponto de vista analítico (Amarel, 1968).

Implemente e resolva o problema de forma ótima, utilizando um algoritmo de busca apropriado. É boa idéia verificar a existência de estados repetidos?

    2. Problema do metrô de Paris

Suponha que queremos construir um sistema para auxiliar um usuário do metrô de Paris a saber o trajeto mais rápido entre a estação onde ele se encontra e a estação de destino. O usuário tem um painel com o mapa, podendo selecionar a sua estação de destino. O sistema então acende as luzes sobre o mapa mostrando o melhor trajeto
a seguir (em termos de quais estações ele vai atravessar., e quais as conexões mais rápidas a fazer – se for o caso).  
Considere que:

- a distância em linha reta entre duas estações quaisquer é dada em uma tabela.
  Para facilitar a vida, considere apenas 4 linhas do metrô.
- a velocidade média de um trem é de 30km/h;
- tempo gasto para trocar de linha dentro de mesma estação (fazer baldeação) é de
  4 minutos.

Formule e implemente este problema em termos de estado inicial, estado final, operadores e função de avaliação para Busca heurística com A\*.

<img src="https://i.imgur.com/tdJzTSd.jpg" width="600px">
<img src="https://i.imgur.com/bw2Ro6H.png" width="600px">

    3. O problema do caixeiro viajante

Um caixeiro viajante precisa visitar 10 cidades do interior de Pernambuco. Ele pede a
um agente de busca que determine uma rota para sua visita tal que cada cidade só
seja visitada uma única vez, e ele percorra o menor espaço possível (em Km). O
agente de busca tem um mapa do estado, e portanto sabe as distâncias entre as
cidades.
Formule e implemente este problema em termos de estado inicial, estado final, operadores e função de avaliação para Busca por melhoras iterativas com Hill-
Climbing.

O operador considerado para gerar os filhos do estado corrente é permutar as
cidades da rota atual duas a duas, e verificar em seguida se o caminho está
conectado (segundo a tabela abaixo, que representa o mapa da questão). A cidade
inicial deve ser mantida, uma vez que o caixeiro mora lá ! A rota é fechada (ele volta
à cidade de origem no final).

<img src="https://i.imgur.com/ebFhEEo.png">

    4. Jogo para dois jogadores

Escolha um jogo para dois jogadores (ex.: jogo da velha, othelo, damas, xadrez, etc.) e implemente-o utilizando o minimax.  
<strong>-> Jogo da Velha foi o jogo escolhido.</strong>
