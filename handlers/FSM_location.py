# тут FSM для получения локации
from aiogram import types, Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove, InputMediaPhoto, FSInputFile

# для загрузки фото ссылки
from keyboards import reply
from aiogram.fsm.state import State, StatesGroup

from handlers.user_privats import bot

from handlers.geo import get_business_info


main_work = Router()


# хранилище
class MainWork(StatesGroup):
    # Шаги состояний
    lat = State()
    long = State()
    business_organization = State()


# ищем локацию
@main_work.message(StateFilter(None), F.text.lower() == 'найти ближайший 📍')
async def add_(message: types.Message, state: FSMContext):
    await message.answer('Для начала работа отправь мне свою локацию!',
                         reply_markup=reply.location_kb)

    await state.set_state(MainWork.lat)
    await state.set_state(MainWork.long)


# ищем организацию
@main_work.message(F.location)
async def add_location(message: types.Message, state: FSMContext):
    await state.update_data(lat=message.location.latitude)
    await state.update_data(long=message.location.longitude)

    await message.answer('Введи тип организации, что ты ищешь', reply_markup=ReplyKeyboardRemove())
    await state.set_state(MainWork.business_organization)


# конец
@main_work.message(F.text)
async def add_business_organization(message: types.Message, state: FSMContext):
    await state.update_data(business_organization=message.text)
    data = await state.get_data()

    media = get_business_info(data['lat'], data['long'], data['business_organization'])

    media_group = [
        InputMediaPhoto(media=media[0],
                        caption='Название организации'),
        InputMediaPhoto(media=media[1],
                        caption='Пример фото оттуда'),
        InputMediaPhoto(media=media[2],
                        caption='Примерное расположение')
    ]
    working_status = media[3]
    biz_link = media[4]
    biz_rate = media[5]
    organization_name = media[6]
    photo_route = FSInputFile(r'route.png')

    await bot.send_media_group(chat_id=message.chat.id, media=media_group)
    await message.answer(f'{organization_name} \n{working_status} \nОценка: {biz_rate}, \nСсылка: {biz_link}')
    print(message.chat.first_name)
    await bot.send_photo(chat_id=message.chat.id, photo=photo_route, caption='Маршрут')
    await message.answer('Если требуется найти что-то ещё - пиши!')
