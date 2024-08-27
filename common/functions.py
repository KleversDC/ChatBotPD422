from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

cars = ["AUDI", "BMW", "Tesla", "Dodge", "Mersedes", "Kia", "Renault"]
menu = ["catalog", "basket", "cancel"]


async def reply_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, url="https://youtube.com"))
    return keyboard.adjust(3).as_markup()

async def inline_menu():
    keyboard = InlineKeyboardBuilder()
    for item in menu:
        keyboard.add(InlineKeyboardButton(text=item, callback_data=f"item_{item.lower()}"))
    return keyboard.adjust(2).as_markup()