import toml
import os


def define_configs_structure():
    config_initial = {
        'configuration':{
            'file':{
            'encoding_file': 'utf-8', 'delimiter_file': ','
            },
        },
        'filters': {
            'exclude': {
                'rows_contains_partial':[],
                'rows_contains_terms': [],
                'rows_excepty_first': [],
                'rows_empety': True,
                'columns_number': [],
            }
        }
    }
    return config_initial


def create_inital_config(path_file='./'):
    if not os.path.exists("config.toml"):
        with open(f'{path_file}config.toml', 'w') as f:
            toml.dump(define_configs_structure(), f)


class FileDataConfig():
    def __init__(self,file_path='./'):
        self.all = self.load_file(file_path)
        self.config_filters = self.get_filters()
        self.confi_to_read = self.get_config_read_file
        self.config_types = self.all.keys()
        self.current_path = file_path


    def load_file(self,path):
        """
        Carrega as informações de configuração do arquivo .toml, caso ele exista. 
        """
        try:
            with open(f"{path}config.toml", "r") as f:
                data = toml.load(f)
        except Exception as e:
            return e
        return data
    

    def save_file(self, path=None):
        """
        Rescreve as informações de configurações no arquivo .toml
        """
        with open(f'{path if path else self.current_path}config.toml', 'w') as f:
            toml.dump(self.all, f)


    def update_config(self):
        """
        atualiza as informações conforme arquivo de configuração
        """
        self.all = self.load_file(self.current_path)
        self.config_filters = self.get_filters()
        self.confi_to_read = self.get_config_read_file
        self.config_types = self.all.keys()


    def get_filters(self):
        """
        Retornar apenas as filtros para serem aplicados no arquivo csv.
        """
        try:
            return self.all['filters']
        except:
            return None

    def get_config_read_file(self):
        """
        Retornar apenas as configurações necessárias para ler o arquivo csv
        """
        try:
            return self.all['configuration']['file']
        except:
            return None


    def add_configuration(self, data_to_add):
        """
        Método para adição de novas convigurações,
        recebe um dicionário com o nome da configuração e os valores.

        """
        for config_type in self.config_types:
            for group in self.all[config_type]:
                for config_to_add in data_to_add:
                    if config_to_add in self.all[config_type][group]:
                        self.all[config_type][group][config_to_add] = data_to_add[config_to_add]


    def get_individual_config(self):
        """
        Cria uma lista de dicionários, onde, 
        - chave é o nome da configuração,
        - valor é a configuração que será usada de fato.
        """
        individual_configuration = []
        for config_type in self.config_types:
            for gruop in self.all[config_type]:
                individual_configuration.append(self.all[config_type][gruop])
        return individual_configuration
        