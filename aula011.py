
'''

        codigo de cores # \033[style;text;backm #


style(estilo)     |  text(texto)      |  back(fundo)
 0 (padrao)       |  30 (branco)      |  40 (branco)
 1 (negrito)      |  31 (vermelho)    |  41 (vermelho)
 4 (sublinhado)   |  32 (verde)       |  42 (verde)
 7 (oposto)       |  33 (amarelo)     |  43 (amarelo)
                  |  34 (azul)        |  44 (azul)
                  |  35 (roxo)        |  45 (roxo)
                  |  36 (siano)       |  46 (siano)
                  |  37 (cinza)       |  47 (cinza)

'''

'pretoebranco'
nome = 'mauro'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}


 nome = 'mauro'
 print('ola ! meu nome é, {}{}{}!!!'.format(cores['azul'], nome,cores['limpa']))