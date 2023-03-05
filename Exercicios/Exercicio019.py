from random import choice
a = str(input('Primeiro aluno: '))
b = str(input('Segundo aluno: '))
c = str(input('Terceiro aluno: '))
d = str(input('Quarto aluno: '))
r = choice([a, b, c, d])
print (f'O aluno(a) escolhido foi {r}')