import toml
import os
 

def read_toml(filename='./config.toml'):
    with open(filename, "r") as f:
        return toml.load(f)
    

def write_toml(filename:str='./config.toml', toml_data:dict=None):
    with open(filename, "w") as f:
        toml.dump(toml_data, f)

def exists_toml(filename:str='./config.toml'):
    return os.path.exists(filename)

def create_toml_config():
    toml_data = read_toml("./utils/template_config.toml")
    write_toml("./config.toml", toml_data)

def load_config():
    if not exists_toml("./config.toml"):
        create_toml_config()
    return read_toml("./config.toml")

config = load_config()