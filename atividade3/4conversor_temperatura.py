def converter_temperatura(valor, origem, destino):
    # Converte para Celsius primeiro
    if origem == "C":
        celsius = valor
    elif origem == "F":
        celsius = (valor - 32) * 5/9
    elif origem == "K":
        celsius = valor - 273.15
    else:
        return None

    # Converte de Celsius para destino
    if destino == "C":
        return celsius
    elif destino == "F":
        return (celsius * 9/5) + 32
    elif destino == "K":
        return celsius + 273.15
    else:
        return None

# Entrada do usuário
valor = float(input("Digite a temperatura: "))
origem = input("Informe a unidade de origem (C, F, K): ").upper()
destino = input("Informe a unidade de destino (C, F, K): ").upper()

# Conversão
resultado = converter_temperatura(valor, origem, destino)

# Saída
if resultado is not None:
    print(f"{valor:.2f}°{origem} equivale a {resultado:.2f}°{destino}")
else:
    print("Unidade inválida. Use C, F ou K.")