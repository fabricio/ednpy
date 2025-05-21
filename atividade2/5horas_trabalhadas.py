#Calculadora de salário por horas trabalhadas
# Ler os valores informados pelo usuário
numero_funcionario = int(input("Insira o número do funcionário: "))
horas_trabalhadas = int(input("Insira a quantidade de horas trabalhadas: "))
valor_por_hora = float(input("Insira o valor da hora trabalhada: "))
# Cálculo do salário
salario = horas_trabalhadas * valor_por_hora
# Exibir o resultado para o usuário
print ("Número do funcionário: ", numero_funcionario)
print ("Salário = R$", round(salario,2))
