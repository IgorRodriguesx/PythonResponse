import sqlite3

# Conecta ao banco de dados SQLite em memória
conn = sqlite3.connect(':memory:')
cur = conn.cursor()

# Cria a tabela World
cur.execute('''CREATE TABLE World (
               nome VARCHAR,
               continente VARCHAR,
               area INT,
               populacao INT,
               PIB BIGINT)''')

# Insere os dados de exemplo na tabela World
dados = [
    ("Afghanistan", "Asia", 652230, 25500100, 20343000000),
    ("Albania", "Europe", 28748, 2831741, 12960000000),
    ("Algeria", "Africa", 2381741, 37100000, 188681000000),
    ("Andorra", "Europe", 468, 78115, 3712000000),
    ("Angola", "Africa", 1246700, 20609294, 100990000000)
]

cur.executemany("INSERT INTO World VALUES (?, ?, ?, ?, ?)", dados)

# Consulta SQL para encontrar os países grandes
query = '''SELECT nome, populacao, area FROM World
           WHERE populacao >= 25000000 OR area >= 3000000'''

# Executa a consulta
cur.execute(query)

# Mostra os resultados
print("Saída:")
print("+-------------+------------+---------+")
print("| name        | population | area    |")
print("+-------------+------------+---------+")
for row in cur.fetchall():
    print("| {:<11} | {:<10} | {:<7} |".format(*row))
print("+-------------+------------+---------+")

# Fecha a conexão com o banco de dados
conn.close()
