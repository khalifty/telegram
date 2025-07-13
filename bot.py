import asyncio
import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from config.settings import TELEGRAM_TOKEN
from handlers.movie_handlers import start, handle_message

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def error_handler(update, context):
    """Обработчик ошибок"""
    logging.error(f"Произошла ошибка: {context.error}")
    if update and update.effective_message:
        await update.effective_message.reply_text("Произошла ошибка. Попробуйте еще раз.")

def main():
    while True:
        try:
            if not TELEGRAM_TOKEN:
                print("Ошибка: TELEGRAM_TOKEN не найден в переменных окружения")
                break
                
            application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
            application.add_handler(CommandHandler("start", start))
            application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
            application.add_error_handler(error_handler)
            
            print("Бот запущен...")
            application.run_polling(allowed_updates=Update.ALL_TYPES)
            
        except Exception as e:
            print(f"Ошибка запуска бота: {e}")
            print("Перезапуск через 5 секунд...")
            time.sleep(5)

if __name__ == "__main__":
    import time
    from telegram import Update
    main()