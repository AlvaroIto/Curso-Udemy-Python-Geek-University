import random

naipes = '♠ ♡ ♣ ♢'.split()
cartas = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

def criar_baralho(aleatorio=False):
    """cria um baralho com 52 cartas para jogar"""
    baralho = [(n, c) for c in cartas for n in naipes]
    if aleatorio:
        random.shuffle(baralho)
    return baralho

def distribuir_cartas(baralho):
    """gerencia a mão de cartas de acordo com o baralho gerado"""
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])

def jogar():
    """inicia um jogo de cartas para 4 jogadores"""
    cartas = criar_baralho(aleatorio=True)
    jogadores = 'p1 p2 p3 p4'.split()
    maos = {j: m for j, m in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        carta = ' '.join(f'{j}{c}' for (j, c) in cartas)
        print(f'{jogador}: {carta}')

if __name__ == '__main__':
    jogar()

