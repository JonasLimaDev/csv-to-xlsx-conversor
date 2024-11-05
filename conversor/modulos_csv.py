import csv

def get_data_csv_file(path_csv_file="dados.csv", config_file=None):
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
    with open(path_csv_file, 'r', encoding=config_file['encoding_file']) as file_csv:
        csv_file_reader = csv.reader(file_csv,
            delimiter=config_file['delimiter_file'])
        try:
            for row in csv_file_reader:
                list_data_file.append(row)
        except Exception as e:     
            return e
    return list_data_file
    

def remove_blank_item(list_terms):
    for term in list_terms:
        if term.strip() == "" or term == "":
            list_terms.pop(list_terms.index(term))
    return list_terms


def exclude_rows_contains_terms(dados, terms: list):
    data_filtered = []
    terms = remove_blank_item(terms)
    for dado in dados:
        if not any(elem in dado for elem in terms):
            data_filtered.append(dado)
    return data_filtered


def exclude_rows_excepty_first(base_data, terms: list):
    data_filtered = []
    exclude_row_contains = []
    terms = remove_blank_item(terms)
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
    partials = remove_blank_item(partials)
    for data_item in base_data:
        for part in partials:
            for elem in data_item:
                if part.strip() != ""  and part in elem :
                    base_data.remove(data_item)
                    break
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
    columns_numbers = remove_blank_item(columns_numbers)
    columns_numbers = [int(number)-1 for number in columns_numbers]
    for data_item in base_data:
        for index in sorted(columns_numbers, reverse=True):
            try:
                del(data_item[index])
            except:
                pass
        data_filtered.append(data_item)
    return data_filtered


def filters_aplier(base_data, filters):
    """
    Executa as funções conforme os filtros passados.
    """
    if not filters:
        return base_data
    base_data = add_blank_itens_to_colunms(base_data)
    for prefix in filters.keys():
        for function, values_paran in filters[prefix].items():
            name_function = f'{prefix}_{function}'
            if values_paran != ['']:
                base_data = globals()[name_function](base_data, values_paran)
    return base_data