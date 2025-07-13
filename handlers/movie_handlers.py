from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text('Привет! Отправь мне код в формате A-001, и я скажу его название по-русски.')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
    number_names = {
        0: 'Я препод',
        1: 'Один',
        2: 'Скин',
        3: 'Три',
        4: 'Четыре',
        5: 'Пять',
        6: 'Шесть',
        7: 'Семь',
        8: 'Восемь',
        9: 'Девять',
        10: 'Десять',
        11: 'Одиннадцать',
        12: 'Двенадцать',
        13: 'Тринадцать',
        14: 'Четырнадцать',
        15: 'Пятнадцать',
        16: 'Шестнадцать',
        17: 'Семнадцать',
        18: 'Восемнадцать',
        19: 'Девятнадцать',
        20: 'Двадцать'
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