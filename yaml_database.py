import yaml
def yaml_loader(filepath):
    with open(filepath, "r") as file_descriptor:
        data = yaml.safe_load(file_descriptor) # Loader parametresi olmadan yaml.load deprecated
    return data


def yaml_dump(filepath, data):
    with open(filepath, "w") as file_descriptor:
        yaml.dump(data, file_descriptor)