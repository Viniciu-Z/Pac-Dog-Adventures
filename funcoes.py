import math

def setPixel(superficie, x, y, cor):
    if 0 <= x < superficie.get_width() and 0 <= y < superficie.get_height():
        superficie.set_at((x, y), cor)

def bresenham(superficie, x0, y0, x1, y1, cor):
    x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
    # Flags para transformações
    steep = abs(y1 - y0) > abs(x1 - x0)
    if steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1

    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    dx = x1 - x0
    dy = y1 - y0

    ystep = 1
    if dy < 0:
        ystep = -1
        dy = -dy

    # Bresenham clássico
    d = 2 * dy - dx
    incE = 2 * dy
    incNE = 2 * (dy - dx)

    x = x0
    y = y0

    while x <= x1:
        if steep:
            setPixel(superficie, y, x, cor)
        else:
            setPixel(superficie, x, y, cor)

        if d <= 0:
            d += incE
        else:
            d += incNE
            y += ystep

        x += 1

def desenhar_poligono(superficie, pontos, cor_borda):
    n = len(pontos)
    for i in range(n):
        x0, y0 = pontos[i]
        x1, y1 = pontos[(i + 1) % n]
        bresenham(superficie, x0, y0, x1, y1, cor_borda)

def scanline_fill(superficie, pontos, cor):
    # 🔥 garante inteiros
    pontos = [(int(x), int(y)) for (x, y) in pontos]

    ys = [p[1] for p in pontos]
    y_min = int(min(ys))
    y_max = int(max(ys))

    n = len(pontos)

    for y in range(y_min, y_max):
        intersecoes = []

        for i in range(n):
            x0, y0 = pontos[i]
            x1, y1 = pontos[(i + 1) % n]

            if y0 == y1:
                continue

            if y0 > y1:
                x0, y0, x1, y1 = x1, y1, x0, y0

            if y < y0 or y >= y1:
                continue

            x = x0 + (y - y0) * (x1 - x0) / (y1 - y0)
            intersecoes.append(x)

        intersecoes.sort()

        for i in range(0, len(intersecoes), 2):
            if i + 1 < len(intersecoes):
                x_ini = int(intersecoes[i])
                x_fim = int(intersecoes[i + 1])

                for x in range(x_ini, x_fim + 1):
                    setPixel(superficie, x, y, cor)

def gerar_elipse(xc, yc, rx, ry, passos=40):
    pontos = []

    for i in range(passos):
        t = 2 * math.pi * i / passos
        x = xc + rx * math.cos(t)
        y = yc + ry * math.sin(t)
        pontos.append((int(x), int(y)))

    return pontos

def identidade():
    return [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]

def translacao(tx, ty):
    return [
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ]

def escala(sx, sy):
    return [
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ]

def rotacao(theta):
    c = math.cos(theta)
    s = math.sin(theta)
    return [
        [c, -s, 0],
        [s,  c, 0],
        [0,  0, 1]
    ]

def multiplica_matrizes(a, b):
    r = [[0]*3 for _ in range(3)]

    for i in range(3):
        for j in range(3):
            for k in range(3):
                r[i][j] += a[i][k] * b[k][j]

    return r

def cria_transformacao():
    return identidade()

def aplica_transformacao(m, pontos):
    novos = []

    for x, y in pontos:
        v = [x, y, 1]

        x_novo = m[0][0]*v[0] + m[0][1]*v[1] + m[0][2]
        y_novo = m[1][0]*v[0] + m[1][1]*v[1] + m[1][2]

        novos.append((x_novo, y_novo))

    return novos

def janela_viewport(janela, viewport):
    Wxmin, Wymin, Wxmax, Wymax = janela
    Vxmin, Vymin, Vxmax, Vymax = viewport

    sx = (Vxmax - Vxmin) / (Wxmax - Wxmin)
    sy = (Vymin - Vymax) / (Wymax - Wymin)  # inversão do Y

    m = identidade()

    m = multiplica_matrizes(translacao(-Wxmin, -Wymin), m)
    m = multiplica_matrizes(escala(sx, sy), m)
    m = multiplica_matrizes(translacao(Vxmin, Vymax), m)

    return m

def flood_fill_iterativo(superficie, x, y, cor_preenchimento, cor_borda):
    largura = superficie.get_width()
    altura = superficie.get_height()

    pilha = [(x, y)]

    while pilha:
        x, y = pilha.pop()

        if not (0 <= x < largura and 0 <= y < altura):
            continue

        cor_atual = superficie.get_at((x, y))[:3]

        if cor_atual == cor_borda or cor_atual == cor_preenchimento:
            continue

        setPixel(superficie, x, y, cor_preenchimento)

        pilha.append((x + 1, y))
        pilha.append((x - 1, y))
        pilha.append((x, y + 1))
        pilha.append((x, y - 1))