import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import translators as ts
import emojis

token = "1027715467:AAE-Ka8lXT1Zf7JAPu2exqlfi8hN9W48Yc8"
bot = telebot.TeleBot(token)
SERVICE = "google"
LNG = 'english'


# service inline button
def s_markup():
    s_markup = InlineKeyboardMarkup()
    s_markup.row_width = 2
    s_markup.add(InlineKeyboardButton("Google", callback_data="google"),
                 InlineKeyboardButton("Deepl", callback_data="deepl"))
    return s_markup


# language inline button with emojis
def l_markup():
    l_markup = InlineKeyboardMarkup()
    l_markup.row_width = 3
    l_markup.add(InlineKeyboardButton("\U0001f1fa\U0001f1f8/\U0001f1ec\U0001f1e7", callback_data="english"),
                 InlineKeyboardButton("\U0001f1eb\U0001f1f7", callback_data="french"),
                 InlineKeyboardButton("\U0001f1e9\U0001f1ea", callback_data="german"),
                 InlineKeyboardButton("\U0001f1ef\U0001f1f5", callback_data="japanese"),
                 InlineKeyboardButton("\U0001f1f5\U0001f1f1", callback_data="polish"),
                 InlineKeyboardButton("\U0001f1fa\U0001f1e6", callback_data="ukrainian"))
    return l_markup


# service select
@bot.callback_query_handler(func=lambda call: True)
def s_callback_query(call):
    global SERVICE
    global LNG
    if call.data == "google":
        bot.answer_callback_query(call.id, "Google Translate selected")
        SERVICE = str(call.data)
    elif call.data == "deepl":
        bot.answer_callback_query(call.id, "Deepl selected")
        SERVICE = str(call.data)
    elif call.data == "english":
        bot.answer_callback_query(call.id, "\U0001f1fa\U0001f1f8/\U0001f1ec\U0001f1e7 selected")
        LNG = str(call.data)
    elif call.data == "french":
        bot.answer_callback_query(call.id, "\U0001f1eb\U0001f1f7 selected")
        LNG = str(call.data)
    elif call.data == "german":
        bot.answer_callback_query(call.id, "\U0001f1e9\U0001f1ea selected")
        LNG = str(call.data)
    elif call.data == "japanese":
        bot.answer_callback_query(call.id, "\U0001f1ef\U0001f1f5 selected")
        LNG = str(call.data)
    elif call.data == "polish":
        bot.answer_callback_query(call.id, "\U0001f1f5\U0001f1f1 selected")
        LNG = str(call.data)
    elif call.data == "ukrainian":
        bot.answer_callback_query(call.id, "\U0001f1fa\U0001f1e6 selected")
        LNG = str(call.data)


# start command
@bot.message_handler(commands=['start'])
def translate(message):
    user_name = message.from_user.first_name
    chat_id = message.chat.id
    bot.reply_to(message, f"\U0001f44b {user_name}!\nThis bot can translate your messages!")
    bot.send_message(chat_id, "Type /service to chose translation service! Default is Google!")
    bot.send_message(chat_id, "Type /lan select your translation language! Default is English.")
    bot.send_message(chat_id, "Type /info to see all supported languages!")


# service command
@bot.message_handler(commands=['service'])
def select(message):
    bot.send_message(message.chat.id, "Select your translation service: ", reply_markup=s_markup())


# service command
@bot.message_handler(commands=['lan'])
def select(message):
    bot.send_message(message.chat.id, "Select your language: ", reply_markup=l_markup())


# info command
@bot.message_handler(commands=['info'])
def translate(message):
    bot.reply_to(message, "\U0001f916This bot autodetects the given language!\nCurrently, we support these "
                          "languages: \U0001f1fa\U0001f1f8/\U0001f1ec\U0001f1e7, "
                          "\U0001f1eb\U0001f1f7, \U0001f1ef\U0001f1f5, "
                          "\U0001f1f5\U0001f1f1, \U0001f1fa\U0001f1e6")


# translate
@bot.message_handler()
def translate(message):
    message_text = message.text
    translation = ""
    if SERVICE == 'google':
        if LNG == 'english':
            translation = ts.google(message_text, from_language='auto', to_language='en')
        elif LNG == 'french':
            translation = ts.google(message_text, from_language='auto', to_language='fr')
        elif LNG == 'german':
            translation = ts.google(message_text, from_language='auto', to_language='de')
        elif LNG == 'japanese':
            translation = ts.google(message_text, from_language='auto', to_language='ja')
        elif LNG == 'polish':
            translation = ts.google(message_text, from_language='auto', to_language='pl')
        elif LNG == 's_korean':
            translation = ts.google(message_text, from_language='auto', to_language='ko')
        elif LNG == 'turish':
            translation = ts.google(message_text, from_language='auto', to_language='tr')
        elif LNG == 'ukrainian':
            translation = ts.google(message_text, from_language='auto', to_language='uk')
    elif SERVICE == 'deepl':
        if LNG == 'english':
            translation = ts.deepl(message_text, from_language='auto', to_language='en')
        elif LNG == 'french':
            translation = ts.deepl(message_text, from_language='auto', to_language='fr')
        elif LNG == 'german':
            translation = ts.deepl(message_text, from_language='auto', to_language='de')
        elif LNG == 'japanese':
            translation = ts.deepl(message_text, from_language='auto', to_language='ja')
        elif LNG == 'polish':
            translation = ts.deepl(message_text, from_language='auto', to_language='pl')
        elif LNG == 's_korean':
            translation = ts.deepl(message_text, from_language='auto', to_language='ko')
        elif LNG == 'turish':
            translation = ts.deepl(message_text, from_language='auto', to_language='tr')
        elif LNG == 'ukrainian':
            bot.reply_to(message, "\U0001f613Apologies, Deepl.com have support \U0001f1fa\U0001f1e6 language")
    bot.reply_to(message, translation)


bot.infinity_polling()
