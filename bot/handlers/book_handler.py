from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()


BOOKS_BY_CATEGORY = {
    "Фантастика": [
        {"title": "Сталкер", "age": "old"},
        {"title": "Ночной дозор", "age": "new"}
    ],
    "Романтика": [
        {"title": "Гордость и предубеждение", "age": "old"},
        {"title": "После", "age": "new"}
    ],
}


@router.callback_query(F.data.startswith("age_"))
async def show_books(callback: CallbackQuery):
    _, age, category = callback.data.split("_")
    books = [book["title"] for book in BOOKS_BY_CATEGORY.get(category, []) if book["age"] == age]
    if not books:
        await callback.message.edit_text("Книги по вашему запросу пока отсутствуют.")
    else:
        result = "\n".join([f"- {book}" for book in books])
        await callback.message.edit_text(f"Вот рекомендуемые книги ({'новые' if age == 'new' else 'классика'}): \n{result}")