from time import time
from datetime import datetime
from helpers.filters import command
from helpers.decorators import sudo_users_only
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, Chat, CallbackQuery
from config import BOT_USERNAME


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, m: Message):
   if m.chat.type == "private":
      await m.reply(f"✨ **Hello tol, gua telegram video streaming bot.**\n\n💭 **gua dibuat untuk melakukan streaming video dalam obrolan video grup dengan mudah.**\n\n❔ **Kalo gak bisa gunain gua, teken tombolnya di bawah tolol! ** 👇🏻",
                    reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "❔ CARA MENGGUNAKAN BOT", callback_data="cbguide")
                       ],[
                          InlineKeyboardButton(
                             "🌐 Terms & Condition", callback_data="cbinfo")
                       ],[
                          InlineKeyboardButton(
                             "💬 Group", url="https://t.me/NaughtyBoysGirls"),
                          InlineKeyboardButton(
                             "📣 Channel", url="https://t.me/AsupanVern")
                       ],[
                          InlineKeyboardButton(
                             "👩🏻‍💻 OWNER", url="https://t.me/Veernn")
                       ],[
                          InlineKeyboardButton(
                             "📚 SEMUA Command List", callback_data="cblist")
                       ]]
                    ))
   else:
      await m.reply("**✨ Bot Udah Onlen Tol ✨**",
                          reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "❔ CARA MENGGUNAKAN BOT", callback_data="cbguide")
                       ],[
                          InlineKeyboardButton(
                             "🌐 Mencari Youtube", switch_inline_query='')
                       ],[
                          InlineKeyboardButton(
                             "📚 Command List", callback_data="cblist")
                       ]]
                    )
      )


@Client.on_message(command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def alive(_, m: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m.reply_text(
        f"""✅ **bot sedang di jalankan**\n<b>💠 **uptime:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨ Group", url=f"https://t.me/NaughtyBoysGirls"
                    ),
                    InlineKeyboardButton(
                        "📣 Channel", url=f"https://t.me/AsupanVern"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(_, m: Message):
    start = time()
    m_reply = await m.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "🏓 `PONG!!`\n"
        f"⚡️ `{delta_ping * 1000:.3f} ms`"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(_, m: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )
