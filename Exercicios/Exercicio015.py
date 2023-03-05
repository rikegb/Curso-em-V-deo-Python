d = int(input('Quantos dias ficou com o carro? '))
taxa = float(input('Quantos reais por dia com o carro? '))
k = float(input('Quantos km percorrido com o carro? '))
taxak = float(input('Quantos reais por km rodado? '))
cald = d * taxa
calk = k * taxak
total = cald + calk
print('Voce ficou {} dias com o carro que da R${} percorreu {} que da R${} \n VALOR TOTAL R$: {}'.format(d, cald, k, calk, total))
