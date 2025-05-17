import os

def root_join(*parts):
    """ Функция, которая возвращает путь к файлу указанному из корня """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_dir, *parts)
    return full_path