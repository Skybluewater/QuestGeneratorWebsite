from os import path


def get_current_app_name(file):
    return path.dirname(file).replace('\\', '/').split('/')[-1]


current_app_name = get_current_app_name(__file__)

default_app_config = current_app_name + '.apps.' + current_app_name.capitalize() + 'Config'

