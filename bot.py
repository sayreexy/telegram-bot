import telebot
from telebot import types

# ⚠️ ЗАМЕНИ ЭТОТ ТОКЕН НА СВОЙ!
TOKEN = "8418283487:AAFr2sck3qfKgqzCk8CjrdolNNctMeMZqYU"
bot = telebot.TeleBot(TOKEN)

user_languages = {}

@bot.message_handler(commands=['start'])
def start(message):
    # Попробуй отправить фото (положи файл photo.jpg в ту же папку)
    try:
        with open('photo.jpg', 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption="👋 Welcome!")
    except:
        pass
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn_lt = types.KeyboardButton("🇱🇹 LT")
    btn_ru = types.KeyboardButton("🇷🇺 RU") 
    btn_eng = types.KeyboardButton("🇺🇸 ENG")
    markup.add(btn_lt, btn_ru, btn_eng)
    
    welcome_text = """
Привет! 👋 
Выберите язык / Pasirinkite kalbą / Choose language:

🇱🇹 LT - Lietuvių kalba
🇷🇺 RU - Русский язык  
🇺🇸 ENG - English
    """
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["🇱🇹 LT", "🇷🇺 RU", "🇺🇸 ENG"])
def handle_language_selection(message):
    chat_id = message.chat.id
    language = message.text
    
    if language == "🇱🇹 LT":
        user_languages[chat_id] = 'LT'
        response = "Sveiki! Pasirinkote lietuvių kalbą. 😊"
    elif language == "🇷🇺 RU":
        user_languages[chat_id] = 'RU' 
        response = "Привет! Вы выбрали русский язык. 😊"
    else:  # ENG
        user_languages[chat_id] = 'ENG'
        response = "Hello! You selected English. 😊"
    
    remove_markup = types.ReplyKeyboardRemove()
    bot.send_message(chat_id, response, reply_markup=remove_markup)
    show_main_menu(chat_id)

def show_main_menu(chat_id):
    language = user_languages.get(chat_id, 'RU')
    
    if language == 'LT':
        text = "Pagrindinis meniu!"
        btn1 = "⚙️ Nustatymai"
        btn2 = "ℹ️ Informacija"
    elif language == 'ENG':
        text = "Main menu!"
        btn1 = "⚙️ Settings" 
        btn2 = "ℹ️ Information"
    else:  # RU
        text = "Главное меню!"
        btn1 = "⚙️ Настройки"
        btn2 = "ℹ️ Информация"
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton(btn1), types.KeyboardButton(btn2))
    
    bot.send_message(chat_id, text, reply_markup=markup)

if __name__ == "__main__":
    print("Бот запущен! 🚀")
    bot.polling(none_stop=True)