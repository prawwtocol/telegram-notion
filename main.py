import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
)
import config
from notion import create_notion_page
import os

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!"
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    create_notion_page(update.message.text)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Created notion task: {update.message.text}",
    )


if __name__ == "__main__":
    application = ApplicationBuilder().token(config.BOT_TOKEN).build()

    start_handler = CommandHandler("start", start)
    echo_handler = MessageHandler(filters.TEXT, echo)
    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    port = int(os.environ.get("PORT", 5000))
    application.run_webhook(
        listen="0.0.0.0",
        port=port,
        url_path=config.BOT_TOKEN,
        webhook_url=f"https://fa9d0sf-7e30cea95529.herokuapp.com/{config.BOT_TOKEN}",
    )
