print('Informe o tamanho dos três lados de um triângulo:')

lado1 = int(input('Lado 1: '))
lado2 = int(input('Lado 2: '))
lado3 = int(input('Lado 3: '))

if lado1 + lado2 < lado3 or lado2 + lado3 < lado1 or lado3 + lado1 < lado2:
    print('Não é um triângulo.')
else:
    if lado1 == lado2 and lado1 == lado3:
        print('É um triângulo equilátero.')
    elif lado1 == lado2  or lado2 == lado3 or lado3 == lado1:
        print('É um triângulo isósceles.')
    else:
        print('É um triângulo escaleno.')
