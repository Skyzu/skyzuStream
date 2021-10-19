"""
VideoStream, An Telegram Bot Project
Copyright (c) 2021 FeriExp <https://github.com/Feriexp>
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

import asyncio
import pafy
from pyrogram import Client, filters
from youtube_search import YoutubeSearch
from lib.tg_stream import call_py
from lib.helpers.filters import private_filters, public_filters
from pytgcalls import idle
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioImagePiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import MediumQualityVideo, MediumQualityAudio
from pytgcalls.exceptions import NoActiveGroupCall


@Client.on_message(filters.command("vplay") & public_filters)
async def play_video(client, message):
    flags = " ".join(message.command[1:])
    replied = message.reply_to_message
    text = message.text.split(None, 2)[1:]
    user = message.from_user.mention
    try:
        if text[0] == "channel":
            chat_id = int(message.chat.title)
            try:
                input = text[1]
            except Exception:
                pass
        else:
            chat_id = message.chat.id
            input = text[0]
    except Exception:
        pass
    if not replied:
        try:
            msg = await message.reply("```Processing...```")
            video = pafy.new(input)
            file = video.getbest().url
            title = video.title
        except Exception as e:
            await msg.edit(f"**Error:** {e}")
            return False
        await msg.edit(f"**Streamed by: {user}**\n**Title:** ```{title}```")
        try:
           await call_py.join_group_call(
               chat_id,
               AudioVideoPiped(
                   file,
                   MediumQualityAudio(),
                   MediumQualityVideo()
               ),
               stream_type=StreamType().live_stream
           )
        except NoActiveGroupCall:
           await msg.edit("**Error:** No active group call, please open group call first")
    elif replied.video or replied.document:
        flags = " ".join(message.command[1:])
        chat_id = int(message.chat.title) if flags == "channel" else message.chat.id
        msg = await message.reply("```Downloading from telegram...```")
        file = await client.download_media(replied)
        await msg.edit(f"**Streamed by: {user}**")
        try:
           await call_py.join_group_call(
               chat_id,
               AudioVideoPiped(
                   file,
                   MediumQualityAudio(),
                   MediumQualityVideo()
               ),
               stream_type=StreamType().live_stream
           )
        except NoActiveGroupCall:
           await msg.edit("**Error:** No active group call, please open group call first")
    elif replied.audio:
        flags = " ".join(message.command[1:])
        chat_id = int(message.chat.title) if flags == "channel" else message.chat.id
        msg = await message.reply("```Downloading from telegram...```")
        input_file = await client.download_media(replied)
        await msg.edit(f"**Streamed by: {user}**")
        try:
           await call_py.join_group_call(
               chat_id,
               AudioImagePiped(
                   input_file,
                   './etc/banner.png',
                   video_parameters=MediumQualityVideo(),
               ),
               stream_type=StreamType().pulse_stream,
           )
        except NoActiveGroupCall:
           await msg.edit("**Error:** No active group call, please open group call first")
    else:
        await message.reply("Error!")


@call_py.on_stream_end()
async def end(cl, update):
    print("stream ended in " + str(update.chat_id))
    await call_py.leave_group_call(update.chat_id)
