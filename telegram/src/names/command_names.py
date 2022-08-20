from dataclasses import dataclass


@dataclass
class UserCommands:
    start: str = '/start'
    help: str = '/help'
    info: str = 'info'
    hi: str = 'Привет'
    leave_feedback: str = 'Оставить отзыв'
    find_item: str = 'Найти товар'
    stop_search: str = 'Остановить поиск'
    to_store: str = 'В магазин'
    show_all_items: str = 'Показать все товары'
    show_basket: str = 'Показать корзину'
    about_us: str = 'О нас'
    contacts: str = 'Контакты'
    about_bot: str = 'О боте'
    work_schedule: str = 'Режим работы'
    send_contact: str = 'Отправить контакт'
    send_location: str = 'Отправить местоположение'
    main_menu: str = 'Главное меню'
