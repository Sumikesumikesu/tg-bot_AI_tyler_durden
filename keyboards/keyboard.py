from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

markup = InlineKeyboardMarkup()
item_tyler = InlineKeyboardButton("tyler,", callback_data='tyler')
item_samanta = InlineKeyboardButton("samanta,", callback_data='samanta')
markup.add(item_tyler, item_samanta)
