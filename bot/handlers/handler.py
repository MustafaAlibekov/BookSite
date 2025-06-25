from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from utils.subscriptions import is_user_subscribed
from config import GROUP_LINK
from .category_handler import get_category_keyboard
router = Router()


@router.callback_query(F.data == "register")
async def handle_register(callback: CallbackQuery, bot):
    await callback.message.edit_text(
        "Подпишитесь на наш канал, чтобы получить рекомендации по книгам:",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Подписаться", url=GROUP_LINK)],
            [InlineKeyboardButton(text="Я подписался", callback_data="subscriptions")]
        ])
    )
    await callback.answer()


@router.callback_query(F.data == "subscriptions")
async def check_subscription(callback: CallbackQuery, bot):
    user_id = callback.from_user.id
    if await is_user_subscribed(bot, user_id, GROUP_LINK):
        await callback.message.edit_text("✅ Вы подписаны! Теперь выберите интересующую вас категорию:")
        keyboard, _ = get_category_keyboard(0)
        await callback.message.edit_reply_markup(reply_markup=keyboard)
    else:
        await callback.answer("❌ Вы ещё не подписались на канал.")