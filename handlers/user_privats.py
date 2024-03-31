# это файл для общения бота с юзером в личных сообщениях
import asyncio

from aiogram import Bot, types, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, or_f
from aiogram.types import URLInputFile, InputMediaPhoto, FSInputFile  # для загрузки фото ссылки
from keyboards import reply
from config import TOKEN

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


# await message.answer('Ознакомься с нашими кнопками! Так ты получишь понимание способностей этого бота',
# reply_markup=reply.start_kb)


# тут в Command можно вписать команды

# @user_private_router.message(or_f(Command('chmo'), F.text.lower() == 'чмо'))
# async def menu_cmd(message: types.Message):
#     await message.reply(message.text)  # это эхо
#     await message.answer(
#         '''
# этот шедевробот создан тремя гениями
# ты chmo
#         ''',
#         reply_markup=types.ReplyKeyboardRemove()  # убираю клавиатуру
#     )


# photo = 'https://krot.info/uploads/posts/2022-03/1647141781_68-krot-info-p-khonda-prikol-smeshnie-foto-73.jpg'
# работает даже с переменной, это хорошо!

# media_group = [
#     InputMediaPhoto(media=FSInputFile(r'me.jpg')),
#     InputMediaPhoto(media=FSInputFile(r'andrew.jpg')),
#     InputMediaPhoto(media=FSInputFile('eliz.jpg'))
# ]


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



# @user_private_router.message(or_f(Command('location'), F.text.lower() == 'найти ближайший..'))
# async def get_location(message: types.Message):
#     await message.answer('Вот и твоя локация!')


# @user_private_router.message(or_f(Command('number'), F.text.lower() == 'отправить номер'),
#                              F.content_type.in_('contact'))
# async def menu_kaif(message: types.Message):
#     await message.answer('Вот и твой номер!')


# @user_private_router.message(F.text)
# async def menu_disc(message: types.Message):
#     await message.answer('это магический фильтр')


# async def geo_info(message: types.Location):
#     await message.answer('это локационный магический фильтр')
#     lat = message.location.latitude
#     lon = message.location.longitude
#     await message.answer(f'latitude: {lat}, longitude: {lon}')
#     await message.answer('Вот и твоя локация!')


# @user_private_router.message(content_types=['location'])
# async def handle_location(message: types.Message):
    # # await sendLocation(latitude, longitude)
    # lat = message.location.latitude
    # lon = message.location.longitude
    # await message.answer(f 'latitude: {lat}, longitude: {lon}')


# вот так возвращаю номер телефона
# @user_private_router.message(F.contact)
# async def get_contact(message: types.Message):
#     await message.answer('<b>Номер получен</b>')  # Красивый шрифт
#     await message.answer(str(message.contact.phone_number))
