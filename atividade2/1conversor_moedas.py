#Conversor de moedas.
# Valores das moedas
valor_em_reais = 100.00
taxa_dolar = 5.70
taxa_euro = 6.40
# Conversões
valor_em_dolares = valor_em_reais / taxa_dolar
valor_em_euros = valor_em_reais / taxa_euro
# Exibição dos resultados
print(f"Valor em Reais: R$ {valor_em_reais: .2f}")
print("Valor em Dólares: $", round(valor_em_dolares, 2))
print("Valor em Euros: €", round(valor_em_euros, 2))
