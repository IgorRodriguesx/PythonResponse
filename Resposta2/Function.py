import sqlite3

def preco_produtos_na_data(dados, data):
    # Criação do banco de dados em memória
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()

    # Criação da tabela Products
    cur.execute('''CREATE TABLE Products (
                   product_id INT,
                   new_price INT,
                   change_date DATE)''')

    # Insere os dados fornecidos na tabela
    cur.executemany("INSERT INTO Products VALUES (?, ?, ?)", dados)

    # Criação da tabela temporária TempPrices
    cur.execute('''CREATE TEMP TABLE TempPrices AS
                   SELECT product_id,
                          COALESCE(new_price, 10) AS price,
                          change_date
                   FROM Products
                   WHERE change_date <= ?''', (data,))

    # Seleciona o preço máximo de cada produto na data especificada
    cur.execute('''SELECT product_id,
                          MAX(price) AS price
                   FROM TempPrices
                   GROUP BY product_id''')

    # Retorna os resultados
    resultados = cur.fetchall()

    # Fecha a conexão com o banco de dados
    conn.close()

    return resultados

# Dados de exemplo
dados = [
    (1, 20, '2019-08-14'),
    (2, 50, '2019-08-14'),
    (1, 30, '2019-08-15'),
    (1, 35, '2019-08-16'),
    (2, 65, '2019-08-17'),
    (3, 20, '2019-08-18'),
    (3, 20, '2019-08-21'),
    (2, 75, '2019-08-23')
]

# Data especificada
data_especificada = '2019-08-16'

# Chama a função e imprime os resultados
resultados = preco_produtos_na_data(dados, data_especificada)
print("Saída:")
print("+------------+-------+")
print("| product_id | price |")
print("+------------+-------+")
for produto in resultados:
    print("| {:<11} | {:<5} |".format(produto[0], produto[1]))
print("+------------+-------+")
