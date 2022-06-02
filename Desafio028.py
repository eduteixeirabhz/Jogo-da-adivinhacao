from random import randint #randomiza
from time import sleep  # pausa entre ações
computador = randint(0, 5)  # faz o computador 'pensar'
print('-=-' * 20)
print('Estou pensando em um número entre 0 e 5 , tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))  # jogador tenta adivinhar
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabéns, você conseguiu me vencer! ')
else:
    print('GANHEI! Eu pensei no  número {} e não no {} !'.format(computador, jogador))
