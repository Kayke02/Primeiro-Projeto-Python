class Funcionario:
    def __init__(self,nome, salario_base=1000, calcular_salario):
        self.nome = nome
        self.salario = salario_base
        self.calcular_salario = calcular_salario
        def calcular_salario(self):
            return self.salario
class Gerente(Funcionario):
    def __init__(self,nome, salario_base, calcular_salario, bonus=500):
        super().__init__(nome, salario_base, calcular_salario)
        self.bonus = bonus
        def calcular_salario(self):
            return self.salario + self.bonus