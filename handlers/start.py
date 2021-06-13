from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Merhaba👋 Telegeam Gruplarının sesli sohbetlerinde müzik çalabiliyorum.
        Seni şaşırtacak bir sürü harika özelliğim var!
        Telegram gruplarının sesli sohbetlerinde müzik çalmamı ister misin?
        Beni nasıl kullanabileceğinizi öğrenmek için lütfen aşağıdaki \ '📜 Kullanım Kılavuzu 📜 \' düğmesini tıklayın.
        Grubunuzun sesli sohbetinde müzik çalabilmek için Asistanın grubunuzda olması gerekir.""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📜 Kullanım Kılavuzu 📜", url="https://telegra.ph/Sohbet-Muzik-Bot-06-13")
                  ],[
                    InlineKeyboardButton(
                        "👨‍💻 Güncellemeler 👨‍💻", url="https://t.me/SohbetCilginlariBotlar"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Destek Grubu 🎙️", url="https://t.me/SohbetMuzikDestek"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**🔴 Müzik Oynatıcı Aktif**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎙️ Destek Grubu 🎙️", url="https://t.me/SohbetMuzikDestek")
                ]
            ]
        )
   )
