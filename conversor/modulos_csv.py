import csv
from .config_file_data import load_config_file,get_filters, get_config_file_csv


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
    config_file = get_config_file_csv()
    delimiter_file = config_file['delimiter_file'] if config_file else ","
    encode_file = config_file['encoding_file'] if config_file else "latin-1"

    with open(path_csv_file, 'r',  encoding=encode_file) as file_csv:
        csv_file_reader = csv.reader(file_csv,delimiter=delimiter_file)
        for row in csv_file_reader:
            list_data_file.append(row)
    return list_data_file


def remove_rows_by_terms(dados, terms: list):
    data_filtered = []
    for dado in dados:
        if not any(elem in dado for elem in terms):
            data_filtered.append(dado)
    return data_filtered


def remove_rows_excepty_first(base_data, terms: list):
    data_filtered = []
    exclude_row_contains = []
    for data_item in base_data:
        if not any(elem in data_item for elem in exclude_row_contains):
            # print(any(elem in data_item for elem in exclude_row_contains))
            for term in terms:
                if term in data_item:
                    exclude_row_contains.append(term)
                    terms.pop(
                        terms.index(term)
                    )
            data_filtered.append(data_item)
    return data_filtered


def remove_blank_rows(base_data):
    data_filtered = []
    for data_item in base_data:
        if not all(elem == "" for elem in data_item):
            data_filtered.append(data_item)
    return data_filtered


def filters_aplier(base_data): 
    config_filters = get_filters()
    if not config_filters:
        return base_data
    # print(config_filters)
    filters_applied = base_data
    if config_filters['exclude-row']['exclude_empety_rows']:
        filters_applied = remove_blank_rows(filters_applied)
    if config_filters['exclude-row']['row_excepty_firts']:
        filters_applied = remove_rows_excepty_first(filters_applied,
        config_filters['exclude-row']['row_excepty_firts']
        )
    if config_filters['exclude-row']['row_contains']:
        filters_applied = remove_rows_by_terms(filters_applied,
        config_filters['exclude-row']['row_contains']
        )
    return filters_applied