from funcoes import desenhar_poligono, scanline_fill, gerar_elipse
from cenario import MESAS, LARGURA_MESA, ALTURA_MESA
import pygame

# Cores
MARROM = (139, 69, 19)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Tamanho do cachorro
TAMANHO = 40

# Posição inicial (centro da tela)
x = 540
y = 360

# Velocidade de movimento
VELOCIDADE = 5

def mover(teclas, largura_tela, altura_tela):
    global x, y

    novo_x = x
    novo_y = y

    # Entrada do jogador
    if teclas[pygame.K_w] or teclas[pygame.K_UP]:
        novo_y -= VELOCIDADE
    if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
        novo_y += VELOCIDADE
    if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
        novo_x -= VELOCIDADE
    if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
        novo_x += VELOCIDADE

    metade = TAMANHO // 2

    # Limite da tela
    if novo_x - metade < 0:
        novo_x = metade
    if novo_x + metade > largura_tela:
        novo_x = largura_tela - metade
    if novo_y - metade < 0:
        novo_y = metade
    if novo_y + metade > altura_tela:
        novo_y = altura_tela - metade

    # Atualiza posição se não colidir com mesa
    if not colidiu_com_mesa(novo_x, novo_y):
        x = novo_x
        y = novo_y

def colidiu_com_mesa(novo_x, novo_y):
    metade = TAMANHO // 2

    # Limites do cachorro
    cachorro_esq = novo_x - metade
    cachorro_dir = novo_x + metade
    cachorro_top = novo_y - metade
    cachorro_bot = novo_y + metade

    for (mx, my) in MESAS:
        mesa_esq = mx
        mesa_dir = mx + LARGURA_MESA
        mesa_top = my
        mesa_bot = my + ALTURA_MESA

        # Teste de colisão AABB
        if (
            cachorro_dir > mesa_esq and
            cachorro_esq < mesa_dir and
            cachorro_bot > mesa_top and
            cachorro_top < mesa_bot
        ):
            return True

    return False

def desenhar_cachorro(superficie):
    xc = int(x)
    yc = int(y)

    # Corpo
    corpo = gerar_elipse(xc, yc, 30, 20, passos=100)
    scanline_fill(superficie, corpo, MARROM)
    desenhar_poligono(superficie, corpo, PRETO)

    # Orelha
    orelha = gerar_elipse(xc - 20, yc - 5, 10, 15, passos=80)
    scanline_fill(superficie, orelha, PRETO)

    # Olho
    olho = gerar_elipse(xc - 8, yc - 2, 2, 2, passos=40)
    scanline_fill(superficie, olho, PRETO)

    # Nariz
    nariz = gerar_elipse(xc + 25, yc, 4, 4, passos=40)
    scanline_fill(superficie, nariz, PRETO)