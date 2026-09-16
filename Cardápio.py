sopa = 20
feijoada = 27
hamburguer = 25
pizza = 35
refrigerante = 5
print(f"Tabela de Preços: \n sopa = {sopa} R$ \n feijoada = {feijoada} R$ \n hamburguer = {hamburguer} R$ \n pizza = {pizza} R$ \n refrigerante = {refrigerante} R$")
QS = int(input("Quantas sopas você(s) desejam? "))
StS = sopa*QS
QF = int(input("Quantas feijoadas você(s) desejam? "))
StF = feijoada*QF
QH = int(input("Quantos hamburgueres você(s) desejam? "))
StH = hamburguer*QH
QP = int(input("Quantas pizzas você(s) desejam? "))
StP = pizza*QP
QR = int(input("Quantos refrigerantes você(s) desejam? "))
StR = refrigerante*QR
Total = (StS+StF+StH+StP+StR)
print(f" O subtotal gasto com sopas é igual a: {StS} R$ \n O subtotal gasto com feijoadas é igual a: {StF} R$ \n O subtotal gasto com hamburgueres é igual a {StH} R$ \n O subtotal gasto com pizzas é igual a: {StP} R$ \n O subtotal gasto com refrigerantes é igual a: {StR} R$ \n O custo total(sem os 10%) é igual a: {Total} R$ \n O valor pago ao garçom(10%) é igual a: {0.1*Total: .2f} R$ \n O valor total(com os 10%) é igual a {1.1*Total: .2f} R$")
if (1.1*Total>200):
    print(f"O valor total a ser pago (com os 10%) é de{1.1*Total: .2f} ultrapassou os 200 R$")
resposta = input("Você deseja dividir com outras pesssoas? (S/N) ")
if resposta == "S" or resposta == "s":
    NP = int(input("Quantas pessoas pagarão a conta? "))
    if NP < 4:
        print (f"O valor a ser pago por cada pessoa é igual a: {(1.1*Total)/NP:.2f} R$")
    else:
        print (f"O valor a ser pago por cada pessoa é igual a: {0.95 * ((Total*1.1)/NP): .2f} R$")
else:
    print(f"O valor total a ser pago é igual a: {1.1*Total} R$")
Pgorjeta = input("Você gostaria de dar uma gorjeta? (S/N) ")
if Pgorjeta == "S" or Pgorjeta == "s":
    gorjeta=float(input("Quantos reais você gostaria de dar para os nossos excelentes trabalhadores? "))
    print(f"Muito obrigado pela gorjeta de {gorjeta} reais!")
else:
    print("Tudo bem, entendemos que você não pode ou não deseja fornecer agora, como podemos melhorar o serviço?")



