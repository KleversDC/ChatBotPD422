from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram import F, Router
import common.keyboard as kb
import common.functions as fun

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hello user", reply_markup= await fun.inline_menu())

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('I`am your telegram bot and i`ll help you to make choice')

@router.message(F.text == 'Hello')
async def answer_hello(message: Message):
    await message.reply(f'Hello, my friend {message.from_user.full_name}')

@router.callback_query(F.data == "catalog")
async def catalog(callback: CallbackQuery):
    await callback.answer("Your choice is catalog", show_alert=True)
    await callback.message.edit_text("Select a car: ", reply_markup=await fun.reply_cars())