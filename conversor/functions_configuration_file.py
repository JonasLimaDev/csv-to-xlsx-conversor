import toml
import os
from .classes_configuration_file import ConfigurationInput

def define_configs_structure():
    "Define configurações inicias padrão"
    config_initial = {
        'configuration':{
            'result':{
            'save_new_file': False
            },
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
    "Cria o arquivo de configuração inicial caso não exista"
    if not os.path.exists("config.toml"):
        with open(f'{path_file}config.toml', 'w') as f:
            toml.dump(define_configs_structure(), f)


def create_inputs_config(configs, base_inputs):
    """
    Cria uma lista com os dados de inputs para interface"""
    inputs_data = []
    for config in configs:
        for key_config in config:
            if key_config in base_inputs:
                inputs_data.append(
                    ConfigurationInput(
                        label=base_inputs[key_config][0],
                        key_to_write=key_config,
                        value=config[key_config],
                        helper=base_inputs[key_config][1].replace("       ",""),
                        type_config = type(base_inputs[key_config][2])
                    )
                )
    return inputs_data

