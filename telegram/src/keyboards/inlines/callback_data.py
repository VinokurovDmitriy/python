from aiogram.utils.callback_data import CallbackData

start_callback = CallbackData('start')
navigation_callback = CallbackData('navigation', 'for_data', 'id')
by_callback_callback = CallbackData('buy', 'id_item')
count_items_callback = CallbackData('change_count', 'type_change', 'good_id')
