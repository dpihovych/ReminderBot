from aiogram.dispatcher import FSMContext
import asyncio
import functools
from aiogram import executor, Dispatcher
from datetime import date, datetime, time
from dispatcher import dp
from handlers.reminder import scheduler, data_time, year, month, day, hours, minutes
from db import reminderdb
from aiogram.dispatcher.filters.state import State, StatesGroup
import sqlite3 as sq
global send, text
year = datetime.now().year

now = datetime.now()
nows = now.strftime("%Y-%m-%d %H:%M")
print(nows)
base = sq.connect("reminder.db")
cur = base.cursor()
text = "" 
send = nows
send = now.strftime("%Y-%m-%d %H:%M")
date_format = "%Y-%m-%d %H:%M"

date_time_obj = datetime.strptime(send, date_format)
print("Об'єкт datetime:", date_time_obj)
print("Тип об'єкту datetime:", type(date_time_obj))
print("first send type", type(send))
send_date = f"{now}"

# 
# cur.execute("SELECT date FROM reminder WHERE id=1")
# send_date = cur.fetchone()[0]
# send = datetime.strptime(send_date, '%Y-%m-%d %H:%M')
#   
# db_text = cur.execute("SELECT text FROM reminder WHERE id=1")
# text = cur.fetchone()[0]
# 


class FSMRe(StatesGroup):
    qtext = State()
    qdate = State()
    qtime = State()


async def send_message_to_admin(dp: Dispatcher, chat_id:str, text:str):
    cur.execute("SELECT date FROM reminder WHERE id=1")
    send_date = cur.fetchone()[0]
    cur.execute("SELECT text FROM reminder WHERE id=1")
    text = cur.fetchone()[0] 
    await dp.bot.send_message(chat_id, text)
    print("Сенд в функції",send)
    print("Тип сенда в функції",type(send))
    

def schedule_jobs(chat_id, text):
    send = datetime.strptime(send_date, '%Y-%m-%d %H:%M') 
    print("Сенд в функції джобс",send)
    print("Тип сенда в функції джобс",type(send))
    scheduler.add_job(send_message_to_admin, "date", run_date=f"{send}",
                      timezone='Europe/Kiev', args=(dp, chat_id, text, send))

async def on_startup(_, text):
    # print("time_obj", time_obj)
    # print("text", text)
    # print("date_obj", date_obj),
    # print(type(time_obj))
    # print(type(text))я
    # print(type(date_obj))
    # print(type(datetime_obj), datetime_obj)
    # print(type(datetime_upd), datetime_upd)
    # print(type(datetime_int), datetime_int)
    schedule_jobs('5197139803', text)
    reminderdb.start()
    

# if __name__ == "__main__":
#     scheduler.start()
#     executor.start_polling(dp, skip_updates=True, on_startup=on_startup, args=(text,))


if __name__ == "__main__":
    scheduler.start()
    on_startup_with_args = functools.partial(on_startup, text=text)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup_with_args)