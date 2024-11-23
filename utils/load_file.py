import pandas as pd


def load_files(file_name):
    """Load all files to analy

    :param file_name: (string) - The file name
    :return: pandas object

    >>> file_name('file name')
    Pandas Objects

    """
    file = pd.read_csv(file_name)
    print(f"This is file has {file.shape[0], file.shape[1]} structure")

    return file
