# Credit Goes To www.github.com/Legend-Mukund
# <www.github.com/Legend-Mukund/META-ROBOT>

import random
import asyncio
from pyrogram import filters, __version__ as pver
from sys import version_info
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telethon import __version__ as tver
from telegram import __version__ as lver
from RocksAlexaRobot import BOT_USERNAME, OWNER_USERNAME, SUPPORT_CHAT, pgram

PHOTO = [
    "https://telegra.ph/file/4f51ea1bf4024a27838d2.jpg",
    "https://telegra.ph/file/2cdc3619dc9966bb8b0c2.jpg",
    "https://telegra.ph/file/7ae68204eacb4fb716e21.jpg",
    "https://telegra.ph/file/1a86496f3c59cb3f6df0c.jpg",
    "https://telegra.ph/file/362b0e068701bf0b06c10.jpg",
]

SHREYXD = [
    [
        InlineKeyboardButton(text="ʜᴇʟᴘ", url=f"https://t.me/ManagementXrobot?start=help"),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/WorldChattingFriendsWCF"),
    ],
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"http://t.me/ManagementXrobot?startgroup=true"),
    ],
]

@pgram.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(1)
    await accha.edit("ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.1)
    await accha.edit("ᴀʟɪᴠɪɴɢ...")
    await accha.delete()
    await asyncio.sleep(0.1)
    umm = await m.reply_sticker("CAACAgUAAx0CUldpJAACaqhjL6HDGrFDCTIYIvmcaURmCosuZAAC-AUAAlNueVXDMbXUWHZvDykE")
    await umm.delete()
    await asyncio.sleep(0.1)
    await m.reply_photo(
        random.choice(PHOTO),
        caption=f"""**ʜᴇʏ​ ɪ ᴀᴍ Queen ʀᴏʙᴏᴛ​**
        ━━━━━━━━━━━━━━━━━━━
        » **ᴍʏ ᴏᴡɴᴇʀ :** [Sangram](https://t.me/OpSangram)
        
        » **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{lver}`
        
        » **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tver}`
        
        » **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pver}`
        
        » **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{version_info[0]}.{version_info[1]}.{version_info[2]}`
        ━━━━━━━━━━━━━━━━━━━""",
        reply_markup=InlineKeyboardMarkup(SHREYXD)
    )
