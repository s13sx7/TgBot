from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu = [[KeyboardButton(text='/help')]]
menu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=menu)