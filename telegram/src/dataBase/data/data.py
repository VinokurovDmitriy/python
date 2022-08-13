class DataBase:
    def __init__(self):
        self.item_data = [
            {
                'id': 34,
                'description': 'черри',
                'name': 'Помидоры',
                'count': 13
            },
            {
                'id': 3,
                'description': 'пупырчатые',
                'name': 'Огурцы',
                'count': 8
            },
            {
                'id': 4,
                'description': 'синенькие',
                'name': 'Баклажаны>',
                'count': 7
            }
        ]

    def add_item(self, id: int, description: str, name: str, count: int):
        self.item_data.append({
            'id': id,
            'description': description,
            'name': name,
            'count': count
        })

    def get_item(self, item_index):
        status = 'ok'
        if item_index == 0:
            status = 'small'
        elif item_index == len(self.item_data) - 1:
            status = 'big'
        return status, self.item_data[item_index]

