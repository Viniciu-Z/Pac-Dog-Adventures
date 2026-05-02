import pygame
import sys
import viewport

from telas import tela_abertura, tela_game_over
from cenario import criar_cenario, desenhar_cenario
from cachorro import desenhar_cachorro, mover
from temporizador import desenhar as desenhar_tempo, atualizar
from alimento import gerar_alimento, desenhar_alimento, colidiu_com_jogador
import pontuacao

PRETO = (0, 0, 0)

pygame.init()

largura, altura = 1080, 720
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pac Dog")

relogio = pygame.time.Clock()

while True:

    # Tela inicial
    tela_abertura(tela, largura, altura)

    # Inicializa pontuação
    pontuacao.resetar()
    pontuacao.iniciar()

    # Cria cenario
    criar_cenario(largura, altura)

    # Gera alimento
    gerar_alimento(largura, altura)

    # Tempo
    tempo_inicial = 50
    tempo_restante = tempo_inicial
    tempo_anterior = pygame.time.get_ticks()
    acabou = False

    rodando = True

    while rodando:
        relogio.tick(60)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        teclas = pygame.key.get_pressed()
        mover(teclas, largura, altura)

        if colidiu_com_jogador():
            pontuacao.adicionar_ponto()
            gerar_alimento(largura, altura)

        # Tempo
        tempo_anterior, tempo_restante, acabou = atualizar(
            tempo_anterior, tempo_restante, acabou
        )

        # Se acabou vai pra tela de game over
        if acabou:
            pontos = pontuacao.pontos
            tela_game_over(tela, largura, altura, pontos)
            rodando = False
            break

        tela.fill(PRETO)

        desenhar_cenario(tela)
        desenhar_alimento(tela)
        desenhar_cachorro(tela)

        pontuacao.desenhar(tela)
        desenhar_tempo(tela, tempo_restante)
        viewport.desenhar_minimapa(tela, largura, altura)

        pygame.display.flip()