import csv


def get_data_csv_file(path_csv_file="dados.csv",
    encode_file="utf-8", delimiter_file=","):
    """
    Lê um arquivo '.csv' e retornar os dados em uma lista de listas,
    sendo, as listas internas as linhas do arquivo.

    Entrada:
     - Caminho do arquivo csv que será lido.
     - type: str

    Saída:
     - lista de listas com os dados do arquivo lido.
     - type: list

    Exemplo da estrutura de saída:
    [
        ['linha 1 coluna A', 'linha 1 coluna B'],
        ['linha 2 coluna A', 'linha 2 coluna B'],
    ]

    """
    list_data_file = []

    with open(path_csv_file, 'r',  encoding=encode_file) as file_csv:
        csv_file_reader = csv.reader(file_csv,delimiter=delimiter_file)
        for row in csv_file_reader:
            list_data_file.append(row)
                
    return list_data_file



def remove_rows_by_terms(dados, terms: list):
    dados_filtrados = []
    for dado in dados:
        if not any(elem in dado for elem in terms):
            dados_filtrados.append(dado)
    return dados_filtrados


def remove_rows_excepty_first(dados, terms: list):
    dados_filtrados = []
    exclude_row_contains = []
    for dado in dados:
        if not any(elem in dado for elem in exclude_row_contains):
            # print(any(elem in dado for elem in exclude_row_contains))
            for term in terms:
                if term in dado:
                    exclude_row_contains.append(term)
                    terms.pop(
                        terms.index(term)
                    )
            dados_filtrados.append(dado)
    return dados_filtrados


def remove_blank_rows(dados):
    dados_filtrados = []
    for dado in dados:
        if not all(elem == "" for elem in dado):
            dados_filtrados.append(dado)
    return dados_filtrados
