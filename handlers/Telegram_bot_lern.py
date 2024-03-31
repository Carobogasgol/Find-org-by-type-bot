import asyncio
import time
from distutils.cmd import Command
from urllib.request import urlopen
from dataclasses import dataclass
import json
import aiohttp

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.strategy import FSMStrategy
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, BotCommandScopeAllPrivateChats

from config import TOKEN
from handlers.user_privats import user_private_router
from handlers.FSM_location import main_work
from coomon.bot_cmds_list import private


ALLOWED_UPDATES = ['message, edited_message']


bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)  # отвечает за фильтрацию разных сообщений
dp = Dispatcher(fsm_strategy=FSMStrategy.USER_IN_CHAT)  # подключаю роутер к диспетчеру
dp.include_routers(user_private_router, main_work)
URL = f'https://api.telegram.org/bot{TOKEN}/'


# Кнопка отправки геолокации
# markup_requests = ReplyKeyboardMarkup(resize_keyboard=True).add(
#     KeyboardButton('Отправить свою геолокацию', request_location=True))

# @dataclass(slots=True, frozen=True)
# class Coordinates:
#     latitude: float
#     longitude: float

# def get_coordinates():
#     data = _get_ip_data()
#     latitude = data['loc'].split(',')[0]
#     longitude = data['loc'].split(',')[1]
#     return Coordinates(latitude=latitude, longitude=longitude)
#
# def _get_ip_data():
#     url = 'http://ipinfo.io/json'
#     response = urlopen(url)
#     return json.load(response)

# def get_keyboard():
#     keyboard = types.ReplyKeyboardMarkup()
#     button = types.KeyboardButton("Share Position", request_location=True)
#     keyboard.add(button)
#     return keyboard


# @user_private_router.message(content_types=['location'])
# async def handle_location(message: types.Message):
#     lat = message.location.latitude
#     lon = message.location.longitude
#     reply = f'latitude: {lat}\nlongitude: {lon}'
#     await message.answer(reply, reply_markup=types.ReplyKeyboardRemove())


# @dp.message_handler(commands=['locate_me'])
# async def cmd_locate_me(message: types.Message):
#     reply = "Click on the the button below to share your location"
#     await message.answer(reply, reply_markup=get_keyboard())


#     CommandStart() - реакция на /start
#     описываем тип события.
#     С пустыми скобками работает на любой текст+смайлик
#     очерёдность важна

# @dp.message()
# async def answer(message: types.Message):
#     text = message.text
#     if text in ['привет', 'Привет', 'hi', 'Hi', 'hello', 'Hello']:
#         await message.answer('И тебе привет, дружище')
#     elif text in ['пока', 'прощай', 'Прощай']:
#         await message.answer('Прощай, подруга')
#     else:
#         await message.answer(message.text) #это эхо

# диспетчер - фильтрация всех событий


# async def send_message(chat_id, text):
#     async with aiohttp.ClientSession() as session:
#         params = {'chat_id': chat_id, 'text': text}
#         async with session.post(URL + 'sendMessage', data=params) as response:
#             await response.json()
#
#
# async def handle_updates(update):
#     message = update.get('message', False)
#     if message:
#         chat_id = message['chat']['id']
#         text = message.get('text', False)
#         if text:
#             await send_message(chat_id, f'Эхо: {text}')
#         else:
#             await send_message(chat_id, 'Я работаю только с текстом')
#
#
# async def get_updates():
#     offset = None
#     async with aiohttp.ClientSession() as session:
#         while True:
#             params = {'timeout': 10, 'offset': offset}
#             async with session.post(URL + 'getUpdates', data=params) as response:
#                 updates = await response.json()
#                 if len(updates['result']) > 0:
#                     offset = updates['result'][-1]['update_id'] + 1
#                     for update in updates['result']:
#                         await handle_updates(update)
#
#                         for_print = update.copy()
#                         for_print['message']['from']['id'] = 1234567890
#                         for_print['message']['chat']['id'] = 9985645850
#                         #посмотреть содержимое обновления
#                         print(for_print)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    # чтобы скипать обновления пока бот был офлайн
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    # это для создания кнопки меню
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)
asyncio.run(main())


# вот так запускаем
# бот начнёт слушать сервер телеги,
# но это надо ещё и запустить через библиотеку
