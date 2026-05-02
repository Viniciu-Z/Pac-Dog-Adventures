import random
import math
from funcoes import *
from cenario import mesas, largura_mesa, altura_mesa
import cachorro

VERMELHO = (255, 0, 0)
tamanho_alimento = 20

# Posição
x = 0
y = 0

# Animação
angulo = 0
tempo = 0

def gerar_alimento(largura_tela, altura_tela):
    global x, y

    while True:
        novo_x = random.randint(tamanho_alimento, largura_tela - tamanho_alimento)
        novo_y = random.randint(tamanho_alimento, altura_tela - tamanho_alimento)

        if not dentro_da_mesa(novo_x, novo_y) and not perto_do_cachorro(novo_x, novo_y):
            x = novo_x
            y = novo_y
            break

def dentro_da_mesa(px, py):
    for (mx, my) in mesas:
        if (
            px > mx and px < mx + largura_mesa and
            py > my and py < my + altura_mesa
        ):
            return True
    return False

def perto_do_cachorro(px, py):
    metade = cachorro.tamanho // 2

    if (
        px > cachorro.x - metade and
        px < cachorro.x + metade and
        py > cachorro.y - metade and
        py < cachorro.y + metade
    ):
        return True

    return False

def desenhar_alimento(superficie):
    global angulo, tempo

    # Atualiza animação
    angulo += 0.05
    tempo += 0.08

    escala_anim = 1.0 + 0.3 * math.sin(tempo)

    # Elipse centrada na origem
    pontos = gerar_elipse(0, 0, tamanho_alimento // 2, tamanho_alimento // 2, passos=50)

    # Transformações
    m = cria_transformacao()
    m = multiplica_matrizes(translacao(0, 0), m)
    m = multiplica_matrizes(rotacao(angulo), m)
    m = multiplica_matrizes(escala(escala_anim, escala_anim), m)
    m = multiplica_matrizes(translacao(x, y), m)

    pontos_transformados = aplica_transformacao(m, pontos)

    # Desenho
    janela = (0, 0, superficie.get_width(), superficie.get_height())

    scanline_fill(superficie, pontos_transformados, VERMELHO)
    desenhar_poligono_recortado(superficie, pontos_transformados, janela, (0, 0, 0))

def colidiu_com_jogador():
    metade_dog = cachorro.tamanho // 2
    metade_food = tamanho_alimento // 2

    dog_x = cachorro.x
    dog_y = cachorro.y

    if (
        dog_x + metade_dog > x - metade_food and
        dog_x - metade_dog < x + metade_food and
        dog_y + metade_dog > y - metade_food and
        dog_y - metade_dog < y + metade_food
    ):
        return True

    return False