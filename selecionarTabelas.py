
def selecionarTabelas(cursor, dataMySQL) -> list:
    sql = [
        "SELECT table_name",
        "FROM information_schema.tables",
        f'WHERE table_schema = {dataMySQL["database"]}'
    ]
    cursor.execute(' '.join(sql))
    resultado = cursor.fetchall()
    return resultado
