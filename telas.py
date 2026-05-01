import pygame
import sys
from funcoes import *

# 🎨 cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AZUL = (20, 40, 120)
VERMELHO = (180, 0, 0)

# Imagem oara Textura
textura_fundo = pygame.image.load("texturas/Doguinho.jpeg")

def desenhar_texto(tela, texto, x, y, tamanho=36):
    fonte = pygame.font.SysFont(None, tamanho)
    img = fonte.render(texto, True, BRANCO)
    tela.blit(img, (x, y))

# Função para Textura no fundo
def desenhar_fundo_textura(tela, largura, altura):
    pontos = [
        (0, 0),
        (largura, 0),
        (largura, altura),
        (0, altura)
    ]

    uvs = [
        (0, 0),
        (1, 0),
        (1, 1),
        (0, 1)
    ]

    scanline_texture(tela, pontos, uvs, textura_fundo)

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

        desenhar_fundo_textura(tela, largura, altura)

        texto = "PAC DOG ADVENTURES"

        surf_titulo = fonte_titulo.render(texto, True, AZUL)
        surf_outline = fonte_titulo.render(texto, True, PRETO)

        titulo_x = largura // 2 - surf_titulo.get_width() // 2
        titulo_y = altura // 3 - surf_titulo.get_height() // 2

        offsets = [
            (-3, 0), (3, 0),
            (0, -3), (0, 3),
            (-3, -3), (3, 3),
            (-3, 3), (3, -3)
        ]

        for ox, oy in offsets:
            tela.blit(surf_outline, (titulo_x + ox, titulo_y + oy))

        tela.blit(surf_titulo, (titulo_x, titulo_y))

        # Retangulo ENTER
        bx1, by1 = largura // 2 - 200, altura // 2 + 50

        pontos_enter = [
            (bx1, by1),
            (bx1 + 400, by1),
            (bx1 + 400, by1 + 60),
            (bx1, by1 + 60)
        ]

        scanline_fill(tela, pontos_enter, VERMELHO)
        desenhar_poligono(tela, pontos_enter, BRANCO)

        texto_enter = fonte_botao.render("APERTE ENTER PARA COMECAR", True,BRANCO)

        tela.blit(
            texto_enter,
            (
                largura // 2 - texto_enter.get_width() // 2,
                by1 + 30 - texto_enter.get_height() // 2
            )
        )

        # Retangulo ESC
        bx2, by2 = largura // 2 - 200, altura // 2 + 130

        pontos_esc = [
            (bx2, by2),
            (bx2 + 400, by2),
            (bx2 + 400, by2 + 60),
            (bx2, by2 + 60)
        ]

        scanline_fill(tela, pontos_esc, VERMELHO)
        desenhar_poligono(tela, pontos_esc, BRANCO)

        texto_esc = fonte_botao.render("APERTE ESC PARA SAIR", True,BRANCO)

        tela.blit(
            texto_esc,
            (
                largura // 2 - texto_esc.get_width() // 2,
                by2 + 30 - texto_esc.get_height() // 2
            )
        )

        pygame.display.flip()


# Tela de Game Over
def tela_game_over(tela, largura, altura, pontos):
    clock = pygame.time.Clock()

    # Fontes menores
    fonte_titulo = pygame.font.SysFont("Arial", 70, bold=True)
    fonte_texto = pygame.font.SysFont("Arial", 32)
    fonte_pontos = pygame.font.SysFont("Arial", 40)

    while True:
        clock.tick(60)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    return

        tela.fill(PRETO)

        # Elipse
        cx = largura // 2
        cy = altura // 4

        pontos_elipse = gerar_elipse(cx, cy, 240, 90, 120)

        desenhar_poligono(tela, pontos_elipse, BRANCO)

        flood_fill_iterativo(tela, cx, cy, VERMELHO, BRANCO)

        texto = "GAME OVER"

        surf_titulo = fonte_titulo.render(texto, True, BRANCO)

        surf_outline = fonte_titulo.render(texto, True, PRETO)

        x = largura // 2 - surf_titulo.get_width() // 2
        y = cy - surf_titulo.get_height() // 2

        offsets = [
            (-3, 0), (3, 0),
            (0, -3), (0, 3),
            (-3, -3), (3, 3),
            (-3, 3), (3, -3)
        ]

        for ox, oy in offsets:
            tela.blit(
                surf_outline,
                (x + ox, y + oy)
            )

        tela.blit(surf_titulo, (x, y))

        # Circulo
        cx_pontos = largura // 2
        cy_pontos = altura // 2 - 10

        pontos_circulo = gerar_elipse(cx_pontos, cy_pontos, 55, 55, 100)

        desenhar_poligono(tela, pontos_circulo, BRANCO)

        flood_fill_iterativo(tela, cx_pontos, cy_pontos, AZUL, BRANCO)

        # Pontuação
        texto_pontos = f"{pontos}"

        surf_pontos = fonte_pontos.render(texto_pontos, True, BRANCO)

        tela.blit(
            surf_pontos,
            (
                largura // 2 - surf_pontos.get_width() // 2,
                cy_pontos - surf_pontos.get_height() // 2
            )
        )

        # Retangulo
        bx = largura // 2 - 250
        by = altura - 200
        bw = 500
        bh = 70

        pontos_botao = [
            (bx, by),
            (bx + bw, by),
            (bx + bw, by + bh),
            (bx, by + bh)
        ]

        desenhar_poligono(tela, pontos_botao, BRANCO)

        flood_fill_iterativo(tela, bx + 5, by + 5, VERMELHO, BRANCO)

        # Recomeçar
        texto_restart = "APERTE R PARA RECOMECAR"

        surf_restart = fonte_texto.render(texto_restart,True, BRANCO)

        tela.blit(
            surf_restart,
            (
                largura // 2 - surf_restart.get_width() // 2,
                by + bh // 2 - surf_restart.get_height() // 2
            )
        )

        pygame.display.flip()