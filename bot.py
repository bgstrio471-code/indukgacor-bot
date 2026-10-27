import os, logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💎 Beli Induk Gacor", callback_data="beli")],
        [InlineKeyboardButton("📋 Daftar Harga", callback_data="harga")],
        [InlineKeyboardButton("📞 Hubungi Admin", callback_data="admin")]
    ]
    text = "🔥 INDUK GACOR STORE 🔥\n\nSelamat datang! Pilih menu di bawah:"
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    if q.data == "beli":
        await q.edit_message_text("💎 Untuk beli, ketik jenis induk yang mau dibeli. Admin akan balas!", parse_mode="Markdown")
    elif q.data == "harga":
        await q.edit_message_text("📋 DAFTAR HARGA\n\nBetina: 150k\nJantan: 200k\nPaket 1J+3B: 600k", parse_mode="Markdown")
    elif q.data == "admin":
        await q.edit_message_text("📞 Hubungi: @admin_indukgacor")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Pesan diterima! Admin akan segera balas.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
