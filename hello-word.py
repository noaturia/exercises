import random
n1 = str(input('primeiro aluno'))
n2 = str(input('segundo aluno'))
n3 = str(input('terceiro aluno'))
n4 = str(input("quarto aluno"))
lista = [n1, n2, n3, n4]
escolido = random.choice(lista)
print('o aluno escolido foi {}'.format (escolido))