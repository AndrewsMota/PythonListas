Questão 1

cod = []#CÓDIGO
titl = []#TÍTULO
qntd = []#QUANTIDADE
mat = []#MATRÍCULA
emp = []#EMPRÉSTIMO
livr = []#LIVRO
solic = []#SOLICITAÇÃO

while True:
    print('[1] Cadastrar exemplar')
    print('[2] Registrar empréstimo')
    print('[3] Emitir relatório de empréstimos')
    print('[4] Indicar livro mais solicitado')
    print('[5] Indicar livro menos solicitado')
    print('[6] Indicar livros não solicitados')

    menu = int(input())

    if (menu == 1):
        code = input('Insira o código do livro: ')
        if (code in cod):
            pos = cod.index(code)
            qntd[pos] = int(qntd[pos]) + int(input(
                f'O livro {titl[pos]} já consta no sistema! Quantas cópias deseja adicionar? '))
        else:
            cod.append(code)
            titl.append(input('Insira o título do livro: '))
            solic.append(0)
            qntd.append(input('Insira a quantidade de livros: '))

    elif (menu == 2):
        code = int(input('Insira a matrícula do aluno: '))
        if code in mat:
            pos = mat.index(code)
            a = emp[pos]
            print(f'O aluno possui os livros {a} emprestados.')
            qtd=0
            while qtd<1 or qtd>3:
                b = int(input('Quantos livros a serem emprestados? '))
                qtd = len(a) + b
                if b == 0:
                    break
                if qtd > 3:
                    print('Quantidade de livros excedida! informe um valor válido ou digite-0 para cancelar!')
                if b != 0:
                    i = 1
                    while i<=b:
                        code2 = input(f'Insira o código do {i}° livro a ser emprestado: ')
                        if (code2 in cod):
                            pos2 = cod.index(code2)
                            qtd2 = qntd[pos2]
                            if int(qtd2) > 0:
                                a.append(code2)
                                i = i+1
                                qntd[pos2] = int(qtd2) - 1
                                solic[pos2] = int(solic[pos2]) + 1
                            else:
                                print('Livro não disponível. Digite-1 para continuar ou 0 para cancelar.')
                                if int(input()) == 0:
                                    break
                        else:
                            print ('Livro não disponível. Digite-1 para continuar ou 0 para cancelar.')
                            if int(input()) == 0:
                                break
                emp[pos] = a

        else:
            mat.append(code)
            b=0
            while b<1 or b>3:
                b = int(input('Quantos livros a serem emprestados? '))
            i = 1
            a = []
            while i <= b:
                code2 = input(f'Insira o código do {i}° livro a ser emprestado: ')
                if (code2 in cod):
                    pos2 = cod.index(code2)
                    qtd2 = qntd[pos2]
                    if int(qtd2) > 0:
                        a.append(code2)
                        i = i+1
                        qntd[pos2] = int(qtd2) - 1
                        solic[pos2] = int(solic[pos2]) + 1
                    else:
                        print('Livro não disponível. Digite 1 para tentar novamente ou 0 para cancelar.')
                        if int(input()) == 0:
                            break
                else:
                    print('Livro não disponível. Digite 1 para tentar novamente ou 0 para cancelar.')
                    if int(input()) == 0:
                        break
            emp.append(a)

    elif (menu == 3):
        qtd_a = len(mat)
        print('\033[1m' + ('\nMATRÍCULA' + ('QUANTIDADE DE LIVROS').rjust(29," ") + '\033[0m'))
        i = 0
        soma = 0
        while i < qtd_a:
            a = emp[i]
            print((f'{mat[i]}') + (f'{len(a)}').rjust(22, " "))
            soma = soma + len(a)
            i = i+1
        print('-------------------------------------------------')
        print(f'TOTAL = {soma} QUANTIDADE DE LIVROS.')
        print('-------------------------------------------------')

    elif (menu == 4):
        max = int(max(solic))
        i = 0
        print('Os livros mais solicitados são:')
        for i in range(len(solic)):
            if max == solic[i]:
                print(titl[i])

    elif (menu == 5):
        min = int(min(solic))
        i = 0
        print('Os livros menos solicitados são:')
        for i in range(len(solic)):
            if min == solic[i]:
                print(titl[i])

    elif (menu == 6):
        i = 0
        print('Os livros não solicitados são:')
        for i in range(len(solic)):
            if solic[i] == 0:
                print(titl[i])


Questão 2

cadh=[]#Candidatos
cadm=[]#Canditadas
cadhxp=[]#Candidatos com experiencia
cadhxp1=[]#Relação dos candidatos > 40 sem experiencia
cadmxp=[]#Relação das candidatas com experiencia
while True:
    insc=int(input('Informe o número de inscrição'))
    if insc <= -1:
        break
    nome = str(input("Informe o nome do candidato"))
    idd = int(input('Informe a idade do candidato '))
    gen = int(input('Informe o gênero do candidato, 1-Masculino/2-Feminino'))
    exp = int(input('Informe a experiencia do candidato, 1-Sim/0-Não'))
    if gen == 1:
        cadh.append(1)
    if gen == 2:
        cadm.append(1)
    if gen == 1 and exp == 1:
        cadhxp.append(idd)
    if idd > 40 and gen == 1 and exp == 0:
        cadhxp1.append(nome)
        cadhxp1.append(idd)
    if gen == 2 and exp == 1:
        cadmxp.append(nome)


print(f'O número de candidados do sexo masculino é: {len(cadh)} e do sexo feminino é: {len(cadm)} ')
if len(cadhxp) == 0:
    print('Nenhum homem possui experiencia')
else:
    print(f'A idade média dos homens que possuem experiência é: {(sum(cadhxp))/len(cadhxp)}')
print(f'Relação dos homens com mais de 40 anos que não possuem experiencia: {cadhxp1}')
print(f'Relação das mulheres que possuem experiencia: {cadmxp}')