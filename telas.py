import pygame
import sys
from funcoes import *

# 🎨 cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AZUL = (20, 40, 120)
VERMELHO = (180, 0, 0)

# Texto Simples
def desenhar_texto(tela, texto, x, y, tamanho=36):
    fonte = pygame.font.SysFont(None, tamanho)
    img = fonte.render(texto, True, BRANCO)
    tela.blit(img, (x, y))

# Retangulo Bresenham
def desenhar_retangulo(tela, x, y, w, h, cor):
    p = [
        (x, y),
        (x + w, y),
        (x + w, y + h),
        (x, y + h)
    ]
    desenhar_poligono(tela, p, cor)

def tela_abertura(tela, largura, altura):
    clock = pygame.time.Clock()

    fonte_titulo = pygame.font.SysFont("Arial", 80, bold=True)
    fonte_botao = pygame.font.SysFont("Arial", 28)

    while True:
        clock.tick(60)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    return
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        tela.fill(PRETO)

        # Titulo
        texto = "PAC DOG ADVENTURES"

        surf_titulo = fonte_titulo.render(texto, True, AZUL)
        surf_outline = fonte_titulo.render(texto, True, PRETO)

        titulo_x = largura // 2 - surf_titulo.get_width() // 2
        titulo_y = altura // 3 - surf_titulo.get_height() // 2

        offsets = [
            (-3, 0), (3, 0), (0, -3), (0, 3),
            (-3, -3), (3, 3), (-3, 3), (3, -3)
        ]

        for ox, oy in offsets:
            tela.blit(surf_outline, (titulo_x + ox, titulo_y + oy))

        tela.blit(surf_titulo, (titulo_x, titulo_y))

        # Botão Enter
        bx1, by1 = largura // 2 - 200, altura // 2 + 50

        desenhar_retangulo(tela, bx1, by1, 400, 60, BRANCO)
        flood_fill_iterativo(tela, bx1 + 5, by1 + 5, VERMELHO, BRANCO)

        texto_enter = fonte_botao.render("APERTE ENTER PARA COMECAR", True, BRANCO)

        tela.blit(
            texto_enter,
            (
                largura // 2 - texto_enter.get_width() // 2,
                by1 + 30 - texto_enter.get_height() // 2
            )
        )

        # Botão ESC
        bx2, by2 = largura // 2 - 200, altura // 2 + 130

        desenhar_retangulo(tela, bx2, by2, 400, 60, BRANCO)
        flood_fill_iterativo(tela, bx2 + 5, by2 + 5, VERMELHO, BRANCO)

        texto_esc = fonte_botao.render("APERTE ESC PARA SAIR", True, BRANCO)

        tela.blit(
            texto_esc,
            (
                largura // 2 - texto_esc.get_width() // 2,
                by2 + 30 - texto_esc.get_height() // 2
            )
        )

        pygame.display.flip()

def tela_game_over(tela, largura, altura, pontos):
    clock = pygame.time.Clock()

    fonte_titulo = pygame.font.SysFont("Arial", 90, bold=True)
    fonte_texto = pygame.font.SysFont("Arial", 40)

    while True:
        clock.tick(60)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    return  # reinicia o jogo

        tela.fill(PRETO)

        # Texto GameOver
        texto = "GAME OVER"

        surf_titulo = fonte_titulo.render(texto, True, VERMELHO)
        surf_outline = fonte_titulo.render(texto, True, PRETO)

        x = largura // 2 - surf_titulo.get_width() // 2
        y = altura // 3 - surf_titulo.get_height() // 2

        offsets = [
            (-4, 0), (4, 0), (0, -4), (0, 4),
            (-4, -4), (4, 4), (-4, 4), (4, -4)
        ]

        for ox, oy in offsets:
            tela.blit(surf_outline, (x + ox, y + oy))

        tela.blit(surf_titulo, (x, y))

        # Pontuação
        texto_pontos = f"PONTOS: {pontos}"
        surf_pontos = fonte_texto.render(texto_pontos, True, BRANCO)

        tela.blit(
            surf_pontos,
            (
                largura // 2 - surf_pontos.get_width() // 2,
                altura // 2
            )
        )

        # Retry
        texto_restart = "APERTE R PARA RECOMECAR"
        surf_restart = fonte_texto.render(texto_restart, True, BRANCO)

        tela.blit(
            surf_restart,
            (
                largura // 2 - surf_restart.get_width() // 2,
                altura // 2 + 80
            )
        )

        pygame.display.flip()