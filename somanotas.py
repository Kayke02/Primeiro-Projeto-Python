nome=input("Digite o nome do aluno: ")
nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
nota3=float(input("Digite a terceira nota: "))
nota4=float(input("Digite a quarta nota: "))
media=(nota1+nota2+nota3+nota4)/4
if media >=7:
    print(f"A média das 4 notas ({nota1: .1f},{nota2: .1f},{nota3: .1f},{nota4: .1f} ) do aluno {nome} é {media: .2f} e ele está aprovado")
elif media<=4:
    print(f"A média das 4 notas ({nota1: .1f},{nota2: .1f},{nota3: .1f},{nota4: .1f} ) do aluno {nome} é {media: .2f} e ele está reproprovado")
else:
    print(f"A média das 4 notas ({nota1: .1f},{nota2: .1f},{nota3: .1f},{nota4: .1f} ) do aluno {nome} é {media: .2f} e ele está de recuperação")
notaR=float(input("Digite a nota da recuperação: "))
if notaR>=7:
    print("A nota da recuperação do aluno",nome," foi", notaR, " e ele está aprovado")
else:
    print(f"A nota da recuperação do aluno {nome} foi {notaR} e ele está reprovado")
