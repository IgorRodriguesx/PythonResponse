def paises_grandes(dados):
    # Lista para armazenar os países grandes
    grandes = []

    # Itera sobre os dados e verifica os critérios
    for pais in dados:
        nome, continente, area, populacao, _ = pais
        if populacao >= 25000000 or area >= 3000000:
            grandes.append((nome, populacao, area))

    return grandes

# Dados de exemplo
dados = [
    ("Afghanistan", "Asia", 652230, 25500100, 20343000000),
    ("Albania", "Europe", 28748, 2831741, 12960000000),
    ("Algeria", "Africa", 2381741, 37100000, 188681000000),
    ("Andorra", "Europe", 468, 78115, 3712000000),
    ("Angola", "Africa", 1246700, 20609294, 100990000000)
]

# Chama a função e imprime os resultados
resultados = paises_grandes(dados)
print("Saída:")
print("+-------------+------------+---------+")
print("| name        | population | area    |")
print("+-------------+------------+---------+")
for pais in resultados:
    print("| {:<11} | {:<10} | {:<7} |".format(*pais))
print("+-------------+------------+---------+")
