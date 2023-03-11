import os
import telebot
import email
import imaplib
import re

# Логин и пароль от вашей учетной записи Gmail
username = 'filipovpetro60@gmail.com'
password = 'bdsdaovuyyktylmq'

# Критерий, который должны удовлетворять гиперссылки
url_criteria = 'fb.me'

# Подключение к почтовому серверу Gmail
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(username, password)

# Выбор папки "Входящие"
mail.select("inbox")

# Поиск писем в папке "Входящие"
status, data = mail.search(None, "ALL")

# Множина для зберігання унікальних гіперссилок
unique_urls = set()

# Перебор найденных писем
for num in data[0].split():
    # Получение данных о письме
    status, data = mail.fetch(num, "(RFC822)")
    message = email.message_from_bytes(data[0][1])

    # Извлечение гиперссылок из письма
    for part in message.walk():
        if part.get_content_type() == 'text/html':
            # Поиск всех гиперссылок в теле письма
            body = part.get_payload(decode=True).decode('utf-8')
            urls = re.findall(r'(https?://\S+)', body)
            # Перебор всех гиперссылок и проверка на соответствие критерию
            for url in urls:
                if url_criteria in url:
                    unique_urls.add(url)

# Виведення унікальних гіперссилок
for url in unique_urls:
    print(url.strip('"'))

# Закрытие соединения с сервером
mail.close()
mail.logout()

with open('unique_urls.txt', 'w') as filee:
    for url in unique_urls:
        filee.write(url.strip('"') + '\n')

BOT_TOKEN = os.environ.get('6220300106:AAHq2J1dNZ0NqX_-MuKA1gEmVGHVBOBplI8')

BOT_TOKEN = "6220300106:AAHq2J1dNZ0NqX_-MuKA1gEmVGHVBOBplI8"
bot = telebot.TeleBot(BOT_TOKEN)
bot_chatID = -1001944684649
filename = "unique_urls.txt"

bot.message_handler(commands=['sendfile'])
def send_file(message):
    filee = open('/unique_urls.txt', 'rb')
    bot.send_document(bot_chatID, filee)

bot.polling()