from converter import get_result
from data_storage import currencies, steps, help_data


def get_descriptions_currency():
    return '\n'.join([f'<b>{key}</b>: {value}' for key, value in currencies.items()])


def get_steps():
    return '\n'.join(steps)


def save_help_data(key, value):
    help_data[key] = value


def check_help_data():
    return help_data['from'] and help_data['to']


def get_result_convert():
    return f'{help_data["count"]} {help_data["from"]} = {get_result()} {help_data["to"]}'


def reset_help_data():
    help_data['count'] = None
    help_data['from'] = None
    help_data['to'] = None
