import json

import data_loading
import model

#constants for reading settings
PATH = 'path'

def read_settings() -> dict:
    """
    Reads settings from file. Documentation of setting located at ...
    :return: returns settings dict
    """
    with open('config.json') as f:
        settings = json.load(f)
    return settings

if __name__ == '__main__':
	settings = read_settings()
	data = data_loading.load(settings[PATH])
	model.capacity_prediction(data)