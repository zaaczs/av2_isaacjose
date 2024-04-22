import mysql.connector

def exec_sql_cmd(cmd, cursor):
    cursor.execute(cmd)

def criar_database(dbname, cursor):
    exec_sql_cmd(f"CREATE DATABASE IF NOT EXISTS {dbname};", cursor)

def usar_database(dbname, cursor):
    exec_sql_cmd(f"USE {dbname};", cursor)

def criar_tabela(table, attrs, cursor):
    exec_sql_cmd(f"CREATE TABLE IF NOT EXISTS {table} ({attrs});", cursor)

def inserir_dados(table, attrs, values, cursor):
    exec_sql_cmd(f"INSERT INTO {table} ({attrs}) VALUES ({values});", cursor)

def selecionar_condicao(attrs, table, wherecond, cursor):
    if wherecond:
        exec_sql_cmd(f"SELECT {attrs} FROM {table} WHERE {wherecond};", cursor)
    else:
        exec_sql_cmd(f"SELECT {attrs} FROM {table};", cursor)
    result = cursor.fetchall()
    print("Resultado da consulta:")
    for row in result:
        print(row)

# Ativação do autocommit para garantir que as alterações sejam salvas
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ijfr88814768",
    database="meu_banco_de_dados",
    autocommit=True
)
cursor = mydb.cursor()

# Objetivo da questão 3
criar_database('AV2_isaacjose', cursor)
usar_database("AV2_isaacjose", cursor)
criar_tabela("USERS", 'id INT, name VARCHAR(255), country VARCHAR(255), id_console INT', cursor)
criar_tabela("VIDEOGAMES", 'id_console INT, name VARCHAR(255), id_company INT, release_date DATETIME', cursor)
criar_tabela("GAMES", "id_game INT, title VARCHAR(255), genre VARCHAR(255), release_date DATETIME, id_console INT", cursor)
criar_tabela("COMPANY", "id_company INT, name VARCHAR(255), country VARCHAR(75)", cursor)  

# Inserindo dados na tabela USERS
inserir_dados("USERS", "id, name, country, id_console", "1, 'João', 'Brasil', 1", cursor)

# Inserindo dados nas tabelas VIDEOGAMES, GAMES e COMPANY (exemplo)
# Certifique-se de substituir os valores de exemplo pelos dados reais que deseja inserir
inserir_dados("VIDEOGAMES", "id_console, name, id_company, release_date", "1, 'Game 1', 1, '2023-01-01 00:00:00'", cursor)
inserir_dados("GAMES", "id_game, title, genre, release_date, id_console", "1, 'Game Title', 'Action', '2023-01-01 00:00:00', 1", cursor)
inserir_dados("COMPANY", "id_company, name, country", "1, 'Company Name', 'USA'", cursor)

# Selecionando dados para verificar se as inserções foram bem-sucedidas
selecionar_condicao("*", "USERS", "", cursor)
selecionar_condicao("*", "VIDEOGAMES", "", cursor)
selecionar_condicao("*", "GAMES", "", cursor)
selecionar_condicao("*", "COMPANY", "", cursor)