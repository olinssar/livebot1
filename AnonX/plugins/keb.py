import asyncio
from config import OWNER_ID
import redis, re
from pyrogram import *
from dotenv import load_dotenv
from os import getenv
from AnonX import app
from pyrogram import Client, filters
from pyrogram.types import *
from pyrogram.errors import PeerIdInvalid



REPLY_MESSAGE = "اليك لوحه التحكم الخاصه بالاعضاء"

REPLY_MESSAGE_BUTTONS = [
         [
             ("المطور"),                   
             ("اوامر التشغيل")

          ],
          [
             ("طريقه التفعيل"),
             ("السورس") 
              ],
    [
        ("رويال شباب"),
        ("رويال بنات")
    ],
    [
        ("استوريهات. 🥹")
    ],
    [
        ("النقشبندي"),
        ("قران")
    ],
    [
        ("فيلمك. 🎥")
    ],
    [
        ("اقتباسات"),
        ("هيدرات")
    ],
    [
        ("غنيلي. 🎙")
    ],
    [
        ("صوره"),
        ("انميي")
    ],
    [
        ("متحركه. 🎬")
    ],
    [
        ("تويت"),
        ("صراحه")
    ],
    [
        ("الالعاب. 🐰")
    ],
    [
        ("نكته"),
        ("كتبات")
    ],
    [
        ("اذكار. 💎")
    ],
    [
        ("حساب العمر"),
        ("ابراج")
    ],
    [
        ("يـوتيوب. 📽")
        
    ],
    [
        ("لو خيروك"),
        ("انصحني")
    ],
    [
        ("بوت حذف")
        
    ],
    [
        ("حساب العمر"),
        ("ابراج")
    ],
    [
       ("انصحني. 🥲")
       
          ]
]

@app.on_message(filters.command("/Almortagel") & filters.private & ~filters.edited)
async def madison(client: Client, message: Message): 
    text = REPLY_MESSAGE
    reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    await message.reply(
        text=text,
        reply_markup=reply_markup
    )

@app.on_message(filters.private & command("طريقه التفعيل"))
async def addbot(client: Client, message: Message):
    await message.reply_text(f"""
❓ طريقة استخدام البوت

1.) اولا قم بإضافة البوت في مجموعتك.
2.) ثانيا قم برفعه مشرف اعطائه جميع الصلاحيات.
3.) قم بفتح الدردشة المرئيه قبل التشغيل.
4.) القي نظره علي الاوامر لتعلم طريقه التشغيل.

•⎆: قناه السورس @AlmortagelTech
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ قـناة الـسورس ›", url=f"https://t.me/AlmortagelTech"),
                ],[
                    InlineKeyboardButton(
                        "اضغط لاضافه البوت لمجموعتك", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



###################new lian#############

REPLY_MESSAGEE = "اليك لـوحه اوامر التشغيل"

REPLY_MESSAGE_BUTTONSS = [
         [
             ("اوامر القناة")
          ],
          [
             ("اوامر المجموعه") 
          ],
          [  
             ("اوامر المجموعة بالانجليزي")
          ],
          [
             ("اوامر مشتركة") 
          ],
          [
             ("اوامر مشتركة بالانجليزي")             
          ],
          [
             ("رجوع")
          ]
]

  
@app.on_message(filters.private & command("اوامر التشغيل"))
async def com(_, message: Message):             
        text = REPLY_MESSAGEE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONSS, resize_keyboard=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )



@app.on_message(filters.private & command("رجوع"))
async def bask(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )


@app.on_message(filters.private & command("اوامر القناة"))
async def mnsat(client: Client, message: Message):
    await message.reply_text(f"""
♚ مرحبا بك في اومر التشغيل بالقنوات

››  تشغيل ↫ اسم الاغنيه .
››  فيديو ↫ اسم الفديو .
››  انهاء ↫ لانهاء التشغيل في القناه .
››  تخطي ↫ لتخطي تشغيل القناه .
›› وقف ↫ لايقاف التشغيل مؤقتا في القناة
›› ربط القناه ↫ ايدي  القناه لربطها بالمجموعه .
›› مطور السورس ↫ @Almortagel_12

•⎆: قـناة السورس @AlmortagelTech
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      
                    InlineKeyboardButton(
                        "اضغط لاضافه البوت لمجموعتك", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),

                ],
            ]
        ),
        disable_web_page_preview=True
    )

