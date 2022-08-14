from google_currency import convert
import json


def get_result(fr, to, count):
    result = convert(fr, to, count)

    json1_data = json.loads(result)
    return json1_data['amount']
