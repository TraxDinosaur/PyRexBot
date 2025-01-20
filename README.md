# PyBotRex

<p align="center">
  <img src="https://i.ibb.co/vVx1xfb/Picsart-25-01-20-22-05-41-616.png" alt="PyBotRex Logo" width="300"/>
</p>


**PyBotRex** simplifies Telegram bot development with an intuitive interface for commands, messaging, buttons, and more. Build interactive Telegram bots effortlessly with a clean and reusable design.

---

## 🚀 Features

- **Command Handling**: Easily add commands with custom callbacks.
- **Message Handling**: Process messages with text or media filters.
- **Inline Buttons**: Create interactive inline keyboard buttons.
- **Advanced Features**: Inline queries, error handling, and custom updates.
- **Async Support**: Fully asynchronous with `python-telegram-bot` 20.0+.

---

## 🛠 Installation

Install PyBotRex using pip:

```bash
pip install PyBotRex
```

---

## 📦 Quick Start

Here’s how you can build a basic bot:

```python
from PyBotRex import PyBotRex
from telegram import Update
from telegram.ext import ContextTypes

# Initialize the bot
bot = PyBotRex("YOUR_TELEGRAM_BOT_TOKEN")

# Define a command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await bot.reply(update, "Welcome to PyBotRex!")

# Add the command
bot.add_command("start", start_command)

# Run the bot
bot.start()
```

---

## 📚 Documentation

Full documentation is available [here](https://github.com/TraxDinosaur/PyRexBot/wiki/PyRexBot).

---


## 🐛 Issues

Encountered a bug? Report it [here](https://github.com/TraxDinosaur/PyRexBot/issues).

---

## 📜 License

This project is licensed under the **CC-BY-SA 4.0**. See the [LICENSE](https://github.com/TraxDinosaur/PyRexBot/blob/main/LICENSE) for more details.

---

## 🌟 Acknowledgments

Thanks to the community and contributors of `python-telegram-bot` for providing the foundation that made PyBotRex possible.

---

## 📬 Contact

- **Author**: TraxDinosaur  
- **Website**: [TraxDinosaur.github.io](https://traxdinosaur.github.io)  
- **GitHub**: [TraxDinosaur](https://github.com/TraxDinosaur)  

---

Happy Bot Building with PyBotRex! 🦖🤖
