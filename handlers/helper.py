from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import command, other_filters2, other_filters



@Client.on_message(command("help") & other_filters2)
async def helper(ok, message: Message):
    await message.reply_text(
        f"""πThanks for useing this botπ

           BOT CAMMANDS 
 
/play <song name>

/urlplay <YouTube video link>

/skip  β©To the next song 

/stop π«to stop playing

/pause βΈοΈto pause the song

/resume βΆοΈTo continue The song

        πβ€οΈπ§‘πππππ€π€β€οΈ
        π€ @D3VIL_SUPPORT π€
        πβ€οΈπ§‘πππππ€π€β€οΈ""")

@Client.on_message(command("help") & other_filters)
async def ghelp(_, message: Message):
    await message.reply_text(f"**{bn} :-** Hey! [DM](http://t.me/D3VIL_MUSIC_BOT?start=help_) me to get all the commands π")
