from math import cos, sin, tan ,radians

num = float(input('Digite um angulo qualquer: '))
# O valor vem em radianos então é necessario converter
num2 = radians(num)
c = cos(num2)
s = sin(num2)
t = tan(num2)
print(f'Coseno de {num} = {c:.2f} \nSeno de {num} = {s:.2f} \nTangente de {num} = {t:.2f} ')
