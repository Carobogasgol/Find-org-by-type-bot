import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.fsm.strategy import FSMStrategy

from handlers.config import TOKEN
from handlers.user_privats import user_private_router
from handlers.FSM_location import main_work
from coomon.bot_cmds_list import private


ALLOWED_UPDATES = ['message, edited_message']


bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)  # отвечает за фильтрацию разных сообщений
dp = Dispatcher(fsm_strategy=FSMStrategy.USER_IN_CHAT)  # подключаю роутер к диспетчеру
dp.include_routers(user_private_router, main_work)
URL = f'https://api.telegram.org/bot{TOKEN}/'


async def main():
    await bot.delete_webhook(drop_pending_updates=True)

    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    # это для создания кнопки меню
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)
asyncio.run(main())


# вот так запускаем
# бот начнёт слушать сервер телеги,
# но это надо ещё и запустить через библиотеку
