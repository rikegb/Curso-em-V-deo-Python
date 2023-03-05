largura = float(input('Qual é a largura da parede em metros? '))
altura = float(input('Qual é altura da parede em metros? '))
tinta = float(input('Com 1 litro de tinta da para pintar quantos m²? '))
area = largura * altura
calculo = area / tinta
print('É necesario {} litros de tinta para pintar o cômodo'.format(calculo))