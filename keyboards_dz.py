from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main_kb = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Привет"), KeyboardButton(text="Пока"),KeyboardButton(text="/links"),KeyboardButton(text="/dynamic")]
], resize_keyboard=True)

url_1 = 'https://dzen.ru/'
url_2 = 'https://music.yandex.ru/home'
url_3 = 'https://ya.ru/video/search?text=фильмы'

main_inline_kb = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Я.Новости", url=url_1)],
   [InlineKeyboardButton(text="Я.Музыка", url=url_2)],
   [InlineKeyboardButton(text="Я.Видео", url=url_3)]])

main_inline_kb2 = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Показать больше", callback_data='show_more')]])

test_kb_command =  [('Опция 1', 'Команда 1'), ('Опция 2', 'Команда 2')]
test_kb = ["Опция 1", "Опция 2"]
async def test_keyboard():
   keyboard = InlineKeyboardBuilder()
   for key in test_kb_command:
      keyboard.add(InlineKeyboardButton(text=key[0], callback_data=key[1]))
   return keyboard.adjust(2).as_markup()

