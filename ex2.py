print('Média')

nota1 = float(input('Insira sua nota'))
nota2 = float(input('Insira sua nota'))

media = (nota1 + nota2)/2

if media >= 9 and media <= 10:
    print('Aprovado, conceito A')
elif media >= 7.5 and media <= 8.9:
    print('Aprovado, conceito B')
elif media >= 6 and media <= 7.4:
    print('Aprovado, conceito C')
elif media >= 4 and media <= 5.9:
    print('Reprovado, conceito D')
else: 
    print('Reprovado, conceito E')