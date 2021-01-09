Questão 1

cod = []#Código e título
cod1 = []#Matrícula e quantidade
op = 0
cont = 0
quo = 0
lista_livro = []
lista_cod = []
lista1 = lista_livro 
while op != 7 :
    print('''    [ 1 ]Cadastrar exemplar
    [ 2 ]Registar empréstimo
    [ 3 ]Emitir relatório de empréstimos
    [ 4 ]Indicar livro mais solicitado
    [ 5 ]Indicar livro menos solicitado
    [ 6 ]Indicar livros não solicitados
    [ 7 ]Finalizar programa''')
    op = int(input('Selecione a opção desejada: '))
    if op == 1:
        codi = int(input('Informe o código do livro: '))
        titl = str(input('Informe o título do livro: '))
        qntd = int(input('Informe a quantidade de exemplares disponíveis: '))
        if op == 1:
            cod.append(codi)
            while len(cod) < qntd:
                cod.append(codi)
            cod.append(titl)
            cont+=1
            lista_livro.append(titl)
            lista_cod.append(codi)
            print(cod)
            print(lista1)
    elif op == 2:
        mat = int(input('Informe a matrícula'))
        cod2 = int(input('Informe o código do livro'))
        qtd = int(input('Informe a quantidade de exemplares até um limite de 3: '))
        if qtd > 3:
            print('Número de livros solicitados é inválido, porfavor, digite um valor válido.')
        if qtd > len(cod)-cont:
            print(f' A quantidade atual do livro requisitado é: {len(cod)-cont} livro(s), porfavor, digite um valor válido.')
        if cod.count(cod2)< qtd:
            print(f'A quantidade atual do livro requisitado é: {cod.count(cod2)} livro(s), porfavor, digite um valor válido.')
        elif cod2 in cod[:]:
            quo+=qtd
            while cod2 in cod[:] and  quo > 0:
                cod.pop(cod2)
                quo-=1
            cod1.append(mat)
            cod1.append(qtd)
            print(cod)
        else:
            print('Código inválido !')

    elif op == 3:
        print(f'Matrículas:\n{cod1[0::2]}')
        print(f'Exemplares: \n{cod1[1::2]}')
        print(f'Total de exemplares emprestados: {sum(cod1[1::2])}')




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
