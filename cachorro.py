from funcoes import desenhar_poligono, scanline_fill, gerar_elipse
from cenario import mesas, largura_mesa, altura_mesa
import pygame

MARROM = (139, 69, 19)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

tamanho = 40

# Posição inicial no centro da tela
x = 540
y = 360

# Velocidade de movimento
velocidade = 5

def mover(teclas, largura_tela, altura_tela):
    global x, y

    novo_x = x
    novo_y = y

    # Entrada do jogador
    if teclas[pygame.K_w]:
        novo_y -= velocidade
    if teclas[pygame.K_s]:
        novo_y += velocidade
    if teclas[pygame.K_a]:
        novo_x -= velocidade
    if teclas[pygame.K_d]:
        novo_x += velocidade

    metade = tamanho // 2

    # Limite da tela
    if novo_x - metade < 0:
        novo_x = metade
    if novo_x + metade > largura_tela:
        novo_x = largura_tela - metade
    if novo_y - metade < 0:
        novo_y = metade
    if novo_y + metade > altura_tela:
        novo_y = altura_tela - metade

    if not colidiu_com_mesa(novo_x, novo_y):
        x = novo_x
        y = novo_y

def colidiu_com_mesa(novo_x, novo_y):
    metade = tamanho // 2

    # Limites do cachorro
    cachorro_esq = novo_x - metade
    cachorro_dir = novo_x + metade
    cachorro_top = novo_y - metade
    cachorro_bot = novo_y + metade

    for (mx, my) in mesas:
        mesa_esq = mx
        mesa_dir = mx + largura_mesa
        mesa_top = my
        mesa_bot = my + altura_mesa

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