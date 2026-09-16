Vingresso=30
Vpipoca=15
Vrefrigerante=6
Vpringles=15

print("Bem vindo ao nosso app de compra de Ingressos online!")
print(f"Tabela de preços: \n"
      f"Ingresso Inteiro = {Vingresso} \n"
      f"Meio Ingresso = {Vpipoca} \n"
      f"Refrigerante = {Vrefrigerante} \n"
      f"Pringles = {Vpringles} \n")

Qingressos=int(input("Quantos ingressos você(s) deseja(m)?: "))
Qmeias=int(input("Quantos desses ingressos são meia?: "))
SubTingressos=30*(Qingressos-Qmeias) + 15*Qmeias
print(f"O gasto com ingressos foi de {SubTingressos} reais.")

Qpipocas=int(input("Quantas pipocas você(s) deseja(m)?: "))
SubTpipoca=Vpipoca*Qpipocas
print(f"O gasto com pipocas foi de {SubTpipoca} reais.")

Qrefrigerantes=int(input("Quantos refrigerantes você(s) deseja(m)?: "))
SubTrefrigerantes=Vrefrigerante*Qrefrigerantes
print(f"O gasto com refrigerantes foi de {SubTrefrigerantes} reais.")

Qpringles=int(input("Quantas pringles você(s) deseja(m)?: "))
SubTpringles=Vpringles*Qpringles
print(f"O gasto com pringles foi de {SubTpringles} reais.")

Total=SubTingressos+SubTpipoca+SubTrefrigerantes+SubTpringles
print(f"O custo total preliminar de todas os itens foi de {Total} reais, há um adicional de {Total*0.05} reais pelo uso do app, o que resulta num total final de {Total*1.05} reais.")
