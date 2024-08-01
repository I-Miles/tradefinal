import sqlite3

# Conectar ao banco de dados (ou criá-lo se não existir)
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Comando SQL para inserção de múltiplos registros
sql_insert = """
    INSERT INTO fornecedor (codiforn, nomeforn, razasocforn, foneforn) VALUES
        ('F001', 'Patrick', 'Lambisgoia', 190),
        ('F002', 'Isaac', 'McDonalds', 172);
"""
sql_insert2 = """
    INSERT INTO produto (codiprod, descprod, valorprod, situprod, idforn_id) VALUES
        ('P001', 'Tomate', 5.00, 'Vermelho', 1),
        ('P002', 'Lanche', 15.00, 'Marrom', 2);
"""
sql_insert3 = '''
   INSERT INTO venda (idvend, codivend, valorvend, descvend, totalvend, datavend, valorcomissao, idcli_id, idforn_id, idvende_id) VALUES
        (1, 'V001', 150.00, 'Venda de ração premium', 150.00, '2023-07-30', 15.00, 1, 1, 1),
        (2, 'V002', 250.00, 'Venda de produtos de higiene para pets', 250.00, '2023-08-15', 25.00, 2, 2, 2);
'''

sql_insert4 = '''
   INSERT INTO vendedor (codivende, nomevende, razasocvende, fonevende, porcvende) VALUES
        ('V001', 'Migs', 'Miguel Tec', 123, 30);
'''


# Executar o comando SQL
cursor.execute(sql_insert)

# Confirmar a transação (fazer o commit)
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()

print("Inserção de dados concluída com sucesso.")