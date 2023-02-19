
from gerarDb import gerarDb
from variaveis_ambiente import DATA_MYSQL_DEV, DATA_MYSQL_PRO

tabelaListCamposTiposDev = gerarDb(DATA_MYSQL_DEV)
tabelaListCamposTiposPro = gerarDb(DATA_MYSQL_PRO)

for itemDev in tabelaListCamposTiposDev:
    itemAchado = False
    for itemPro in tabelaListCamposTiposPro:
        if itemDev == itemPro:
            itemAchado = True
            break

    if not itemAchado:
        print(itemDev)
