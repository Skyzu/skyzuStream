import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
SESSION_NAME = getenv("SESSION_NAME")
USERNAME_BOT = getenv("USERNAME_BOT", "Feritapibot")
OWNER_NAME = getenv("OWNER_NAME", "Xflicks")
COMMAND_PREFIXES = getenv("COMMAND_PREFIXES", "!")
SUDO_USERS = list(map(int, getenv("SUDO_USERS"))
