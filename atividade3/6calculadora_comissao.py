# Entrada de dados
nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo: "))
vendas = float(input("Digite o total de vendas do mês: "))

# Cálculo da comissão e total a receber
comissao = vendas * 0.15
total_receber = salario_fixo + comissao

# Saída formatada
print(f"total {total_receber:.2f}")