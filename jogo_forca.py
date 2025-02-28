import random

pessoas = ['Eduardo', 'Julianna', 'Laura', 'Alice','Isis','Vera','Assis','Carlos','Marcia','Elaine','Karol', 'Levi', 'Elissa','Lucas']
pessoa_sorteada = random.choice(pessoas)
total_letras_pessoa_sorteada = len(pessoa_sorteada)
pessoa_escondida = "-"*total_letras_pessoa_sorteada

letras_sorteadas = []
max_tentativas = 6

while True:
    print(f"A Palavra possui ({total_letras_pessoa_sorteada}) letras: {pessoa_escondida}")
    letra = input('Digite uma letra: ')

    if letra in letras_sorteadas:
        print('Você já escolheu essa letras antes. tente outra!')
        continue
    
    letras_sorteadas.append(letra)

    if letra in pessoa_sorteada:
        lista= []
        for indice in range(len(pessoa_sorteada)):
            if letra == pessoa_sorteada[indice]:
                lista.append(letra)
            else:
                lista.append(pessoa_escondida[indice])
        pessoa_escondida = ''.join(lista)
    else: 
        max_tentativas -= 1
        print(f'Letra não encontrada. Você tem mais {max_tentativas} tentativas.')
    
    if pessoa_escondida == pessoa_sorteada:
        print(f'Parabéns!! a palavra é {pessoa_escondida}' )
        break
    elif max_tentativas == 0:
        print("Quantidade de tentativas esgotadas. Você perdeu!")
        break
