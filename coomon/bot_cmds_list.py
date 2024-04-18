# здесь прописываю команды бота, которые видны в кнопке "меню"
from aiogram.types import BotCommand


private = [
    BotCommand(command='start', description='Начать работу'),
    BotCommand(command='description', description='Узнать, что умеет этот шедевробот'),
]
