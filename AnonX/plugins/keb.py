import asyncio
from pyrogram import Client, filters
from random import choice
from pyrogram import filters
from strings import get_command
from strings.filters import command
from config import BANNED_USERS
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, ChatJoinRequest

#كسمك تحياتي😂
REPLY_MESSAGE = "**🧑🏻‍✈️︙اهلا بك بك عزيزي المطور الاساسي ♥️**\n**⤵️︙ اليـكـ ازرار التحـكـم خاصة ب سورس الميوزك💞**"

REPLY_MESSAGE_BUTTONS = [
    [
             ("المطور"),                   
             ("سورس")

          ],
          [
             ("لو خيروك"),
             ("كت تويت") 
          ],
          [
             ("اذكار"),
             ("صراحه") 
          ],
          [
             ("غيلي"),
             ("سوال") 
          ],
          [
             ("نقشبندي"),
             ("عبدالباسط")           
          ],
          [
             ("الالعاب"),
        ("❎ ¦ حذف الكيبورد")
    ]
]

@app.on_message(command("/almortagel") & filters.private & ~filters.edited)
async def madison(client: Client, message: Message): 
    text = REPLY_MESSAGE
    reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    await message.reply(
        text=text,
        reply_markup=reply_markup
    )


@app.on_message(command("❎ ¦ حذف الكيبورد") & filters.private & ~filters.edited)
async def upbkgt(client: Client, message: Message):
    await message.reply_text(
        text="""❎ ¦ تم حذف الكيبورد بنجاح""",
        reply_markup=ReplyKeyboardRemove()
    )


    
    @app.on_message(command(["عبدالباسط", "عبدالباسط عبدالصمد"], ""))
async def upbkgt(client: Client, message: Message):
    rl = random.randint(1,50)
    url = f"https://t.me/telawatnader/{rl}"
    await client.send_audio(message.chat.id,url,caption="🥹♥ ¦ تـم اختيـار الشيخ عبدالباسط لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )