'''
       segundo mundo de python

               estruturas de controle

    condições aninhadas
  if
  elif
  elif
  else

'''

nome = str(input('qual é o seu nome ? '))
if nome == 'joao victor':
    print(' fala piroca xoxa do papai !')
elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print('seu nome é bem popular no Brasil')
elif nome in 'ana claudia joana juliana':
    print('seu nome e popular')
else:
    print('seu nome é bem normal,')
print('tenha um bom dia, \033[1;33m{}\033[m !'.format(nome))
