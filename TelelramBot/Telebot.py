import telebot

token = ''
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def handle_text(mes):
    if mes.text.lower() == "привет":
        bot.reply_to(mes, "Здрасте")
    elif mes.text.lower() == "как дела?":
        bot.reply_to(mes, "Прекрасно")
    elif mes.text.lower() == "пока":
        bot.reply_to(mes, "Прощай")
    elif mes.text.lower() == "писатель":
        bot.reply_to(mes, "Хемингуэй\n" + "Гюстав Флобер")
    elif mes.text.lower() == "поэт":
        bot.reply_to(mes, "Шекспир\n" + "Александр Пушкин")
    elif mes.text.lower() == "книга":
        bot.reply_to(mes, "Три товарища\n" + "Капитанская дочка")
    elif mes.text.lower() == "монолог":
        bot.reply_to(mes, "Быть или не быть\n" + "Лицом к лицу лица не увидать")
    else:
        bot.send_message(mes.chat.id, mes.text + ": Простите я вас не понимаю...")


bot.infinity_polling()
