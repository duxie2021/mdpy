import os
import json


class EmptyConfig:

    def __init__(self):
        pass

    def load(self, config_path):
        load_from_file(self, config_path)


def class_to_dict(obj):
    if isinstance(obj, dict):
        return obj
    if hasattr(obj, 'to_dict'):
        return obj.to_dict()
    return obj.__dict__


def dict_to_object(data, obj):
    for key, value in data.items():
        setattr(obj, key, value)
    return obj


def save_to_file(obj, config_path):
    with open(config_path, 'w') as f:
        json.dump(obj, f, indent=True, default=class_to_dict)


def load_from_file(obj, config_path):
    if os.path.exists(config_path):
        with open(config_path) as f:
            config_dict = json.load(f)
            dict_to_object(config_dict, obj)
