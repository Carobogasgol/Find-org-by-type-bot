from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_keyboard(
        *btns: str,
        placeholder: str = None,
        request_contact=None,
        request_location=None,
        sizes: tuple[int] = (2,),
):
    keyboard = ReplyKeyboardBuilder()

    for index, text in enumerate(btns, start=0):

        if request_contact and request_contact == index:
            keyboard.add(KeyboardButton(text=text, request_contact=True))

        elif request_location and request_location == index:
            keyboard.add(KeyboardButton(text=text, request_location=True))

        else:
            keyboard.add(KeyboardButton(text=text))

    return keyboard.adjust(*sizes).as_markup(
        resize_keyboard=True, input_field_placrholder=placeholder)


location_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Отправить мне свою геолокацию 📍', request_location=True)]],
    resize_keyboard=True,
    input_field_placeholder='Сделай это!'
)


# # это то, что было до улучшения
# start_kb = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text="Меню"),
#             KeyboardButton(text="Старт"),
#         ],
#         [
#             KeyboardButton(text="Локация", request_location=True),
#             KeyboardButton(text="чмо"),
#             KeyboardButton(text="Отправить номер", request_contact=True)
#         ],
#     ],
#     resize_keyboard=True,
#     input_field_placeholder='Чё тебе надо, путник?'
#     # это, чтобы изменить текст в строке текста
# )


# start_kb3.row(KeyboardButton(text='example'))  # добавить просто кнопку новым рядом
