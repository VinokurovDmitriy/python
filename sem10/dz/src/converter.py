from google_currency import convert
import json

from data_storage import help_data


def get_result():
    result = convert(help_data["from"], help_data["to"], help_data["count"])
    json1_data = json.loads(result)
    return json1_data['amount']
