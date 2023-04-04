# Импортируем необходимые классы.
import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from config import BOT_TOKEN
from datetime import datetime, date


# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def start(update, context):
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет {user.mention_html()}! Я эхо-бот. Напишите мне что-нибудь, и я пришлю это назад!",
    )


async def help_command(update, context):
    await update.message.reply_text("Я пока не умею помогать... Я только ваше эхо.")


async def time(update, context):
    now = datetime.now()
    await update.message.reply_text(now.strftime("%H:%M"))


async def d(update, context):
    now = date.today()
    await update.message.reply_text(f'{now}')


async def echo(update, context):
    await update.message.reply_text('Я получил сообщение: '+update.message.text)


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    text_handler = MessageHandler(filters.TEXT, echo)
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("time", time))
    application.add_handler(CommandHandler("dates", d))
    application.add_handler(text_handler)
    application.run_polling()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