@app.on_message(filters.private & command("اوامر المجموعه"))
async def laksk(client: Client, message: Message):
    await message.reply_text(f"""
♚ مرحبا بك في اوامر التشغيل في المجموعات

•اوامر التشغيل العربيه

›› تشغيل ↫ لتشغيل اغنية
›› فيديو ↫ لتشغيل فيديو 
›› تخطي ↫ لتخطي التشغيل الحالي
›› ايقاف ↫ لانتهاء التشغيل الحالي
›› وقف ↫ لايقاف التشغيل الحالي مؤقتا
›› استئناف ↫ لاستمرار التشغيل المتوقف
›› قائمة التشغيل ↫ لمعرفة التشغيل الحالي 
›› اعدادات ↫ لضبط اعدادات البوت
›› مطور السورس ↫ @Almortagel_12

•⎆: قـناه الـسورس @AlmortagelTech
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ قـناة الـسورس ›", url=f"https://t.me/AlmortagelTech"),
                ],[
                    InlineKeyboardButton(
                        "اضغط لاضافه البوت لمجموعتك", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )


@app.on_message(filters.private & command("اوامر المجموعة بالانجليزي"))
async def channvom(client: Client, message: Message):
    await message.reply_text(f"""
♚ مرحبا بك في اوامر التشغيل في المجموعات

•اوامر التشغيل الانجليزيه

/mplay - لتشغيل اغنيه
/vplay - لتشغيل فيديو
/playlist - لمعرفة قائمة التشغيل 
/skip - لتخطي التشغيل الحالي
/stop - ايقاف التشغيل الحالي
/pause - لايقاف التشغيل الحالي مؤقتا
/resume - استئناف التشغيل الحالي
/reload - تحديث قائمة الادمنية

›› جروب السورس @AlmortagelTech2

•⎆: قـناه الـسورس @AlmortagelTech

 """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ قـناة الـسورس ›", url=f"https://t.me/AlmortagelTech"),
                ],[
                    InlineKeyboardButton(
                        "اضغط لاضافه البوت لمجموعتك", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



@app.on_message(filters.private & command("اوامر مشتركة"))
async def dowmmr(client: Client, message: Message):
    await message.reply_text(f"""

  ♚ مرحبا بك في الاوامر المشتركه

•الاوامر المشتركه العربيه

›› تحميل ↫ لتحميل اغنية من اليوتيوب
›› تحميل فيديو ↫ لتحميل فيديو من اليوتيوب

•⎆: قـناه الـسورس @AlmortagelTech  
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ قـناة الـيورس ›", url=f"https://t.me/AlmortagelTech"),
                ],[
                    InlineKeyboardButton(
                        "اضغط لاضافه البوت لمجموعتك", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )
@app.on_message(filters.private & command("اوامر مشتركة بالانجليزي"))
async def dowhmr(client: Client, message: Message):
    await message.reply_text(f"""
♚ مرحبا بك في الاوامر المشتركه

•الاوامر المشتركه الانجليزيه

/song - تحميل اغنيه من يوتيوب
/video - تحميل فيديو من يوتيوب

•⎆: قـناه الـسورس @AlmortagelTech

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ قـناة الـسورس ›", url=f"https://t.me/AlmortagelTech"),
                ],[
                    InlineKeyboardButton(
                        "اضغط لاضافه البوت لمجموعتك", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )
@app.on_message(command(["صوره", "🕷", "صورهه", "صور"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/vnnkli/{rl}"
    await client.send_photo(message.chat.id,url,caption="🐉 ¦ تـم اختيـار صوره لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )


@app.on_message(command(["انميي", "انمي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/LoreBots7/{rl}"
    await client.send_photo(message.chat.id,url,caption="🐉 ¦ تـم اختيـار انمي لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )


@app.on_message(command(["متحركه. 🎬", "متحركه"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/GifWaTaN/{rl}"
    await client.send_animation(message.chat.id,url,caption="🐉 ¦ تـم اختيـار ملصق لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

@app.on_message(command(["اقتباسات", "اقتباس"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/LoreBots9/{rl}"
    await client.send_photo(message.chat.id,url,caption="🐉 ¦ تـم اختيـار اقتباس لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

@app.on_message(command(["هيدرا", "هيدرات"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/flflfldld/{rl}"
    await client.send_photo(message.chat.id,url,caption="🐉 ¦ تـم اختيـار هيدرات لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

@app.on_message(command(["صور", "افتار بنات"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/vvyuol/{rl}"
    await client.send_photo(message.chat.id,url,caption="🐉 ¦ تـم اختيـار صوره لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

@app.on_message(command(["صور شباب", "افتار شباب"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/vgbmm/{rl}"
    await client.send_photo(message.chat.id,url,caption="🐉 ¦ تـم اختيـار صوره لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
    
@app.on_message(command(["سوره", "قران"]))
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

@app.on_message(command(["الشيخ", "النقشبندي", "نقشبندي"]))
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

@app.on_message(command(["عبدالباسط", "عبدالباسط عبدالصمد"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(1,50)
    url = f"https://t.me/telawatnader/{rl}"
    await client.send_audio(message.chat.id,url,caption="🐉 ¦ تـم اختيـار الشيخ عبدالباسط لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )