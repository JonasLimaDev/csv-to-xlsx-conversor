import toml

def load_config_file():
    try:
        with open("./config.toml", "r") as f:
            data = toml.load(f)
    except:
        return None    
    return data

def wirite_config_file(data_config):
    # Write the modified config back to the file
    with open('./config.toml', 'w') as f:
        toml.dump(data_config, f)


def get_config_file_csv():
    try:
        return load_config_file()['config-file']
    except:
        return None
def get_filters():
    try:
        return load_config_file()['filters']
    except:
        return None

# def get_filters_new():
#     try:
#         return load_config_file()['filters']
#     except:
#         return None