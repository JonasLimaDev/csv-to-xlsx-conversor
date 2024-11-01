import toml
import os

def create_inital_config():
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
    if not os.path.exists("config.toml"):
        wirite_config_file(config_initial)


def load_config_file():
    try:
        with open("./config.toml", "r") as f:
            data = toml.load(f)
    except:
        return None    
    return data


def wirite_config_file(data_config, file_path='./'):
    with open(f'{file_path}config.toml', 'w') as f:
        toml.dump(data_config, f)


def add_configuration(data_config, data_to_add):
    for type_config in data_config.keys():
        for configuration in data_config[type_config]:
            for config_to_add in data_to_add:
                if config_to_add in data_config[type_config][configuration]:
                    data_config[type_config][configuration][config_to_add] = data_to_add[config_to_add]
    return data_config


def get_config_file_csv():
    try:
        return load_config_file()['configuration']['file']
    except:
        return None

        
def get_filters():
    try:
        return load_config_file()['filters']
    except:
        return None

def get_individual_config():
    try:
        # return load_config_file()['filters']
        individual_configuration = []
        configurations = load_config_file()
        for type_config in configurations:
            for gruop in  configurations[type_config]:
                individual_configuration.append(configurations[type_config][gruop])
        return individual_configuration
    except:
        return None
# create_inital_config()
# add_configuration(load_config_file(),{"rows_excepty_first":["Tombamento",]})