# dados do usuario
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))

# calculo do IMC
imc = peso / (altura ** 2)

# classificacao
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

# resultado
print(f"Seu IMC é {imc:.2f}. Classificação: {classificacao}")