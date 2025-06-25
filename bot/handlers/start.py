from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.message(F.text == "/start")
async def cmd_start(message: Message):
    kb = [
        [InlineKeyboardButton(text="Найти книгу", callback_data="register")],
        [InlineKeyboardButton(text="Информация о боте", callback_data="help")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    await message.answer("Добро пожаловать! Выберите действие:", reply_markup=keyboard)


@router.callback_query(F.data == "help")
async def process_help(callback_query):
    help_text = (
        "🤖 Я помогу вам найти подходяшую вам кингу.\n\n"
        "🔹 Нажмите 'Зарегистрироваться' и вступите в группу Telegram.\n"
        "🔹 После этого нажмите 'Я вступил', чтобы получить рекомендацию по книгам.\n"
        "❓ Если у вас есть вопросы — напишите @LordOtThik."
    )
    await callback_query.message.answer(help_text)
    await callback_query.answer()