import telebot
from translate import translator
API_KEY = "2003887536:AAF-ZXAg_LgbbAKSMLQIEAVthTjk_ddvGyg"

bot = telebot.TeleBot(API_KEY,parse_mode="HTML")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Welcome to my TranslaThor bot, ask me japanese and i will give the pronunciation for you")

@bot.message_handler(content_types=['text'])
def translate(message):
    link = f"https://translate.google.com/?sl=ja&tl=ja&text={message.text}&op=translate"
    reply = f"\"{translator(message.text)}\""
    bot.send_message(message.chat.id, reply,disable_web_page_preview=True)

print("starting bot.")
bot.infinity_polling()