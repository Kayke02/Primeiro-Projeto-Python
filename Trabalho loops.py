#Função da soma
def somar(N1, N2):
    return N1 + N2
#Função da subtração
def subtrair(N1, N2):
    return N1 - N2
#Função da multiplicação
def multiplicar(N1, N2):
    return N1 * N2
#Função da divisão
def dividir(N1, N2):
    return N1/N2
# VC = variável de continuidade
VC = 'S'
# Loop para realização da operação e verificação da continuidade da realização das operações
while VC != "N" and VC != 'N':
    VC = input("Você deseja realizar alguma operação matemática? S(sim) N(não): ")
    if VC == 'N' or VC == 'n':
        break
    else:
        N1 = float(input("Qual o primeiro número que você deseja realizar a operação?: "))
        N2 = float(input("Qual o segundo número que você deseja realizar a operação?: "))
        VO = int(input("Qual operação você deseja realizar? (1) Somar (2) Subtrair (3) Multiplicar (4) Dividir: "))
        if VO == 1:
            print(f"A soma de {N1} com {N2} resulta em {somar(N1, N2)}.")
        elif VO == 2:
            print(f"A subtração de {N1} com {N2} resulta em {subtrair(N1, N2)}.")
        elif VO == 3:
            print(f"A multiplicação de {N1} com {N2} resulta em {multiplicar(N1, N2)}.")
        elif VO == 4:
            if N2 == 0:
                print(f"A divisão de {N1} com {N2} não pode ser realizada, pois N2 é igual a 0 e tal divisão não é permitida.")
            else:
                print(f'A divisão de {N1} com {N2} resulta em {dividir(N1, N2): .2}')
        else:
            print("Valor digitado está incorreto, tente novamente.")
print(f"Obrigado por usar a aplicação!")