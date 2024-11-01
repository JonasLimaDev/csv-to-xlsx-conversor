import csv
from .config_file_data import (
    load_config_file,
    get_filters,
    get_config_file_csv,
    )


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


def exclude_rows_contains_terms(dados, terms: list):
    data_filtered = []
    for dado in dados:
        if not any(elem in dado for elem in terms):
            data_filtered.append(dado)
    return data_filtered


def exclude_rows_excepty_first(base_data, terms: list):
    data_filtered = []
    exclude_row_contains = []
    for data_item in base_data:
        if not any(elem in data_item for elem in exclude_row_contains):
            for term in terms:
                if term in data_item:
                    exclude_row_contains.append(term)
                    terms.pop(
                        terms.index(term)
                    )
            data_filtered.append(data_item)
    return data_filtered


def exclude_rows_empety(base_data, option):
    data_filtered = []
    if not option:
        return base_data

    for data_item in base_data:
        if not all(elem == "" for elem in data_item):
            data_filtered.append(data_item)
    return data_filtered


def exclude_rows_contains_partial(base_data, partials):
    ignore = False
    for data_item in base_data:
        for elem in data_item:
            for part in partials:
                if part in elem:
                    del(base_data[base_data.index(data_item)])
    return base_data


def add_blank_itens_to_colunms(base_data):
    limite = max(len(l) for l in base_data)
    processed_data = []
    for item in base_data:
        blank_itens = ["" for count in range(limite - len(item))]
        processed_data.append(
            item + blank_itens)
    return processed_data


def exclude_columns_number(base_data, columns_numbers):
    """
    >>> remove_columns([[1,2,3,4,5,6,7]],[2,5,6])
    [[1, 2, 4, 5]]
    >>> remove_columns([[1,2,3,4,5,6,7]],[0,4,6])
    [[2,3,4,6]]
    """
    data_filtered = []
    columns_numbers = [number-1 for number in columns_numbers]
    print()
    for data_item in base_data:
        for index in sorted(columns_numbers, reverse=True):
            try:
                del(data_item[index])
            except:
                pass
        data_filtered.append(data_item)
    return data_filtered


def filters_aplier(base_data):
    filters = get_filters()
    if not filters:
        return base_data
    base_data = add_blank_itens_to_colunms(base_data)
    for prefix in filters.keys():
        for function, values_paran in filters[prefix].items():
            name_function = f'{prefix}_{function}'
            base_data = globals()[name_function](base_data, values_paran)
    return base_data