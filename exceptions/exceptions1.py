import re


class FilePathError(Exception):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def __str__(self):
        return f'Incorrect file path: {self.file_path}'


class FileHandler:
    def __init__(self, file_path: str, no_connectors: int, max_file_size: int):
        if re.match(r'^(.+)\/([^\/]+)$', file_path) is None:
            raise FilePathError(file_path)
        if no_connectors > 10:
            raise ValueError('Number of connectors has to be 10 or less')
        if len(str(max_file_size)) != 4:
            raise ValueError('Max file size has to be four-digit number')
        self.file_path = file_path
        self.no_connectors = no_connectors
        self.max_file_size = max_file_size

    def set_file_path(self, new_path: str):
        if re.match(r'^(.+)\/([^\/]+)$', new_path) is None:
            raise FilePathError(new_path)
        self.file_path = new_path

    def set_no_connectors(self, new_number: int):
        if new_number > 10:
            raise ValueError('Number of connectors has to be 10 or less')
        self.no_connectors = new_number

    def set_max_file_size(self, new_max_size: int):
        if len(str(new_max_size)) != 4:
            raise ValueError('Max file size has to be four-digit number')
        self.max_file_size = new_max_size

    def read_content(self):
        print('')

    def save_to_file(self):
        print('')


# Tests

file_handler1 = FileHandler('C:/Program Files/JetBrains/PyCharm Community', 8, 4000)
# file_handler2 = FileHandler('sdagawgfa', 8, 4000)
# file_handler3 = FileHandler('C:/Program Files/JetBrains/PyCharm Community', 12, 4000)
# file_handler4 = FileHandler('C:/Program Files/JetBrains/PyCharm Community', 8, 12345)
