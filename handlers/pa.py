from aiogram import types
from dispatcher import dp


# # start
# @dp.message_handler(commands=('start'))
# async def start(message: types.Message):
    # await message.answer("Хай! Мене звуть Ромбі! Для отримання списку команд введи - /help. В мені з'явилося невеличке оновлення! Якщо хочеш подивитися що змінилося напиши - /renewal")


# # help
# @dp.message_handler(commands=('help'))
# async def help(message: types.Message):
    # await message.answer("<b>Меню допомоги:</b>\n\n<b>Команди які я вмію виконувати:</b>\n<code>/start</code> - запуск/перезапуск бота\n<code>/help</code> - меню допомоги\n<code>/info</code> - інформація\n<code>/password</code> - генерує випадковий пароль, довжина максимум 10 символів\n")


# # info
# @dp.message_handler(commands=('info'))
# async def info(message: types.Message):
    # await message.answer("<b>Інформація:</b> Це бот Ромбі, створенний однією українською людиною, яка до речі проти росії і мені стало скучно... Ну і я вирішив зробити свого Telegram бота і мені стало весело)). Також я надіюся що бот буде оновлюватися і далі, тому чекайте версії 3.01. А я піду поїм вареників і буду думати як можна вдосконалити бота😉\n\n<b>Технічна інформація:</b>\nТех. підтримка: soon\nМови програмування: Python, Aiogram 2\nВерсія боту: 2.103\n\n<b>Комадна розробки:</b>\nГоловний розробник: @Videodimaa\nДизайнер аватару: @Videodimaa\nДизайнер/обробчик повідомлень: @Videodimaa")
