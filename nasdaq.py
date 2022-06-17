import nasdaqdatalink

nasdaqdatalink.read_key(filename="my_api_key.txt")


def download_data(path_name):
    data = nasdaqdatalink.get(path_name)
    return data


def download_many_data(names_list):
    data_list = []
    for name in names_list:
        data_list.append(download_data(name))
    return data_list
