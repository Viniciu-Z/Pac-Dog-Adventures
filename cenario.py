import pygame
from funcoes import *

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (150, 150, 150)

LARGURA_MESA = 400
ALTURA_MESA = 235

MESAS = [
    (70, 70),
    (600, 70),
    (70, 410),
    (600, 410)
]

# Superfície pré-renderizada do cenário
cenario_surface = None

def desenhar_mesa(superficie, x, y):
    pontos = [
        (x, y),
        (x + LARGURA_MESA, y),
        (x + LARGURA_MESA, y + ALTURA_MESA),
        (x, y + ALTURA_MESA)
    ]

    # 🎨 cores por vértice (gradiente)
    cores = [
        (220, 220, 220),  # topo esq
        (220, 220, 220),  # topo dir
        (60, 60, 60),  # base dir
        (60, 60, 60)  # base esq
    ]

    janela = (0, 0, superficie.get_width(), superficie.get_height())

    # 🔥 usa gradiente em vez de cor sólida
    scanline_fill_gradiente(superficie, pontos, cores)

    # borda continua normal
    desenhar_poligono_recortado(superficie, pontos, janela, PRETO)

def desenhar_fundo_textura(superficie, textura):
    largura, altura = superficie.get_width(), superficie.get_height()

    pontos = [
        (0, 0),
        (largura, 0),
        (largura, altura),
        (0, altura)
    ]

    # UV mapeando a imagem inteira
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

    for (x, y) in MESAS:
        desenhar_mesa(cenario_surface, x, y)

def desenhar_cenario(tela):
    tela.blit(cenario_surface, (0, 0))