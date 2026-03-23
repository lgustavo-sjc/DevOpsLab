nome = 'Luis Gustavo'
altura = 1.67
peso = 110
imc = peso / (altura * altura)
imc = peso / (altura ** 2)
print2 = f'{nome} tem {altura} de altura pesa {peso:.2f} quilos e seu IMC é {imc:.2f}'

print(nome, 'tem', altura, 'de altura, pesa', peso, 'quilos e seu IMC é',imc )
print(f'{nome} tem altura de altura pesa peso quilos e seu IMC é {imc:,.2f}')
print(print2)