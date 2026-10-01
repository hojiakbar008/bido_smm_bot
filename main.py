import telebot
from telebot import types

# 1. BOT TOKENINI KIRITISH
# Diqqat: SIZNING_BOT_TOKENINGIZ_SHU_YERDA degan yozuv o'rniga @BotFather bergan tokeningizni qo'ying.
# Qavslar ( ' ' ) o'chib ketmasin!
TOKEN = '8717877939:AAH0NFHpZ-m5IXYm1FnjbiuZH90IGoFVeeU'
bot = telebot.TeleBot(TOKEN)

# 2. START BUYRUG'I VA ASOSIY MENYU
# Foydalanuvchi botga kirganda shu qism ishlaydi
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Asosiy menyu klaviaturasini yaratish (2 ta qator)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    
    # Tugmalarni yasash
    btn1 = types.KeyboardButton("👤 Profilim")
    btn2 = types.KeyboardButton("⚙️ Sozlamalar")
    btn3 = types.KeyboardButton("📞 Aloqa")
    btn4 = types.KeyboardButton("ℹ️ Ma'lumot")
    
    # Tugmalarni menyuga qo'shish
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)

    bot.send_message(
        message.chat.id, 
        f"Salom, {message.from_user.first_name}! Xush kelibsiz.\n\nKerakli bo'limni tanlang:", 
        reply_markup=markup
    )

# 3. TUGMALAR VA MATNLARNI QAYTA ISHLASH (Yangi bo'limlarni shu yerga qo'shasiz)
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if message.text == "👤 Profilim":
        user_id = message.from_user.id
        username = message.from_user.username
        text = f"Sizning Telegram ID raqamingiz: {user_id}\nUsername: @{username}"
        bot.send_message(message.chat.id, text)
        
    elif message.text == "⚙️ Sozlamalar":
        # Xabar tagida chiqadigan (Inline) tugmalar
        inline_markup = types.InlineKeyboardMarkup(row_width=2)
        btn_lang = types.InlineKeyboardButton("🇺🇿 Tilni tanlash", callback_data="lang")
        btn_notif = types.InlineKeyboardButton("🔔 Bildirishnomalar", callback_data="notif")
        inline_markup.add(btn_lang, btn_notif)
        
        bot.send_message(message.chat.id, "Sozlamalar paneli:", reply_markup=inline_markup)
        
    elif message.text == "📞 Aloqa":
        bot.send_message(message.chat.id, "Admin bilan bog'lanish: @SizningUsername \nBizning kanal: @SizningKanal")
        
    elif message.text == "ℹ️️ Ma'lumot":
        bot.send_message(message.chat.id, "Bu bot mukammal va kelajakda rivojlantirish oson bo'lishi uchun tayyorlangan! 🚀")
        
    else:
        # Menyu tugmalaridan boshqa so'z yozilsa shu javob qaytadi
        bot.send_message(message.chat.id, "Kechirasiz, bu buyruqni tushunmadim. Menyudan foydalaning.")

# 4. INLINE TUGMALAR BOSILGANDA ISHLAYDIGAN QISM (Callback)
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "lang":
        bot.answer_callback_query(call.id, "Hozircha faqat O'zbek tili mavjud 😊", show_alert=True)
    elif call.data == "notif":
        bot.answer_callback_query(call.id, "Bildirishnomalar yoqilgan 🔔")

# Bot to'xtab qolmasdan doimiy ishlab turishi uchun kod
print("Bot muvaffaqiyatli ishga tushdi...")
bot.polling(none_stop=True, interval=0)
