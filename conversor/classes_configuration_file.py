import toml


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



class ConfigurationInput():
    def __init__(self, label, key_to_write, type_config, value="", helper=""):
        self.label = label
        self.key_to_write = key_to_write
        self.value = value
        self.helper = helper
        self.type_config = type_config
        self.value_display = self.value_to_display_view()
    
    def value_to_display_view(self):
        """
        Prepara as informações das configurações para visualização na interface.
        """
        if self.type_config != list:
            text_display = str(self.value)
            remove = ['[',']','"',]
            for item in remove:
                text_display =text_display.replace(item,"")
        else:
            text_display = ""
            for item in self.value:
                removes = ['[',']','"',]
                for remove in removes:
                    item = str(item).replace(remove,"")
                text_display += f"{item}; "
            text_display = text_display[:-2]
        return text_display
    
    def get_dict_to_save(self):
        """
        Prepara os dados para serem salvos no arquivo de configuração
        """
        if self.type_config == list:
            return {self.key_to_write: str(self.value).split(";")}
        elif self.type_config == bool:
            if str(self.value).lower() == "true" or str(self.value).lower() == "sim": 
                return {self.key_to_write: True}
            else:
                return {self.key_to_write: False}
        else:
            return {self.key_to_write: self.value}
