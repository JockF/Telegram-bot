import telebot
from telebot import types

token='token'
bot=telebot.TeleBot(token)

# start

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'🗂<b>Привет! Добро пожаловать в @MLTIMET_BOT,</b> {message.from_user.first_name}\n<b>📬 это бот проекта MLTime.</b> \n📎 Все команды -> /help' , parse_mode="HTML")

@bot.message_handler(commands=['help'])
def help_message(message):
    help1 = ("<b>Все команды:</b> \n/start - Включает бота\n/help - Показывает все команды")
    bot.send_message(message.chat.id, help1, parse_mode="HTML")
    bot.send_message()

@bot.message_handler(commands=['buy'])
def buy_message(message):
    buy = ("<b>Как купить проходку?:</b> Мы желаем осуществлять индивидуальный подход к каждому игроку наших серверов.\nВы получите доступ не сразу после доната.\nВ течении 24х часов с момента доната, Вам напишет администратор,\nкоторый предоставит вам ссылку на группу в ВК,\nссылку на специальный канал в дискорде,\nдобавит ваш аккаунт на сервер и предоставит\nостальные данные для входа.\nДля связи с вами в донате укажите ссылку на свой профиль в VK или Дискорд.\nУбедитесь, что у вас открыта личка для связи с вами.\n(Если в течение 24х часов, вы не получили сообщения от\nАдминистрации, однако точно уверены, что ввели данные верно -\nзначит на данный момент присутствуют задержки, которые могут длится от нескольких дней до недели.\nУбедитесь, что все данные введены правильно!\nВ ином случае МЫ НЕ СМОЖЕМ СВЯЗАТЬСЯ С ВАМИ и ваш донат будет утерян.\nДонат с неправильными данными, может,\nи будет рассчитываться только\nкак помощь проекту")
    bot.send_message(message.chat.id, buy, parse_mode="HTML")
    bot.send_message()



# help - Показ всех команд
# start - Запуск бота

bot.infinity_polling()