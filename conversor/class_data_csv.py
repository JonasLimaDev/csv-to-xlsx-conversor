import csv
class DataClassCSV():
    def __init__(self, data=[], filters={}, path_file="./"):
        self.data = data
        self.filters = filters
        self.erros = None
        self.path_file = path_file


    def exclude_columns_number(self, columns_numbers):
        """
        >>> remove_columns([[1,2,3,4,5,6,7]],[2,5,6])
        [[1, 2, 4, 5]]
        >>> remove_columns([[1,2,3,4,5,6,7]],[0,4,6])
        [[2,3,4,6]]
        """
        print("exclude_columns_number")
        data_filtered = []
        columns_numbers = self.remove_blank_item(columns_numbers)
        columns_numbers = [int(number)-1 for number in columns_numbers]
        for data_item in self.data:
            for index in sorted(columns_numbers, reverse=True):
                try:
                    del(data_item[index])
                except:
                    pass
            data_filtered.append(data_item)
        self.data = data_filtered
    

    def exclude_rows_excepty_first(self, terms: list):
        print("exclude_rows_excepty_first")
        data_filtered = []
        exclude_row_contains = []
        terms = self.remove_blank_item(terms)
        for data_item in self.data:
            if not any(elem in data_item for elem in exclude_row_contains):
                for term in terms:
                    if term in data_item:
                        exclude_row_contains.append(term)
                        terms.pop(
                            terms.index(term)
                        )
                data_filtered.append(data_item)
        self.data = data_filtered
    

    def remove_blank_item(self,list_terms):
        for term in list_terms:
            if term.strip() == "" or term == "":
                list_terms.pop(list_terms.index(term))
        return list_terms


    def exclude_rows_contains_terms(self, terms: list):
        print("exclude_rows_contains_terms")
        data_filtered = []
        terms = self.remove_blank_item(terms)
        counter = 0
        for item in self.data:
            if any(elem.strip() in item for elem in terms):
                self.data.remove(item)
                counter += 1
        return counter


    def exclude_rows_contains_partial(self, partials: list):
        print("exclude_rows_contains_partial")
        partials = self.remove_blank_item(partials)
        removed = False
        counter = 0
        for data_item in self.data:
            for part in partials:
                for elem in data_item:
                    if part.strip() in elem :
                        self.data.remove(data_item)
                        removed = True
                        break
                if removed:
                    counter += 1
                    removed=False
                    break
        return counter


    def exclude_rows_empety(self, option: bool):
        print("exclude_rows_empety")
        for data_item in self.data:
            if all(elem == "" for elem in data_item):
                self.data.remove(data_item)


    def filters_aplier(self):
        """
        Executa as funções conforme os filtros passados.
        """
        # base_data = add_blank_itens_to_colunms(base_data)
        for prefix in self.filters.keys():
            for function, values_paran in self.filters[prefix].items():
                name_function = f'{prefix}_{function}'
                if values_paran != ['']:
                    match name_function:
                        case "exclude_rows_empety":
                            self.exclude_rows_empety(values_paran)
                        case "exclude_rows_contains_partial":
                            while True:
                                result = self.exclude_rows_contains_partial(values_paran)
                                if result == 0:
                                    break
                        case "exclude_rows_contains_terms":
                             while True:
                                result = self.exclude_rows_contains_terms(values_paran)
                                if result == 0:
                                    break
                        case "exclude_rows_excepty_first":
                            self.exclude_rows_excepty_first(values_paran)
                        case "exclude_columns_number":
                            self.exclude_columns_number(values_paran)

                    getattr(self,name_function)( values_paran)
                    # globals()[name_function](self.data, values_paran)
    def load_csv_file(self,config_file
    ):
        list_data_file = []
        with open(self.path_file, 'r', encoding=config_file['encoding_file']) as file_csv:
            csv_file_reader = csv.reader(file_csv,delimiter=config_file['delimiter_file'])
            try:
                for row in csv_file_reader:
                    list_data_file.append(row)
            except Exception as e:
                self.erros = e
        self.data = list_data_file
    
    def write_csv_file(self,config_file):
        with open('temp_file.csv', 'w',encoding=config_file['encoding_file'], newline='') as csvfile:
            writer = csv.writer(csvfile, )
            writer.writerows(self.data)