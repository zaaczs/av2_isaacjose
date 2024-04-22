import mysql.connector

# Estabelecer conexão com o MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ijfr88814768",
    database="meu_banco_de_dados",
    autocommit=True
)

# Cursor no qual executa comandos SQL no banco de dados.
cursor = mydb.cursor()

# Usar database
usar_database = lambda dbname, cursor: cursor.execute(f"USE {dbname};")

# Função lambda para gerar o INNER JOIN entre as tabelas
generate_inner_join = lambda: """
SELECT GAMES.title, GAMES.genre, GAMES.release_date, COMPANY.name AS company_name
FROM GAMES
INNER JOIN VIDEOGAMES ON GAMES.id_console = VIDEOGAMES.id_console
INNER JOIN COMPANY ON VIDEOGAMES.id_company = COMPANY.id_company;
"""

# Função lambda para gerar o comando SELECT com os atributos envolvidos
generate_select_query = lambda attributes: f"""
SELECT {', '.join(attributes)}
FROM GAMES
INNER JOIN VIDEOGAMES ON GAMES.id_console = VIDEOGAMES.id_console
INNER JOIN COMPANY ON VIDEOGAMES.id_company = COMPANY.id_company;
"""

# Exemplo de uso:
usar_database("av2_isaacjose", cursor)

# Atributos que queremos selecionar na consulta
attributes = ["GAMES.title", "GAMES.genre", "COMPANY.name AS company_name"]
select_query = generate_select_query(attributes)
print("\nComando SELECT com os atributos especificados:")
print(select_query)
