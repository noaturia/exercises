from random import randint
conputador = randint(0, 5) 
print('--' * 20)
print('eu vou pensar em um numero entre 1 e 5 temte adivinhar...')
print('--' * 20)
jogador = int(input("en que numero eu pensei?"))
if jogador == conputador:
    print('PARABENS! vc conseguiu me vanser')
else:
    print('GANHEI! eu pensei no numero {} e nono {}!'.format(conputador, jogador))