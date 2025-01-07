from telegram import Update, InputFile
from telegram.ext import Application, CommandHandler, ContextTypes

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    # Sending a welcome message
    await update.message.reply_text("Welcome to the Bot! Here's an image for you:")

    # Sending an image file
    with open('download.png', 'rb') as image:
        await context.bot.send_photo(chat_id=chat_id, photo=image)

def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    application = Application.builder().token("7643444089:AAENsuoSdFA7sPxN6DFuswwJN3wC8ge1Xfk").build()
    
    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    
    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
