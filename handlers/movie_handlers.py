from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text('Привет! Отправь мне код в формате 000, и я скажу его название по-русски.')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
    number_names = {
        0: 'Я препод',
        1: 'Мерцающий арбуз',
        2: 'Скин',
        3: 'Под прикрытием в старшей школе',
        4: 'Винченцо',
        5: 'Король Стейтен-Айленда',
        6: 'Скоро',
        7: 'Скоро',
        8: 'Скоро',
        9: 'Скоро',
        10: 'Скоро',
        11: 'Скоро',
        12: 'Скоро',
        13: 'Скоро',
        14: 'Скоро',
        15: 'Скоро',
        16: 'Скоро',
        17: 'Скоро',
        18: 'Скоро',
        19: 'Скоро',
        20: 'Скоро'
    }
    text = update.message.text.strip()
    import re
    import os
    match = re.fullmatch(r"(\d{3})", text)
    if match:
        num = int(match.group(1))
        if num in number_names:
            image_path = f"images/image{num}.jpg"
            if os.path.exists(image_path):
                with open(image_path, "rb") as photo:
                    await update.message.reply_photo(photo=photo, caption=number_names[num])
            else:
                await update.message.reply_text(number_names[num])
            return
        else:
            await update.message.reply_text("Нет названия для этого кода.")
            return
    await update.message.reply_text("Пожалуйста, отправьте код в формате 000") 