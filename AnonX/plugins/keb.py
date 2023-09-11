import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from Anonx import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


REPLY_MESSAGE = "اليك لوحه التحكم الخاصه بالاعضاء"

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
             ("قفل الكيب") 
          ]
]

@app.on_message(filters.command("Almortagel") & filters.private & ~filters.edited)
async def madison(client: Client, message: Message): 
    text = REPLY_MESSAGE
    reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    await message.reply(
        text=text,
        reply_markup=reply_markup
    )
    
    @app.on_message(command("^اخفاء الازرار . 🕷$") & filters.private & ~filters.edited)
async def upbkgt(client: Client, message: Message):
    await message.reply_text(text="تم الازرار بنجاح .🕷",
        reply_markup=ReplyKeyboardRemove()
    )

    @app.on_message(filters.command(["سوره", "قران"], ""))
async def ihd(client: Client, message: Message):
    rl = random.randint(1,90)
    url = f"https://t.me/opuml/{rl}"
    await client.send_voice(message.chat.id,url,caption="🐉 ¦ تـم اختيـار ايـه قرآنيه لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

@app.on_message(filters.command(["الشيخ", "النقشبندي", "نقشبندي"], ""))
async def ihd(client: Client, message: Message):
    rl = random.randint(1,90)
    url = f"https://t.me/ggcnjj/{rl}"
    await client.send_voice(message.chat.id,url,caption="🥹♥ ¦ تـم اختيـار الشيخ نقشبندي لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
    
    @app.on_message(filters.command(["عبدالباسط", "عبدالباسط عبدالصمد"], ""))
async def ihd(client: Client, message: Message):
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