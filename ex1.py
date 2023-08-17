print('Programa farmácia')

salarioAntigo = float(input('Informe salário'))

print(salarioAntigo)

if salarioAntigo <= 280:
    percentual = 20
elif salarioAntigo >= 281 and salarioAntigo <= 700: 
    percentual = 15
elif salarioAntigo >= 701 and salarioAntigo <= 1500: 
    percentual = 10
else:
    percentual = 5

percentual = percentual/100.0
aumento = percentual * salarioAntigo
salarioAtual = salarioAntigo + aumento


print('Salário antigo', salarioAntigo)
print('Percentual', percentual)
print('Aumento', aumento)
print('Salário atual', salarioAtual)