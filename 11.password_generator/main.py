def gerandor_de_senha():
    import random
    import time
    
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]
    
    simbolos =['!', '#', '$', '%', '&', '(', ')', '*', '+', '>', '<', '^', '~', '@', '-', '_', 'ç', 'Ç','`', '/', '|', 'ª', 'º', '¿',]
    
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]

    print('******************************')
    print('*** Vamos criar sua senha! ***')
    print('******************************')
    
    quantidade_letras = int(input('Quantas letras você gostaria em sua senha?\n'))
    quantidade_simbolos = int(input('Quantos símbolos você gostaria em sua senha?\n'))
    quantidade_numeros = int(input('Quantos números você gostaria em sua senha?\n'))

    lista_senha = []

    for i in range(1, quantidade_letras + 1):
        lista_senha.append(random.choice(letras))

    for i in range(1, quantidade_simbolos + 1):
        lista_senha += random.choice(simbolos)
    
    for i in range(1, quantidade_numeros + 1):
        lista_senha += random.choice(numeros)

    random.shuffle(lista_senha)

    senha = ''
    for i in lista_senha:
        senha += i

    time.sleep(3)

    print(f'Sua senha é: {senha}')

gerandor_de_senha()