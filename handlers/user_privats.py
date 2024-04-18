# это файл для общения бота с юзером в личных сообщениях
import asyncio

from aiogram import Bot, types, Router, F
from aiogram.filters import CommandStart, Command, or_f
from handlers.config import TOKEN

from keyboards.reply import get_keyboard

bot = Bot(token=TOKEN)
user_private_router = Router()


# тут универсальная клавиатура
@user_private_router.message(or_f(CommandStart(), F.text.lower() == 'старт'))  # обработчик
async def start_cmd(message: types.Message):
    await message.answer(

        '''
Привет, я виртуальный помощник
Ознакомься с кнопками этого бота:
        ''',

        reply_markup=get_keyboard(
            'Старт',
            'Описание',
            'Найти ближайший 📍',
            placeholder='Что вас интересует?',
            sizes=(2, )
        ),
    )



@user_private_router.message(or_f(Command('description'), F.text.lower() == 'описание'))
async def menu_disc(message: types.Message):
    await message.answer('''
Вот тебе описание бота:
                         
Этот проект создан для активных и амбициозных исследователей городов. 
Он решает такую проблему, как <i>"не знаю, куда пойти"</i>. Вам хочется поесть вкусной пиццы, 
но ближайшая пиццерия уже надоела? Знайте, <b>мы</b> решим эту проблему! 
Поделитесь локацией, напишите заветное слово "пицца" и бац! Вам уже намечен маршрут, вам
известно название пиццерии, её рейтинг, описание и часы работы. 
  
 Наслаждайтесь!
 ''')

