from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

adminMarkup = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton('Добавить админ'),
            KeyboardButton("🗑Удаление админа")

        ]
    ], resize_keyboard=True
)