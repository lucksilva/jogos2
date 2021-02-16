def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False
    index = 0

    while not enforcou and not acertou:
        #Valor de entrada.
        palpite = input('Qual a leta desejada? \n'
                        'Insira aqui: ').lower()

        print('jogando ...')

        for letra in palavra_secreta:

            if(palpite == letra):
                print(f'Encontrei a letra {letra} na posição {index}')
            index = index + 1

    print("Fim do jogo")


if(__name__ == "__main__"):
    jogar()
