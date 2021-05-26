from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I can play music in your group's voice call. Developed by [D3_krish For D3VIL support](https://t.me/D3VIL_SUPPORT).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Source Code 🛠", url="https://github.com/D3KRISH/D3VILMUSICBOT")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/D3VIL_BOT_SUPPORT"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/D3VIL_SUPPORT"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "❗IF ANY PROBLEM CLICK HERE❗", url="https://t.me/D3_krish"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/D3VIL_SUPPORT")
                ]
            ]
        )
   )


