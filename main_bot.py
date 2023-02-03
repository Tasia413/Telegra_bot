

bot = telebot.TeleBot('Токен Бота')
bot.remove_webhook()
googlesheet_id = 'Токен для Эксель'
gc = gspread.service_account(
     filename='C:\\Users\\Настя\\AppData\\Local\\Programs\\Python\\Python310'
              '\\Lib\\site-packages\\gspread\\service_account.json')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,
                 "Привет, я буду записивать номера ваших сделок, "
                 "и отправлять их порядковый номер. Готов принять информацию!).")


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    deal = message.text

    if len(deal) == 6:
        deal = message.text
        if deal.isdigit():

            sh = gc.open_by_key(googlesheet_id)
            worksheet = sh.sheet1

            number = len(worksheet.col_values(2))
            user = message.chat.username
            text_message = f'Ваша сделка - № {deal} занесена в таблицу под номером {number}'
            bot.send_message(message.chat.id, text_message)

            transaction = [number, deal, user]
            worksheet.append_row(transaction)
        else:
            bot.send_message(message.chat.id, 'Вводите числововое значение.')
    else:
        bot.send_message(message.chat.id, 'Повторите попытку ввода (6 символов)!')


if __name__ == '__main__':
    bot.polling(none_stop=True)
