from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from config import ASSISTANT_NAME as bn


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""❓ CARA MENGGUNAKAN BOT:

1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @{bn} to your group.
4.) turn on the voice chat first before start to stream video.
5.) type /vstream (reply to video) to start streaming.
6.) type /vstop to end the video streaming.

📝 **Note: Stream & stop command cuman buat admin ya tolol!**

⚡ __Maintained by Veez Project Team__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "🏡 Go Back", callback_data="cbstart")
      ]]
    ))


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
  await query.edit_message_text(f"✨ **Hello tol, Gua telegram streaming bot.**\n\n💭 **gua  dibuat untuk melakukan streaming video dalam obrolan video grup dengan mudah.**\n\n❔ **Kalo mau gunain gua, lo pencet tombol di bawah ya tol** 👇🏻",
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
                             "👩🏻‍💻 Owner", url="https://t.me/Veernn")
                       ],[
                          InlineKeyboardButton(
                             "📚 Semua Command List", callback_data="cblist")
                       ]]
                    ))


@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""🌐 **bot information !**

🤖 __This bot was created to stream video in telegram group video chats using several methods from WebRTC.__

💡 __Powered by PyTgcalls the Async client API for the Telegram Group Calls, and Pyrogram the telegram MTProto API Client Library and Framework in Pure Python for Users and Bots.__

👨🏻‍💻 __Thanks to the developers who participated in the development of this bot, the list of devs can be seen below:__

🤵🏻 » [Vern](https://github.com/vellovernn)


__This bot licensed under GNU-GPL 3.0 License__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "🏡 Go Back", callback_data="cbstart")
      ]]
    ),
    disable_web_page_preview=True
  )

@Client.on_callback_query(filters.regex("cblist"))
async def cblist(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""📚 Semua Command List:

» /vstream (reply to video or file) - to stream video
» /vstop - end the video streaming
» /song (song name) - download song from YT
» /vsong (video name) - download video from YT
» /lyric (song name) - lyric scrapper

🎊 FUN CMD:

» /asupan - check it by yourself
» /chika - check it by yourself
» /wibu - check it by yourself
» /truth - check it by yourself
» /dare - check it by yourself

🔰 EXTRA CMD:

» /tts (reply to text) - text to speech
» /alive - check bot alive status
» /ping - check bot ping status
» /uptime - check bot uptime status
» /sysinfo - check bot system information

⚡ __Maintained by Vern Project Team__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "🏡 Go Back", callback_data="cbstart")
      ]]
    ))


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
