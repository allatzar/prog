'''Camilla = Mariana = Pedro = branco = nulos = voto = conf = 1
while voto != 4321:
    voto = int(input('Digite seu voto:'))
    conf = int(input('Certeza que esse é seu voto. Digite 1 para sim e 0 para nao: '))
    if conf == 1:
        if voto == 14:
            Camilla = Camilla + 1
        elif voto == 24:
            Mariana = Mariana + 1
        elif voto == 34:
            Pedro = Pedro + 1
        elif voto == 0:
            branco = branco + 1
        else:
            nulos = nulos + 1
    elif conf == 0:
        print('Vote novamente')
    else:
        print('Error')
nulos = nulos - 1
print('Camilla ficou com {} votos'.format(Camilla))
print('Mariana ficou com {} votos'.format(Mariana))
print('Pedro ficou com {} votos'.format(Pedro))
print('tivemos tambem {} votos em branco e {} votos nulos'.format(branco, nulos))'''

dic = {14: 0, 24: 0, 34: 0, 0: 0, "nulo": 0}
voto = conf = 1
while voto != 4321:
    voto = int(input('Digite seu voto:'))
    if voto != 4321:
        conf = int(input('Certeza que esse é seu voto. Digite 1 para sim e 0 para nao: '))
        if conf == 1:
            try:
                dic[voto] += 1
            except KeyError:
                dic["nulo"] += 1
        elif conf == 0:
            print('Vote novamente')
        else:
            print('Error')
    else:
        print('FIM DA ELEIÇAO')
print('\nCamilla ficou com {} votos'.format(dic[14]))
print('Mariana ficou com {} votos'.format(dic[24]))
print('Pedro ficou com {} votos'.format(dic[34]))
print(f'tivemos tambem {dic[0]} votos em branco e {dic["nulo"]} votos nulos')