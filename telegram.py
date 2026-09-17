from aiogram import Bot

from config import BOT_TOKEN, GROUP_ID, TOPIC_ID


bot = Bot(token=BOT_TOKEN)


async def send_price(price):

    message = (
        "💵 <b>قیمت دلار</b>\n\n"
        f"🇺🇸 قیمت تتر: <b>{price:,.0f}</b> تومان\n\n"
        "🔄 بروزرسانی خودکار هر ۲ ساعت"
    )

    await bot.send_message(
        chat_id=GROUP_ID,
        message_thread_id=TOPIC_ID,
        text=message,
        parse_mode="HTML"
    )
