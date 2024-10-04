import csv


def get_data_csv_file(path_csv_file="dados.csv"):
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
    with open(path_csv_file, 'r',  encoding='latin-1') as file_csv:
        csv_file_reader = csv.reader(file_csv)
        for row in csv_file_reader:
            list_data_file.append(row)
    return list_data_file

