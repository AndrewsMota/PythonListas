time = []
tecnico = []
pontos = []
vitoria = []
campeao = []
rebaixado = []
torneioanterior = []
maior = []
while True:
    print('''
    [1] Cadastrar Time
    [2] Cadastrar Jogo
    [3] Exibir Classificação
    [4] Exibir Time Campeão
    [5] Exibir time Rebaixado
    [6] Encerrar Campeonato ''')
    menu = int(input(' Informe a opção desejada:  '))
    if menu <1 or menu > 6:
        print('\nOpção inválida, Digite uma opção válida!')

    elif menu == 1:
        time1 = int(input('\nInforme a classificação do seu time no torneio anterior: '))
        if time1 > 8 or time1 < 1:
            print('\nSinto muito ! seu time não atende aos critérios de participação do torneio !')

        elif time1 in torneioanterior:
            print('\nClassificação já cadastrada no sistema, Insira uma classificação válida !')

        elif len(time) <= 8:
            team = str.capitalize(input('Informe o nome do time: '))
            if team in time:
                print('\nTime já cadastrado! porfavor reinicie o cadastro!')
            else:
                time.append(team)
                pos = time.index(team)
                tecnico.append(input('Informe o nome do técnico: '))
                torneioanterior.append(time1)
                pontos.append(0)
                vitoria.append(0)

    elif menu == 2:
        time1 = str.capitalize(input('Insira o nome do primeiro time: '))
        time2 = str.capitalize(input('Insira o nome do segundo time: '))

        if time1 and time2 not in time:
            print(f'\nNenhum dos times está cadastrado no torneio, reinicie o processo')

        elif time1 not in time:
            print(f'O time {time1} não está cadastrado no torneio, porfavor, reinicie o cadastro do jogo')
        elif time2 not in time:
            print(f'O time {time2} não está cadastrado no torneio, porfavor, reinicie o cadastro do jogo')
        else:
            placar1 = int(input(f'Informe o placar do {time1} '))
            placar2 = int(input(f'Informe o placar do {time2} '))
            if time1 in time and time2 in time:
                pos1 = time.index(time1)
                pos2 = time.index(time2)


            if placar1 > placar2:
                pontos[pos1] +=3
                vitoria[pos1] +=1

            elif placar1 < placar2:
                pontos[pos2] +=3
                vitoria[pos2] +=1

            else:
                pontos[pos1] = int(pontos[pos1])+1
                pontos[pos2] = int(pontos[pos2])+1

    elif menu == 3:
        qtd_a = len(time)
        print('\033[1m' + ('\nTimes' + ('Pontos').rjust(20," ") + '\033[0m'))
        i = 0
        soma = 0
        while i < qtd_a:
            a = pontos[i]
            print((f'{time[i]}') + (f'{(pontos[i])}').rjust(22," "))
            soma = soma + len(pontos)
            i = i+1

    elif menu == 4:
        maxi = int(max(pontos))
        maior = pontos.copy()
        i = 0
        f = 0
        soma = sum(pontos)
        while maxi in maior:
            maior.remove(maxi)
            f+=1

        if f != 1:
            maior.clear()
            f-=f
            print('Existem times empatados na primeira posição! faça um rematch entre os times empatados!')

        else:
            for i in range(len(pontos)):
                if maxi == pontos[i]:
                    print(f'{time[i]} é o  Campeão! com {pontos[i]} pontos ' )
                    print(f'Técnico: {tecnico[i]}')
                    print(f'Percentual de pontos: {(pontos[i]/soma)*100}%')

    elif menu == 5:
        mini = int(min(pontos))
        menor = pontos.copy()
        i = 0
        f = 0
        soma = sum(pontos)
        while mini in menor:
            menor.remove(mini)
            f+=1

        if f != 1:
            menor.clear()
            f-=f
            print('Existem times empatados na ultima posição! faça um rematch entre os times empatados!')

        else:
            for i in range(len(pontos)):
                if mini == pontos[i]:
                    print(f'{time[i]} foi rebaixado ! com {pontos[i]} pontos! ')
                    print(f'Técnico: {tecnico[i]}')
                    print(f'Percentual de pontos: {(pontos[i]/soma)*100}%')

    elif menu == 6:
        qtd_a = len(time)
        print('\033[1m' + ('\nTimes' + ('Pontos').rjust(20, " ") + '\033[0m'))
        i = 0
        soma = 0
        while i < qtd_a:
            a = pontos[i]
            print((f'{time[i]}') + (f'{(pontos[i])}').rjust(22, " "))
            soma = soma + len(pontos)
            i = i + 1
        else: break




