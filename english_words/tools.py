"""

Functions for fork with this project

"""


def get_data_from_file(filename: str) -> list:
    """
    Get data from file. Trasform data to format.

    :param filename: filename file with data

    :return: formating list
    """
    try:
        with open(filename) as f:
            data = f.read()
        return trasform_data_from_file(data)
    except Exception as e:
        print(e)
    return []


def trasform_data_from_file(junk_data: str) -> list:
    """
    Clear data to need format
    :param junk_data:
    :return:
    """
    if not isinstance(junk_data, str):
        return []
    try:
        data = [
            [y.strip() for y in x.split('-')]
            for x in junk_data.lower().split('\n') if '-' in x]
    except Exception as e:
        print(e)
        data = []
    return data

