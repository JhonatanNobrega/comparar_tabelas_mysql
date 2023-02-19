
import mysql.connector

from gerarArquivoJson import gerarArquivoJson
from selecionarTabelas import selecionarTabelas
from selecionarTabelasCamposTipos import selecionarTabelasCamposTipos


def gerarDb(dataMySQL):
    db_connection = mysql.connector.connect(
        host=dataMySQL['host'],
        user=dataMySQL['user'],
        password=dataMySQL['pass'],
        database=dataMySQL['database']
    )

    cursor = db_connection.cursor()

    tabelaList = selecionarTabelas(cursor, dataMySQL)
    tabelaListCamposTipos = selecionarTabelasCamposTipos(cursor, tabelaList)

    arquivoTabelaList = f'tabelas_{dataMySQL["tipo"]}'
    gerarArquivoJson(tabelaList, arquivoTabelaList)

    arquivoTabelaListCamposTipo = f'tabelas_campos_tipos_{dataMySQL["tipo"]}'
    gerarArquivoJson(tabelaListCamposTipos, arquivoTabelaListCamposTipo)

    cursor.close()
    db_connection.close()

    return tabelaListCamposTipos
