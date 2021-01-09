cand1=str(input("informe o nome do  candidato 1: "))
cand2=str(input("informe o nome do  candidato 2: "))
cand3=str(input("informe o nome do  candidato 3: "))
cand4=str(input("informe o nome do  candidato 4: "))

c1=c2=c3=c4=int(0)#quantidade de votos
nulo=int(0)
branco=int(0)
vezes=int(0)

while True:
    n1 = int(input('informe o código do candidato'))
    if n1 == -1:
        break

    else:
        vezes+=1
        n2 = int(input('informe seu título de eleitor'))
        n3 = str(input('informe seu nome'))

    if n1 == 1:
        c1 += 1
    elif n1 == 2:
        c2 += 1
    elif n1 == 3:
        c3 += 1
    elif n1 == 4:
        c4 += 1
    elif n1 == 0:
        branco += 1
    else:
        nulo += 1
print(f'O candidato 1 {cand1} teve no total {c1} votos')
print(f'O candidato 2 {cand2} teve no total {c2} votos')
print(f'O candidato 3 {cand3} teve no total {c3} votos')
print(f'O candidato 4 {cand4} teve no total {c4} votos')

if c1 > c2 and c1 > c3 and c1 > c4:
    print(f'O vencedor foi o candidato {cand1} com {(c1/(vezes-nulo))*100}% dos votos ')
elif c2 > c1 and c2 > c3 and c2 > c4:
    print(f'O vencedor foi o candidato {cand2} com {(c2/(vezes-nulo))*100}% dos votos  ')
elif c3 > c1 and c3 > c2 and c3 > c4:
    print(f'O vencedor foi o candidato {cand3} com {(c3/(vezes-nulo))*100}% dos votos  ')
else:
    print(f'O vencedor foi o candidato {cand4} com {(c4/(vezes-nulo))*100}% dos votos  ')

print(f'O percentual de brancos em relação ao total foi de {(branco/(vezes-nulo))*100}%')
print(f'O percentual de votos nulos em relação ao total de votos é de {(nulo/vezes)*100}%')