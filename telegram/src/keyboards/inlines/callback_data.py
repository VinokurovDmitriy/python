from aiogram.utils.callback_data import CallbackData

start_callback = CallbackData('start')
navigation_callback = CallbackData('navigation', 'for_data', 'good_id')
by_callback = CallbackData('buy', 'good_id')
count_items_callback = CallbackData('change_count', 'type_change', 'good_id')
