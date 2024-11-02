from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Dictionary to store movie links
movie_links = {
    'Inception': 'https://example.com/inception',
    'Titanic': 'https://example.com/titanic',
    # Add more movies and links as needed
}

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome! Send me a movie name.')

def handle_message(update: Update, context: CallbackContext) -> None:
    movie_title = update.message.text
    link = movie_links.get(movie_title)
    if link:
        update.message.reply_text(f'Here is the link to {movie_title}: {link}')
    else:
        update.message.reply_text('Sorry, I don\'t have information on that movie.')

def main() -> None:
    # Replace 'YOUR_TOKEN' with your bot's API token
    updater = Updater("7615617551:AAGfcLer-oN0YpsptJx0G4Q3qghnkL0towo")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
