import pygame
from funcoes import *

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (150, 150, 150)

largura_mesa = 400
altura_mesa = 235

mesas = [
    (70, 70),
    (600, 70),
    (70, 410),
    (600, 410)
]

# Superfície separada do cenario
# Para desenhar o cenario apenas uma vez e melhorar o desempenho
cenario_surface = None

def desenhar_mesa(superficie, x, y):
    # Defini os pontos para desenhar o poligono (retangulo)
    pontos = [
        (x, y),
        (x + largura_mesa, y),
        (x + largura_mesa, y + altura_mesa),
        (x, y + altura_mesa)
    ]

    # cores para o scanline gradiente
    cores = [
        (220, 220, 220),
        (220, 220, 220),
        (60, 60, 60),
        (60, 60, 60)
    ]

    janela = (0, 0, superficie.get_width(), superficie.get_height())

    scanline_fill_gradiente(superficie, pontos, cores)

    desenhar_poligono_recortado(superficie, pontos, janela, PRETO)

def desenhar_fundo_textura(superficie, textura):
    largura, altura = superficie.get_width(), superficie.get_height()

    # Pontos do poligono que cobre a tela inteira
    pontos = [
        (0, 0),
        (largura, 0),
        (largura, altura),
        (0, altura)
    ]

    # Coordenadas da textura
    uvs = [
        (0, 0),
        (1, 0),
        (1, 1),
        (0, 1)
    ]

    scanline_texture(superficie, pontos, uvs, textura)

def criar_cenario(largura, altura):
    global cenario_surface

    cenario_surface = pygame.Surface((largura, altura)).convert()

    textura = pygame.image.load("texturas/chao_textura.jpg").convert()

    desenhar_fundo_textura(cenario_surface, textura)

    for (x, y) in mesas:
        desenhar_mesa(cenario_surface, x, y)

def desenhar_cenario(tela):
    # "Cola" a imagem na tela
    tela.blit(cenario_surface, (0, 0))