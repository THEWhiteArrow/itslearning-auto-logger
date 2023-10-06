import toml
import os
 

def read_toml(filename='./config.toml'):
    """
    Reads a toml file and returns a dict.
    @param filename: The path to the toml file.
    @return dict: The toml file as a dict.
    """

    with open(filename, "r") as f:
        return toml.load(f)
    

def write_toml(filename:str='./config.toml', toml_data:dict=None):
    """
    Writes a dict to a toml file.
    @param filename: The path to the toml file.
    @param toml_data: The dict to write to the toml file.
    """

    with open(filename, "w") as f:
        toml.dump(toml_data, f)

def exists_toml(filename:str='./config.toml'):
    """
    Checks if a toml file exists.
    @param filename: The path to the toml file.
    @return bool: True if the file exists, False if it does not.
    """

    return os.path.exists(filename)

def create_toml_config():
    """
    Creates a toml file with default values.
    """
    toml_data = read_toml("./utils/template_config.toml")
    write_toml("./config.toml", toml_data)

def load_config():
    """
    Loads the config from the toml file.
    @return dict: The toml file as a dict.
    """
    
    if not exists_toml("./config.toml"):
        create_toml_config()
    return read_toml("./config.toml")

config = load_config()