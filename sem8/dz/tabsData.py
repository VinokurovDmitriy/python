from sem8.dz.controllers import showPupils, showDfMerged, getPhones, getAddress, getPlaces
from sem8.dz.controllers.viewController import delPupil, findPupil, setAllParams

pupilsData = [{'type': 'scrolledtext', 'data': showPupils(), 'row': 2}]
contactPhonesData = [{'type': 'scrolledtext', 'data': showDfMerged(getPhones()), 'row': 2}]
addressBookData = [{'type': 'scrolledtext', 'data': showDfMerged(getAddress()), 'row': 2}]
placeData = [
    {'type': 'scrolledtext', 'data': showDfMerged(getPlaces()), 'row': 2},
]
addPupilData = [
    {'type': 'label', 'label': 'Имя', 'column': 0, 'row': 0},
    {'type': 'entry', 'name': 'name', 'column': 0, 'row': 1},
    {'type': 'label', 'label': 'Фамилия', 'column': 1, 'row': 0},
    {'type': 'entry', 'name': 'surname', 'column': 1, 'row': 1},
    {'type': 'label', 'label': 'Дата рождения', 'column': 2, 'row': 0},
    {'type': 'entry', 'name': 'birthday', 'column': 2, 'row': 1},
    {'type': 'label', 'label': 'Класс', 'column': 3, 'row': 0},
    {'type': 'entry', 'name': 'class', 'column': 3, 'row': 1},
    {'type': 'label', 'label': 'Успеваемость', 'column': 0, 'row': 2},
    {'type': 'entry', 'name': 'progress', 'column': 0, 'row': 3},
    {'type': 'label', 'label': 'Ряд', 'column': 1, 'row': 2},
    {'type': 'entry', 'name': 'row', 'column': 1, 'row': 3},
    {'type': 'label', 'label': 'Парта', 'column': 2, 'row': 2},
    {'type': 'entry', 'name': 'desk', 'column': 2, 'row': 3},
    {'type': 'label', 'label': 'Вариант', 'column': 3, 'row': 2},
    {'type': 'entry', 'name': 'variant', 'column': 3, 'row': 3},
    {'type': 'label', 'label': 'Телефон', 'column': 0, 'row': 6},
    {'type': 'entry', 'name': 'phone', 'column': 0, 'row': 7},
    {'type': 'label', 'label': 'Тел. инфо', 'column': 1, 'row': 6},
    {'type': 'entry', 'name': 'commentPhone', 'column': 1, 'row': 7},
    {'type': 'label', 'label': 'Адрес', 'column': 2, 'row': 6},
    {'type': 'entry', 'name': 'address', 'column': 2, 'row': 7},
    {'type': 'label', 'label': 'Адрес инфо', 'column': 3, 'row': 6},
    {'type': 'entry', 'name': 'commentAddress', 'column': 3, 'row': 7},
    {'type': 'button',
     'label': 'Добавить Ученика', 'column': 0, 'row': 8, 'command': setAllParams},
    {'type': 'button',
     'label': 'Поиск по имени', 'column': 1, 'row': 8, 'command': lambda: findPupil('name')},
    {'type': 'button',
     'label': 'Поиск по фамилии', 'column': 2, 'row': 8, 'command': lambda: findPupil('surname')},
    {'type': 'button',
     'label': 'Удалить', 'column': 3, 'row': 8, 'command': delPupil},
    {'type': 'scrolledtext', 'data': '', 'row': 9, 'height': 10},

]