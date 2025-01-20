from telegram import Update, BotCommand, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    InlineQueryHandler,
    filters,
    ContextTypes
)


class PyRexBot:
    """
    A simplified Telegram bot wrapper for building bots using python-telegram-bot.
    Provides an intuitive API for managing commands, messages, and more.
    """

    def __init__(self, token: str):
        """
        Initialize the bot application.
        
        :param token: The Telegram bot token provided by BotFather.
        """
        self.app = Application.builder().token(token).build()

    def start(self, webhook_url=None, port=8443):
        """
        Start the bot using polling or webhook.
        
        :param webhook_url: The URL for webhook mode. If None, the bot will use polling.
        :param port: Port for webhook mode. Default is 8443.
        """
        if webhook_url:
            self.app.run_webhook(listen="0.0.0.0", port=port, webhook_url=webhook_url)
        else:
            self.app.run_polling()

    def add_command(self, name: str, callback):
        """
        Add a command handler for the bot.
        
        :param name: The command name (e.g., "start" for /start).
        :param callback: The async function to handle the command.
        """
        self.app.add_handler(CommandHandler(name, callback))

    def handle_message(self, callback, text_only=True):
        """
        Add a message handler to the bot.
        
        :param callback: The async function to handle incoming messages.
        :param text_only: If True, handles only text messages. Default is True.
        """
        filter_rule = filters.TEXT if text_only else filters.ALL
        self.app.add_handler(MessageHandler(filter_rule, callback))

    def handle_button_click(self, callback):
        """
        Add a handler for inline button clicks.
        
        :param callback: The async function to handle button clicks.
        """
        self.app.add_handler(CallbackQueryHandler(callback))

    def handle_inline_query(self, callback):
        """
        Add a handler for inline queries.
        
        :param callback: The async function to handle inline queries.
        """
        self.app.add_handler(InlineQueryHandler(callback))

    async def set_commands(self, commands: dict):
        """
        Set bot commands for the menu.
        
        :param commands: A dictionary where keys are command names and values are descriptions.
        """
        bot_commands = [BotCommand(name, desc) for name, desc in commands.items()]
        await self.app.bot.set_my_commands(bot_commands)

    async def send_text(self, chat_id: int, text: str, buttons=None):
        """
        Send a text message.
        
        :param chat_id: The ID of the chat to send the message to.
        :param text: The text of the message.
        :param buttons: Optional inline buttons as a list of lists of tuples [(text, callback_data)].
        """
        markup = InlineKeyboardMarkup(buttons) if buttons else None
        await self.app.bot.send_message(chat_id=chat_id, text=text, reply_markup=markup)

    async def send_photo(self, chat_id: int, photo, caption=None, buttons=None):
        """
        Send a photo.
        
        :param chat_id: The ID of the chat to send the photo to.
        :param photo: The photo file (file ID, URL, or file object).
        :param caption: Optional caption for the photo.
        :param buttons: Optional inline buttons.
        """
        markup = InlineKeyboardMarkup(buttons) if buttons else None
        await self.app.bot.send_photo(chat_id=chat_id, photo=photo, caption=caption, reply_markup=markup)

    async def send_file(self, chat_id: int, file, caption=None, buttons=None):
        """
        Send a file.
        
        :param chat_id: The ID of the chat to send the file to.
        :param file: The file to send (file ID, URL, or file object).
        :param caption: Optional caption for the file.
        :param buttons: Optional inline buttons.
        """
        markup = InlineKeyboardMarkup(buttons) if buttons else None
        await self.app.bot.send_document(chat_id=chat_id, document=file, caption=caption, reply_markup=markup)

    async def send_video(self, chat_id: int, video, caption=None, buttons=None):
        """
        Send a video.
        
        :param chat_id: The ID of the chat to send the video to.
        :param video: The video file (file ID, URL, or file object).
        :param caption: Optional caption for the video.
        :param buttons: Optional inline buttons.
        """
        markup = InlineKeyboardMarkup(buttons) if buttons else None
        await self.app.bot.send_video(chat_id=chat_id, video=video, caption=caption, reply_markup=markup)

    async def reply(self, update: Update, text: str, buttons=None):
        """
        Reply to a message.
        
        :param update: The update object containing the message.
        :param text: The text to reply with.
        :param buttons: Optional inline buttons.
        """
        markup = InlineKeyboardMarkup(buttons) if buttons else None
        await update.message.reply_text(text, reply_markup=markup)

    async def edit_message(self, chat_id: int, message_id: int, new_text: str, buttons=None):
        """
        Edit an existing message.
        
        :param chat_id: The ID of the chat where the message is located.
        :param message_id: The ID of the message to edit.
        :param new_text: The new text for the message.
        :param buttons: Optional inline buttons.
        """
        markup = InlineKeyboardMarkup(buttons) if buttons else None
        await self.app.bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=new_text, reply_markup=markup)

    async def delete_message(self, chat_id: int, message_id: int):
        """
        Delete a message.
        
        :param chat_id: The ID of the chat where the message is located.
        :param message_id: The ID of the message to delete.
        """
        await self.app.bot.delete_message(chat_id=chat_id, message_id=message_id)

    async def get_user(self, user_id: int):
        """
        Get details of a user or chat.
        
        :param user_id: The ID of the user or chat.
        :return: A Chat object containing user details.
        """
        return await self.app.bot.get_chat(user_id)

    def create_buttons(self, button_data: list[tuple[str, str]]):
        """
        Create inline buttons for messages.
        
        :param button_data: A list of tuples where each tuple is (button_text, callback_data).
        :return: A list of InlineKeyboardButton objects.
        """
        return [[InlineKeyboardButton(text, callback_data=data)] for text, data in button_data]

    def handle_errors(self, callback):
        """
        Add a global error handler.
        
        :param callback: The async function to handle errors.
        """
        self.app.add_error_handler(callback)

    def listen(self, update_handler):
        """
        Add a custom update handler for advanced use cases.
        
        :param update_handler: The custom handler to add.
        """
        self.app.add_handler(update_handler)

    async def get_bot_info(self):
        """
        Get information about the bot.
        
        :return: A User object with bot details.
        """
        return await self.app.bot.get_me()

    async def stop(self):
        """
        Stop the bot application.
        """
        await self.app.stop()
