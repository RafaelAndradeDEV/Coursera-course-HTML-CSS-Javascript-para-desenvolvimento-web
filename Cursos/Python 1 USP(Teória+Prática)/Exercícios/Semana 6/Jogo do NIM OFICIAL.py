

def partida():
    print('Bem - vindo ao jogo do NIM! Escolha:')

    jogo = int(input('\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato'))

    if jogo == 2:
        print('\nVocê escolheu um campeonato!')
    if jogo == 1:
        print('\nVocê escolheu uma partida isolada!')

    n = int(input('\nQuantas peças?'))
    m = int(input('Limite de peças por jogada?'))
    if n < 1 or m < 1:
        print('Erro... Defina novamente as peças e lista_inversa quantidade lista_inversa ser tirada...')
        n = int(input('Quantas peças?'))
        m = int(input('Limite de peças por jogada?'))
    if m > n:
        print('Erro... Defina novamente as peças e lista_inversa quantidade lista_inversa ser tirada...')
        n = int(input('Quantas peças?'))
        m = int(input('Limite de peças por jogada?'))

    respostas = str
    i = 0
    valor = 1
    variavel = 1
    if m <= n and m >= 1:
        while i <= m > 0:
            while i < 100 and respostas != '\nVocê começa!':
                i = i + 1
                if n == (m + 1) * i:
                    respostas = '\nVocê começa!'
                    print(respostas)
                    valor = (m + 1) * i
                    variavel = valor
            if n != (m + 1) * i:
                respostas = '\nComputador começa!'
                print(respostas)
                valor = (m + 1) * i
                variavel = valor
            i = m + 1
        while m > n and m < 1:
            print('Erro... Defina novamente as peças e lista_inversa quantidade lista_inversa ser tirada...')
            n = int(input('Quantas peças?'))
            m = int(input('Limite de peças por jogada?'))

    variavel = int(variavel)

    def usuario_escolhe_jogada(n, m):
        i = 0
        x = 1
        x = int(input('Quantas peças você vai tirar?'))
        while x <= 0:
            print('Erro... Coloque um valor correto')
            x = int(input('Quantas peças você vai tirar?'))
        while x > m:
            print('Erro... Coloque um valor correto')
            x = int(input('Quantas peças você vai tirar?'))

        respostas = str
        saida = 1
        a = 1
        n = n - x
        if n == 0:
            while saida != 0:
                if n != 1:
                    print('Voce tirou {} peças.'.format(x))
                if n == 1:
                    print('Voce computador tirou {} peça.'.format('uma'))
                saida = 0
            print('Fim do jogo! Você ganhou!')
            respostas = 'Legal'
        if n != 0:
            if n == 1 and x != 1:
                print('\nVoce tirou {} peças.\nAgora resta {} peça no tabuleiro.\n'.format(x, 'uma'))
            if x == 1 and n != 1:
                print('\nVoce tirou {} peça.\nAgora restam {} peças no tabuleiro.\n'.format('uma', n))
            if x == 1 and n == 1:
                print('\nVoce tirou {} peça.\nAgora resta {} peça no tabuleiro.\n'.format('uma', 'uma'))
            if x != 1 and n != 1:
                print('\nVoce tirou {} peça.\nAgora resta {} peça no tabuleiro.\n'.format(x, n))
            respostas = '\nComputador começa!'
            while n != 0:
                computador_escolhe_jogada(n, m)
        if respostas == '\nVocê começa!':
            if n != 0:
                usuario_escolhe_jogada(n, m)

    def computador_escolhe_jogada(n, m):
        saida = 1
        variavel2 = int(1)
        respostas = str
        if n <= m:
            variavel2 = n
            n = n - variavel2
        if n > m:
            if n != (m + 1):
                variavel2 = m
            n = n - variavel2
        if n == 0:
            while respostas != 'Legal':
                if variavel2 != 1:
                    print('O computador tirou {} peças.'.format(variavel2))
                if variavel2 == 1:
                    print('O computador tirou {} peça.'.format('uma'))
                respostas = 'Legal'
                print('Fim do jogo! O computador ganhou!')
        if n != 0:
            while saida != 0:
                if n == 1 and variavel2 != 1:
                    print('O computador tirou {} peças.\nAgora resta {} peça no tabuleiro.\n'.format(variavel2, 'uma'))
                if variavel2 == 1 and n != 1:
                    print('O computador tirou {} peça.\nAgora restam {} peças no tabuleiro.\n'.format('uma', n))
                if variavel2 == 1 and n == 1:
                    print('O computador tirou {} peça.\nAgora resta {} peça no tabuleiro.\n'.format('uma', 'uma'))
                if variavel2 != 1 and n != 1:
                    print('\nO computador tirou {} peça.\nAgora resta {} peça no tabuleiro.\n'.format(variavel2, n))
                saida = 0
                respostas = '\nVocê começa!'
        while n != 0:
            usuario_escolhe_jogada(n, m)
    if respostas == '\nComputador começa!':
        if n != 0:
            computador_escolhe_jogada(n, m)


partida()
