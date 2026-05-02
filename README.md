# Pac-Dog Adventures
Aluno: Prudencio Vinicius

# Proposta do Jogo
Você já parou para pensar em como o Restaurante Universitário é visto por um cachorro? Devido à presença frequente deles nos horários de almoço, é possível imaginar que eles enxergam o local como uma oportunidade de encontrar alimento. Ao mesmo tempo, a disposição das mesas pode transformar o ambiente em um verdadeiro labirinto.

A proposta do jogo é colocar o jogador nessa perspectiva: assumir o papel de um cachorro explorando o restaurante. Inspirado no clássico Pac-Man, porém de forma mais simples, o objetivo é coletar o máximo de comida possível antes que o tempo acabe, desviando dos obstáculos formados pelas mesas e navegando pelo “labirinto” do ambiente.

# O Desafio: Uso da Biblioteca Pygame
Este projeto foi desenvolvido utilizando a biblioteca Pygame em Python, partindo da manipulação direta de pixels por meio da primitiva setPixel. O objetivo foi implementar, de forma manual, os principais conceitos de Computação Gráfica, evitando o uso de funções gráficas prontas.
Para isso, foram utilizados algoritmos clássicos, descritos a seguir:

- Algoritmo de Bresenham para o traçamento de retas;
- Preenchimento de polígonos com Scanline e de regiões delimitadas com Flood Fill;
- Desenho de primitivas geométricas, como retas, polígonos, circunferências e elipses;
- Transformações geométricas (rotação, translação e escala), implementadas por meio de cálculo matricial;
- Algoritmo de recorte Sutherland–Hodgman, utilizado para delimitação da área visível (clipping).

# Estrutura dos Arquivos
1 - funcoes.py
Este é o arquivo base do projeto. Ele concentra os principais algoritmos de Computação Gráfica utilizados, como rasterização, preenchimento, transformações geométricas e operações auxiliares. Todas as outras partes do sistema dependem diretamente dessas funções.

2 - jogo.py
É o arquivo principal (main) do projeto. Nele ocorre a integração de todos os componentes do jogo, incluindo controle de fluxo, eventos, renderização e execução geral.

3 - cenario.py
Responsável pela construção do cenário onde o jogo acontece. Contém os obstáculos (mesas), que são desenhados com o algoritmo de Bresenham e preenchidos com scanline em gradiente. Também inclui a aplicação de textura no fundo, simulando o chão.

4 - cachorro.py
Define o personagem controlado pelo jogador, o “Pac Dog”. Além do desenho do personagem, este módulo gerencia o movimento e as colisões, tanto com os obstáculos do cenário quanto com os limites da tela.

5 - alimento.py
Responsável pelo objeto coletável do jogo, que gera pontuação. O alimento aparece aleatoriamente no cenário, evitando posições inválidas (como dentro das mesas ou sobre o jogador). Também é neste arquivo que são aplicadas transformações geométricas e animações.

6 - pontuacao.py
Módulo responsável pelo controle da pontuação do jogador. Gerencia a contagem de pontos e sua exibição na tela.

7 - temporizador.py
Implementa o sistema de tempo do jogo, controlando a duração da partida e atualizando o tempo restante.

8 - viewport.py
Responsável pela implementação do minimapa. Realiza a transformação de coordenadas do mundo para a viewport, permitindo visualizar uma versão reduzida do cenário com os principais elementos (jogador, alimento e obstáculos).

9 - telas.py
Contém as telas do jogo, como a tela inicial e a tela de game over. Gerencia a interface visual dessas etapas e a interação básica do usuário (iniciar ou reiniciar o jogo).

# Como Executar
Este projeto foi desenvolvido utilizando a linguagem Python com a biblioteca Pygame, sendo implementado e testado no ambiente de desenvolvimento PyCharm.
Antes de executar o projeto, é necessário ter instalado:
- Python (versão 3.x)
- Biblioteca Pygame

No Pycharm:
Localize o arquivo principal do projeto: jogo.py
Clique com o botão direito sobre o arquivo e selecione “Run jogo”.

Caso prefira executar fora do PyCharm:
Abra o terminal na pasta do projeto;
Execute o comando:
python jogo.py

