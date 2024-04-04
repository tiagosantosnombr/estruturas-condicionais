salario = float(input('Digite o valor do seu salário: '))
abono = 0

if salario < 500:
    abono = 5000 * 0.15
else:
    abono = 5000 * 0.1

print(f'Valor do seu abono de fim de ano: R$ {abono:.2f}.')
