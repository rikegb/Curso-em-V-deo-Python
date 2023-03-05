p = float(input('Preço do produto: '))
d = int(input('Quantos porcento de desconto? '))
desconto = d / 100
calculo = p * desconto
calculof = p - calculo
print('O produto custará R${:.2f} '.format(calculof))
