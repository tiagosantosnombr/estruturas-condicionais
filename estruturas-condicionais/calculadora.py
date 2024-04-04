numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
operacao = input('Qual operação deseja realizar (+ - * /)? ')
resultado = 0

if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 - numero2
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    resultado = numero1 / numero2
else:
    operacao = 'erro'

if operacao == 'erro':
    print('Operação inválida.')
else:
    print(numero1, operacao, numero2, '=', resultado)
