import telebot
from telebot import types
# Создаем бота
bot = telebot.TeleBot('5284799411:AAFByfrB8QBcGqESGKOJ-bW5GXfDli__Xjc')
# Команда start
@bot.message_handler(commands=["start"])
def start(m, res = False):
    
        # Добавляем две кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)

        item1=types.KeyboardButton("Я стала жертвой сексуального насилия")
        item2=types.KeyboardButton("Я стала жертвой физического насилия")
        item3=types.KeyboardButton("Я стала жертвой психологического насилия")
        item4=types.KeyboardButton("Связаться с нами")
        item5=types.KeyboardButton("Получить реквизиты для помощи пострадавшим")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        bot.send_message(m.chat.id, 'Привет, меня зовут Алия😊! Я бот фонда \n"Луч защиты"❤️‍🔥 и могу ответить на \nсамые популярные вопросы, которые\n задают пострадавшие и свидетели насилия.🔆 \n \nКакая ситуация характеризует ваше положение?',  reply_markup=markup)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Я стала жертвой сексуального насилия':
            mess = f'Обратитесь как можно скорее в течение 7 дней в один из центров помощи жертвам сексуального насилия, которые круглосуточно работают в Бишкеке, Канте и Токмаке. Помощь бесплатная. Не мойся, ничего не ешь и не пей. Ту одежду, которая была на тебе в момент случившегося, положи в бумажный пакет и принеси с собой. Если с момента совершения сексуального преступления прошло более 7 дней, нужно обратиться в полицию. Если состояние твоего здоровья плохое или ухудшается, нужно обратиться к семейному врачу или в отделение Экстренной медицины. Если с момента совершения сексуального преступления прошло более 7 дней, то взять медицинский материал для доказательств уже невозможно, но, возможно, тебе будет нужна психологическая помощь или помощь врача (гинеколога, дерматовенеролога) для проведения анализов на инфекции, передающиеся половым путем. Для этого нужно будет обратиться на прием к психологу или соответствующему врачу. \n\n <b>Пострадавший человек никогда не виноват в сексуальном насилии!</b>'
            bot.send_message(message.chat.id, mess, parse_mode='html')
    elif message.text.strip() == 'Связаться с нами':
            mess = f'Если у вас есть вопросы обращайтесь по горячей линии: <b>1234</b> \n Наша почта: \n noviolence@gmail.com'
            bot.send_message(message.chat.id, mess, parse_mode='html')
            
    elif message.text.strip() == 'Я стала жертвой физического насилия':
            mess = f'<a href="https://katsaylidi.ru/article/chto-delat-esli-izbili-cheloveka">Что делать если я подверглась физическому насилию?</a>'
            bot.send_message(message.chat.id, mess, parse_mode='html')
    
    elif message.text.strip() == 'Я стала жертвой психологического насилия':
            mess = f'Обратитесь по горячей линии, 1234 или напишите нам на почту noviolence@gmail.com и присоединятесь в нашему АНОНИМНОМУ форуму где вы сможете поделиться своей историей и получить советы от экспертов.'
            bot.send_message(message.chat.id, mess, parse_mode='html')
    
    elif message.text.strip() == 'Получить реквизиты ддя помощи пострадавшим':
            mess = f'<b>Наши реквезиты: </b> \n Optima bank: 2348 7384 7556, \n Элсом: +996 555 105 353, \n Qiwi: +996 564 239 323, \n Payeer: P1067879164, \n PayPal: 9485 4549 3840' 
            bot.send_message(message.chat.id, mess, parse_mode='html')
    
bot.polling(none_stop=True, interval=0)
