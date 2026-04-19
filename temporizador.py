import pygame

pygame.init()

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

tempo_inicial = 50
tempo_restante = tempo_inicial
tempo_anterior = pygame.time.get_ticks()
fonte = pygame.font.SysFont(None, 36)
acabou = False

def atualizar(tempo_anterior, tempo_restante, acabou):
    if acabou:
        return tempo_anterior, tempo_restante, acabou

    tempo_atual = pygame.time.get_ticks()

    # verifica se passou 1 segundo (1000 ms)
    if tempo_atual - tempo_anterior >= 1000:
        tempo_restante -= 1
        tempo_anterior = tempo_atual

        if tempo_restante <= 0:
            tempo_restante = 0
            acabou = True

    return tempo_anterior, tempo_restante, acabou


def desenhar(tela, tempo_restante):
    # muda a cor quando o tempo está acabando
    cor = (255, 0, 0) if tempo_restante <= 10 else PRETO

    texto = fonte.render(f"Tempo: {tempo_restante}", True, cor)
    tela.blit(texto, (900, 10))


def resetar():
    tempo_restante = tempo_inicial
    tempo_anterior = pygame.time.get_ticks()
    acabou = False
    return tempo_anterior, tempo_restante, acabou