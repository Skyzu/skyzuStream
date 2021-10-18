import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SESSION_NAME = os.getenv("SESSION_NAME")
USERNAME_BOT = os.getenv("USERNAME_BOT", "Feritapibot")
OWNER_NAME = os.getenv("OWNER_NAME", "Xflicks")
COMMAND_PREFIXES = os.getenv("COMMAND_PREFIXES", "!")
SUDO_USERS = list(map(int, getenv("SUDO_USERS"))
