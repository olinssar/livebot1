import asyncio
import config
from pyrogram import Client, filters
from pyrogram import filters
from strings import get_command
from strings.filters import command
from AnonX import app
from config import OWNER_ID
from AnonX.misc import SUDOERS
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX.misc import SUDOERS

@Client.on_message(filters.command(["/Almortagel", ": رجوع للقائمة الرئيسيه :"], ""))
async def start(client, message):
 if not message.chat.type == enums.ChatType.PRIVATE:
    if await joinch(message):
            return
 bot_username = client.me.username
 dev = await get_dev(bot_username)
 nn = await get_dev_name(client, bot_username)
 if message.chat.id == dev or message.chat.username in OWNER:
   kep = ReplyKeyboardMarkup([[": السورس :"], [": تعين اسم البوت :"],[": تعين قناة السورس :",": تعين مجموعة السورس :"],[": تعين لوجو السورس :",": تعين يوزر مطور السورس :"], [": المكالمات النشطه :"], [": تفعيل الاشتراك الإجباري :", ": تعطيل الاشتراك الإجباري :"], [": تعين مجموعة البوت :", ": تعين قناة البوت :"], [": المجموعات :", ": المستخدمين :"], [": الاحصائيات :"], [": قسم الإذاعة :"], [": قسم التحكم في المساعد :"], [": تغير مكان سجل التشغيل :"], [": تفعيل سجل التشغيل :"], [": تعطيل سجل التشغيل :"], [": تفعيل التواصل :", ": تعطيل التواصل :"]], resize_keyboard=True)
   return await message.reply_text("**مرحباً بك عزيزي المطور**\n**يمكنك التحكم ف البوت من خلال الازرار**", reply_markup=kep)
 else:
  kep = ReplyKeyboardMarkup([[": مطور البوت :", ": مطور السورس :"], [": السورس :",": بنج :"], [": رمزيات :",": استوري :"],[": صور انمي :"],[": تويت :", ": صراحه :"],[": نكته :",": احكام :"],[": الاوامر :"],[":  لو خيروك :",": انصحني :"],[": اغنية عشوائية :"],[": اذكار :",": كتابات :"],[": حروف :",": بوت :"],[": قران الكريم :",": استوري قران :"],[": رمزيات بنات :",": المزيد من الصور :"]], resize_keyboard=True)
  await message.reply_text("اهلا عزيزي اليك كيب الاعضاء : ◗⋮◖", reply_markup=kep)
  @Client.on_message(filters.command(": تعين اسم البوت :", ""))
async def set_bot(client: Client, message):
   NAME = await client.ask(message.chat.id, "ارسل اسم البوت الجديد", filters=filters.text, timeout=30)
   BOT_NAME = NAME.text
   bot_username = client.me.username
   await set_bot_name(bot_username, BOT_NAME)
   await message.reply_text("**تم تعين اسم البوت بنجاح -🖱️**")

@Client.on_message(filters.command(["بوت", "البوت",": بوت :"], ""))
async def bottttt(client: Client, message: Message):
    bot_username = client.me.username
    BOT_NAME = await get_bot_name(bot_username)
    bar = random.choice(selections).format(BOT_NAME)
    await message.reply_text(f"**[{bar}](https://t.me/{bot_username}?startgroup=True)**", disable_web_page_preview=True)
    
@Client.on_message(filters.command(": تعين لوجو السورس :", ""))
async def set_vi_so(client: Client, message):
   NAME = await client.ask(message.chat.id, "ارسل رابط لوجو السورس \nمثال:-\n https://telegra.ph/file/202fb7bab05c41e550fb5.jpg", filters=filters.text, timeout=30)
   VID_SO = NAME.text
   bot_username = client.me.username
   await set_video_source(bot_username, VID_SO)
   await message.reply_text("تم تعين لوجو السورس  بنجاح -⌯")
   
@Client.on_message(filters.command(": تعين يوزر مطور السورس :", ""))
async def set_dev_username(client: Client, message):
   NAME = await client.ask(message.chat.id, "ارسل معرف المطور الجديد", filters=filters.text, timeout=300)
   CH_DEV_USER = NAME.text
   bot_username = client.me.username
   await set_dev_user(bot_username, CH_DEV_USER)
   await message.reply_text("تم تعين المطور بنجاح -⌯")

@Client.on_message(filters.command(": تعين قناة البوت :", ""))
async def set_botch(client: Client, message):
   NAME = await client.ask(message.chat.id, "ارسل رابط القناه البوت الجديدة", filters=filters.text)
   channel = NAME.text
   bot_username = client.me.username
   await set_channel(bot_username, channel)
   await message.reply_text("**تم تعين قناه البوت بنجاح -🖱️**")

@Client.on_message(filters.command(": تعين مجموعة البوت :", ""))
async def set_botgr(client: Client, message):
   NAME = await client.ask(message.chat.id, "ارسل رابط الجروب الجديد", filters=filters.text)
   group = NAME.text
   bot_username = client.me.username
   await set_group(bot_username, group)
   await message.reply_text("**تم تعين مجموعه البوت بنجاح -🖱️**")

@Client.on_message(filters.command(": تعين قناة السورس :", ""))
async def set_botchsr(client: Client, message):
   NAME = await client.ask(message.chat.id, "ارسل رابط القناه البوت الجديدة", filters=filters.text)
   channelsr = NAME.text
   bot_username = client.me.username
   await set_channelsr(bot_username, channelsr)
   await message.reply_text("**تم تعين قناه السورس بنجاح -🖱️**")

@Client.on_message(filters.command(": تعين مجموعة السورس :", ""))
async def set_botgrsr(client: Client, message):
   NAME = await client.ask(message.chat.id, "ارسل رابط الجروب الجديد", filters=filters.text)
   groupsr = NAME.text
   bot_username = client.me.username
   await set_groupsr(bot_username, groupsr)
   await message.reply_text("**تم تعين مجموعه السورس بنجاح -🖱️**")
   
async def set_must(bot_username: dict, m: str):
    if m == ": تعطيل الاشتراك الإجباري :":
      ii = "معطل"
    else:
      ii = "مفعل"
    must[bot_username] = ii
    mustdb.update_one({"bot_username": bot_username}, {"$set": {"getmust": ii}}, upsert=True)
    
@Client.on_message(filters.command([": تعطيل الاشتراك الإجباري :", ": تفعيل الاشتراك الإجباري :"], ""))
async def set_join_must(client: Client, message):
   bot_username = client.me.username
   m = message.command[0]
   await set_must(bot_username, m)
   if message.command[0] == ": تعطيل الاشتراك الإجباري :":
     await message.reply_text("**تم تعطيل الاشتراك الإجباري بنجاح -🖱️**")
   else:
     await message.reply_text("**تم تفعيل الاشتراك الإجباري بنجاح -🖱️**")
