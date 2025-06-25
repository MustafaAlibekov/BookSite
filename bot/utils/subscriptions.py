from aiogram import Bot


async def is_user_subscribed(bot: Bot, user_id: int, chat_link: str) -> bool:
    try:
        chat_member = await bot.get_chat_member(chat_id=chat_link, user_id=user_id)
        return chat_member.status in ['member', 'administrator', 'creator']
    except Exception as e:
        print(f"Ошибка проверки подписки: {e}")
        return False