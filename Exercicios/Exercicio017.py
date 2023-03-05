from math import hypot, sqrt

x = float(input('O comprimento do cateto oposto é ? '))
y = float(input('O comprimento do cateto adjacente é ? '))
# h = sqrt(x * x + y * y)

h2 = hypot(x, y)

print(f'Á hipotenusa do triangulo é igaul á {h2:.2f}')
