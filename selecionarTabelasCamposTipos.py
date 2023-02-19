
def selecionarTabelasCamposTipos(cursor, tabelaList) -> list:
    sql_whare = f'WHERE TABLE_NAME = "{tabelaList[0][0]}"'
    for index, item in enumerate(tabelaList):
        if (index == 0):
            continue
        sql_whare += f' OR TABLE_NAME = "{item[0]}"'
    sql = [
        "SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, IS_NULLABLE",
        "FROM INFORMATION_SCHEMA.COLUMNS",
        sql_whare
    ]
    cursor.execute(' '.join(sql))
    resultado = cursor.fetchall()
    return resultado
