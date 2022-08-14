from data_storage import currencies
def get_descriptions_currency():
    return '\n'\
        .join([f'{key.capitalize()}: {value}' for key, value in currencies.items()])
