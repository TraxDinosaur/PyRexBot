import setuptools

# Package metadata
NAME = "PyRexBot"
VERSION = "1.0.0"
DESCRIPTION = "PyBotRex simplifies Telegram bot creation with a clean and intuitive interface for commands, messaging, buttons, and more."
URL = "https://github.com/TraxDinosaur/PyRexBot"
AUTHOR = "TraxDinosaur"
AUTHOR_CONTACT = "https://traxdinosaur.github.io"
LICENSE = "CC-BY-SA 4.0"
KEYWORDS = [
    "Telegram Bot", "Python Telegram Bot", "Telegram API", "Bot Development", "Python Bot Library",
    "Interactive Bots", "PyBotRex", "Bot Framework", "Telegram Python Bot", "Telegram Bot Toolkit"
]

# Read long description from README.md
with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

# Packages required by the project
REQUIRED_PACKAGES = [
    "python-telegram-bot>=20.0"
]

setuptools.setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_contact=AUTHOR_CONTACT,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=URL,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved",
        "Operating System :: OS Independent",
    ],
    keywords=KEYWORDS,
    install_requires=REQUIRED_PACKAGES,
    python_requires=">=3.7",
)