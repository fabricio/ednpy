# Leitura das quatro notas
notas = input().split()

N1 = float(notas[0])
N2 = float(notas[1])
N3 = float(notas[2])
N4 = float(notas[3])

# Cálculo da média ponderada
media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10

print(f"Media: {media:.1f}")

# Decisão conforme a média
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    
    # Leitura da nota do exame
    exame = float(input())
    print(f"Nota do exame: {exame:.1f}")
    
    # Nova média com exame
    media_final = (media + exame) / 2

    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    
    print(f"Media final: {media_final:.1f}")