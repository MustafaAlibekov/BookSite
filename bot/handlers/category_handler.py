from aiogram import Router, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

router = Router()

CATEGORIES = [
    "Фантастика", "Романтика", "Триллер",
    "Классика", "Приключения", "Научная литература",
    "Фэнтези", "Ужасы"
]
ITEMS_PER_PAGE = 6


def get_category_keyboard(page: int):
    start_index = page * ITEMS_PER_PAGE
    end_index = start_index + ITEMS_PER_PAGE
    current_page = CATEGORIES[start_index:end_index]
    total_pages = len(CATEGORIES) // ITEMS_PER_PAGE + (1 if len(CATEGORIES) % ITEMS_PER_PAGE > 0 else 0)

    kb = []
    for category in current_page:
        kb.append([InlineKeyboardButton(text=category, callback_data=f"cat_{category}")])

    nav_buttons = []
    if page > 0:
        nav_buttons.append(InlineKeyboardButton(text="⬅️ Назад", callback_data=f"page_{page - 1}"))
    if end_index < len(CATEGORIES):
        nav_buttons.append(InlineKeyboardButton(text="➡️ Вперёд", callback_data=f"page_{page + 1}"))
    if nav_buttons:
        kb.append(nav_buttons)

    return InlineKeyboardMarkup(inline_keyboard=kb), total_pages


@router.callback_query(F.data.startswith("page_"))
async def navigate_pages(callback: CallbackQuery):
    page = int(callback.data.split("_")[1])
    keyboard, total_pages = get_category_keyboard(page)
    await callback.message.edit_reply_markup(reply_markup=keyboard)


@router.callback_query(F.data.startswith("cat_"))
async def choose_age(callback: CallbackQuery):
    category = callback.data.split("_", 1)[1]
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🆕 Новые книги", callback_data=f"age_new_{category}")],
        [InlineKeyboardButton(text="📚 Классика", callback_data=f"age_old_{category}")]
    ])
    await callback.message.edit_text(f"Выберите возраст книги в категории '{category}':", reply_markup=kb)