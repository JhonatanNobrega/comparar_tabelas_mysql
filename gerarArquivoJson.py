import json


def gerarArquivoJson(tabelaList, nomeArquivo):
    arquivoTabelaList = f'{nomeArquivo}.json'
    with open(arquivoTabelaList, "w") as arquivo:
        json.dump(tabelaList, arquivo, indent=2)
