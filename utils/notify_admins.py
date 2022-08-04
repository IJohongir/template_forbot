import logging
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Command
from data.config import admins
from keyboards.default import adminMarkup

from loader import dp, db, bot


async def on_startup_notify(dp: Dispatcher):
    for admin in admins:
        try:
            await dp.bot.send_message(admin, "я начал работать")

        except Exception as err:
            logging.exception(err)


@dp.message_handler(Command('admin'))
async def admins_not(message: types.Message):
    admin = admins
    user_id = message.from_user.id

    if user_id in admin:
        await message.answer(
            "Привествую вас оо все могучий 💪💪💪", reply_markup=adminMarkup
        )

    else:
        await message.answer("У вас нет права админа😬!!!")

