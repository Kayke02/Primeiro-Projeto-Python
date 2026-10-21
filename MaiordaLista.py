limite=int(input(f"Digite a quantidade de elementos presentes na lista a ser comparada: "))
vetor=[None]*limite
for i in range(limite):
    vetor[i]=int(input(f"digite o {i+1}° elemento da sua lista: "))
def comparar(a,b):
    if a>b:
        maior=a
    else:
        maior=b
    return maior
for i in range(limite-1):
    maior_comparado = comparar(vetor[i],vetor[i+1])
print(f"{maior_comparado}")
