"""
tg-stream-video, An Telegram Bot Project
Copyright (c) 2021 GalihMrd <https://github.com/Imszy17>
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.
You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram import Client, filters
from lib.config import USERNAME_BOT


BOKEP = "https://telegra.ph/file/1e78b509a59fe6c04362a.mp4"
START_MESSAGE = """**I'm Online and ready to streaming your video on your Voice Chat Group**"""


@Client.on_message(filters.command("start"))
async def start(client, message):
    coli = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("How to use ❔", callback_data="cbhelp"),
            ]
        ]
    )
    await client.send_video(message.chat.id, BOKEP, caption=START_MESSAGE, reply_markup=coli)
