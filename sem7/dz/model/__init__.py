data = {}


def init(d):
    global data
    data = d


def rowFormat():
    return '\n{};{};{};{}\n'.format(data['name'], data['surName'], data['phone'], data['description'])


def columnFormat():
    return '*{}\n*{}\n*{}\n{}\n\n'.format(data['name'], data['surName'], data['phone'], data['description'])


def getContactDict(contactList):
    return {
        'name': contactList[0],
        'surName': contactList[1],
        'phone': contactList[2],
        'description': contactList[3]
    }
