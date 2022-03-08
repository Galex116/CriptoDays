# Импортирование модулей:
import telebot

# Авторизация Telegram:
bot = telebot.TeleBot(token="5251838403:AAFjGaAY9QQ_isXxcOnt9LUa9CtiwxkrbeY")

# Основная часть кода:
@bot.message_handler(commands=['start'])
def welcome(message):

    welcome_keyboard = telebot.types.ReplyKeyboardMarkup(True)
    welcome_keyboard.row("О нас", "Контакты")
    welcome_keyboard.row("Наши чаты")

    bot.send_message(message.chat.id, "👋 Приветствую вас. Этот бот создан, чтобы помочь вам).\n"
                                      "\n"
                                      "👉 Выберите то,что вы хотите узнать: ", reply_markup=welcome_keyboard)

@bot.message_handler(content_types=['text'])
def send_text(message):

    welcome_keyboard = telebot.types.ReplyKeyboardMarkup(True)
    welcome_keyboard.row("О нас", "Контакты")
    welcome_keyboard.row("Наши чаты")

    if message.text == "О нас":
        bot.send_message(message.chat.id, "Добро пожаловать в CryptoDays.\n "
                                          "⚪️ В сфере криптовалюты мы находимся уже более 2 лет.⚡️\n"
                                          "⚪️ Над нашим проектами работают опытные аналитики,"
                                          "которые делятся своим опытом, аналитикой и помогут вам в развитии грамотности. 🧠\n"
                                 "⚪️ Также у нас есть каналы с мировыми новостями криптоволюты,"
                                 " с нами вы всегда будете в курсе чтобы происходит в мире крипты. 🌐\n"
                                 "⚪️ Имеется канал-чат где люди делятся своими успехами, обсуждают новости.🗞\n"
                                 "⚪️Наши аналитики проводят обзоры рынка, вы сможете найти их в нашем канале.📈\n"
                                 "⚪️Надеюсь вам будет приятно и уютно с нами!☺️", reply_markup=welcome_keyboard)
    elif message.text == "Контакты":
        bot.send_message(message.chat.id, "Наш главный аналитик @van_vano03\n"
                                          "Автор канала @Artem12467", reply_markup=welcome_keyboard)
    elif message.text == "Наши чаты":
        bot.send_message(message.chat.id, "Дружелюбный чат: https://t.me/CryptoDaysChat_22\n"
                                          "Канал с сигналами и аналитикой: https://t.me/CryptoDaysSignals_22\n"
                                          "Канал с полезным материалом: https://t.me/CryptoDaysTraining_22\n"
                                          "Новостной канал: https://t.me/Crypto_Days_22", reply_markup=welcome_keyboard)
     


bot.infinity_polling()
