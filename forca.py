import os
import random

def jogar():
    mensagem_inicial()

    palavra_secreta = retorna_palabra_secreta()

    letras_acertadas = ['_' for _ in palavra_secreta]

    # teste para definir tentativas
    if len(palavra_secreta) > 15:
        tentativas = 20
        penalidade = 100 / tentativas
    elif 15 > len(palavra_secreta) > 10:
        tentativas = 10
        penalidade = 100 / tentativas
    else:
        tentativas = 6
        penalidade = 100 / tentativas

    enforcou = False
    acertou = False
    erros = 0
    pontos = 100
    # laço do jogo
    while not enforcou and not acertou:
        # Valor de entrada.
        palpite = palpite_letra(palavra_secreta, tentativas, letras_acertadas)

        # Teste do palpite da letra é correta ou não
        if palpite in palavra_secreta:
            index = 0
            for letra in palavra_secreta:

                if palpite == letra:
                    letras_acertadas[index] = letra
                index += 1

        else:
            erros += 1
            pontos = pontos - penalidade

        if erros == tentativas:
            enforcou = True
            final_de_jogo(palavra_secreta)

        elif '_' not in letras_acertadas:
            acertou = True
            mensagem_acertou(palavra_secreta, pontos)

def palpite_letra(palavra_secreta, tentativas, letras_acertadas):
    tamanho = int(len(palavra_secreta))
    palpite = input('Acerte a palavra para não se inforcar !! \n'
                    f'Você tem {tentativas} tentativas\n'
                    f'A palavra tem {tamanho} letras {letras_acertadas}\n'
                    'Qual a leta desejada chutar ? \n'
                    'Insira aqui: ').upper().strip()
    return palpite

def mensagem_acertou(palavra_secreta, pontos):
    print('\n\bParabens você acertou !\n'
          f'A palavra era ** {palavra_secreta} **\n'
          f'O seu Score foi de {pontos}\n\n')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def final_de_jogo(palavra_secreta):

    print("Fim do jogo")
    print('Se enforcou\n\n'
          '|///-    -\n'
          '|   -   -  -\n'
          '|   -  - x x -\n'
          '|    -  -   -\n'
          '|     -   -'
          '|       -----\n'
          '|         -\n'
          '|    ==========\n'
          '|    |   ||   |\n'
          '|    |   ||   |\n'
          '|    |   ||   |\n'
          '|      ======\n'
          '|      |    |\n'
          '|      |    |\n'
          '|      |    |\n'
          '|      |    |\n'
          '|    ---    ---\n'
          '*** ENFORCADO ***\n'
          f'A palabra secreta era {palavra_secreta}\n')

def mensagem_inicial():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def retorna_palabra_secreta():
    # Escolhendo a palvra ou pegando da base
    escolha = int(input('\n Deseja escolher uma palavra para o jogo ou pegar uma randomica ??\n'
                        'Opção 1 - Inserir a plavra\n'
                        'Opção 2 - Pegar uma palavra randomica\n'
                        '\nQual sua escolha: '))
    if escolha == 1:
        # Inserir palavra pelo usuario
        palavra_secreta = input('\nDigite a palavra desejada para o jogo: ').upper()
        os.system('cls')
        letras_acertadas = ['_' for _ in palavra_secreta]
    elif escolha == 2:
        # Pegando palavra de um arquivo txt
        arquivo = open('opcoes_forca', 'r')
        lista_palavras = []

        for linha in arquivo:
            linha = linha.strip()
            lista_palavras.append(linha)

        arquivo.close()
        indice = random.randrange(0, len(lista_palavras))
        palavra_secreta = lista_palavras[indice].upper()

    return palavra_secreta


if __name__ == "__main__":
    jogar()
