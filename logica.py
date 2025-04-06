# 1º Desafio (Volei)

saque = input('Conseguiu sacar? ')

if saque == 'sim':

    saque_passou_da_rede = input('Ultrapassou a rede? ')
    if saque_passou_da_rede == 'sim':
        saque_passou_da_rede = True

        defesa_do_saque = input('Defendeu o saque? ')
        if defesa_do_saque == 'nao':
            defesa_do_saque = False

        if saque_passou_da_rede and defesa_do_saque:
            print('Continua o jogo')
        elif saque_passou_da_rede and not defesa_do_saque:
            print('+1 pontos pro time, sacar novamente')
    else:
        saque_passou_da_rede = False
        print('O saque não passou da rede, +1 ponto pro time adversario')

else:
    print('+1 ponto pro adversario, saque falhado')

# 2º Desafio (Basquete)

arremessar = input ('Quer arremesar? ')

if arremessar == 'sim':
    errou_arremesso = input('Errou? ')
    if errou_arremesso == 'sim':
        errou_arremesso = True

        rebote = input('Conseguiu o rebote ')
        if rebote == 'nao':
            rebote = False

        if errou_arremesso and rebote:
            print('Continua o jogo')
        elif errou_arremesso and not rebote:
            print('posse de bola do adversario')
    else:
        errou_arremesso = False
        print('+3 pontos pro time')

else:
    print('Passa a bola')


# 3º Desafio (Estudar)

estudar = input('Você ira estudar? ')

if estudar == 'sim':
    horario = input('Em qual horario? ')
    lugar = input('Em que lugar? ')

    if lugar == 'casa':
        lugar = True
    else:
        lugar = False
    
    if horario and lugar:
        print(f'Bons estudos a {horario}h em casa')
    elif horario and not lugar:
        print('É melhor estudar em casa')
    else:
        print('Procure estudar em casa num bom horario')
else:
    print('Va descansar')


# 4º Desafio (War)

atacar = input('Voce vai atacar? ')

if atacar == 'sim':
    forma_de_ataque = input('Como ira atacar? ')
    if forma_de_ataque == 'terrestre':
        forma_de_ataque = True
    else:
        forma_de_ataque = False

    condicoes = input('Tem condições? ')
    if condicoes == 'nao':
        condicoes = False

    if forma_de_ataque and condicoes:
        print('Ataque realizado com sucesso')
    elif forma_de_ataque and not condicoes:
        print('Melhor pegar recursos antes')
    else:
        print('Procure uma melhor forma de atacar e recursos')
else:
    print('Recue')

# 5º Desafio (Banco Imobiliario)

comprar = input('Voce ira comprar ? ')

if comprar == 'sim':
    item = input('O que deseja? ')
    onde = input('Onde comprar')

    if onde == 'Casas Bahia':
        onde = True
    else: 
        onde = False
    
    if item and onde:
        print('Pode ir la comprar')
    elif item and not onde:
        print('Não esta disponivel nesse local')
    else:
        print('Não há esse item em nenhuma loja')
else:
    print('Economize então')


# 6º Desafio (Biblia)

ajudar = input('Ajudar a pessoa? ')

if ajudar == 'sim':
    forma_de_ajuda = input('O que a pessoa precisa? ')
    if forma_de_ajuda == 'saude':
        forma_de_ajuda = True
    else:
        forma_de_ajuda = False

    dinheiro = input('Voce pode pagar consulta? ')
    if dinheiro == 'sim':
        dinheiro = True
    else:
        dinheiro = False

    if forma_de_ajuda and dinheiro:
        print('Voce conseguiu ajuda-la')
    elif forma_de_ajuda and not dinheiro:
        print('Não há dinheiro suficiente para ajudar')
    else:
        print('Ela nao precisa de ajuda')
else:
    print('Voce é uma pessoa ruim')