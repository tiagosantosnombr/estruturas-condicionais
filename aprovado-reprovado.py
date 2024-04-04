print('Digite as quatro notas bimestrais da disciplina:')

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
nota4 = float(input('Nota 4: '))
faltas = int(input('Digite o número de faltas: '))
media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'A média anual é {media}.')

presenca = 100 - (faltas * 100) / 40

print(f'Sua porcentagem de presença é {presenca}.')

if media >= 7 and presenca >= 75:
    print("Você está aprovado na disciplina.")
elif media >= 7 and presenca < 75:
    print("Você foi reprovado por faltas.")
elif media <=7 and presenca >= 75:
    print("Você foi reprovado por nota.")
else:
    print("Você foi reprovado por nota e por faltas.")
