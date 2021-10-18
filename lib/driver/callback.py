from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""👋🏻 **Hi {message.from_user.mention} !**
**I'm online and ready for playing video.**
**For more information, hit the » 📚 `Command` bellow**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                   InlineKeyboardButton(
                       "📚 Command", callback_data="cbhelp"
                   )
                ]
             ]
          ),
       )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(f"""It os the help menu for streaming!
You can find how to use me on the button bellow.""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "Help Play", callback_data="cbplay"),
                    InlineKeyboardButton(
                        "Help Pause​​", callback_data="cbpause"
                    ),
                 ],
                 [
                    InlineKeyboardButton(
                        "Help Resume", callback_data="cbresume"),
                    InlineKeyboardButton(
                        "Help Stop", callback_data="cbstop"
                    )
                 ],
                 [
                    InlineKeyboardButton(
                        "Home", callback_data="cbstart"
                    )
                 ]
             ]
         ),
     )


@Client.on_callback_query(filters.regex("cbplay"))
async def cbplay(_, query: CallbackQuery):
    await query.edit_message_text("""**[HELP MESSAGE]**

**>> Description:** ```to streaming video in video chat group/channel```

**[GUIDE]**

**>> Group:** ```/play [reply to video/audio/give youtube url]```
**>> Channel:** ```/play [channel] [reply to video/audio/give youtube url]```

**>> Note:** ```To stream in channel stream you must replace chat title to Channel ID```""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "🔙 Back", callback_data="cbhelp"
                    )
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbpause"))
async def cbpause(_, query: CallbackQuery):
    await query.edit_message_text("""**[HELP MESSAGE]**

**>> Description:** ```To pause stream in video chat group/channel```

**[GUIDE]**

**>> Group:** ```/pause```
**>> Channel:** ```/pause [channel]```

**>> Note:** ```Replace chat title to pause channel stream```""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "🔙 Back", callback_data="cbhelp"
                    )
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbresume"))
async def cbresume(_, query: CallbackQuery):
    await query.edit_message_text("""**[HELP MESSAGE]**

**>> Description:** ```To resume stream in video chat grouo/channel```

**[GUIDE]**

**>> Group:** ```/resume```
**>> Channel:** ```/resume [channel]```

**>> Note:** ```Replace chat title to resume channel stream```""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "🔙 Back", callback_data="cbhelp"
                    )
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbstop"))
async def cbstop(_, query: CallbackQuery):
    await query.edit_message_text("""**[HELP MESSAGE]**

**>> Description:** ```To stop stream in video chat grouo/channel```

**[GUIDE]**

**>> Group:** ```/stop```
**>> Channel:** ```/stop [channel]```

**>> Note:** ```Replace chat title to stop channel stream```""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "🔙 Back", callback_data="cbhelp"
                    )
                ]
            ]
        ),
    )


