from aiogram.dispatcher import FSMContext
import asyncio
from aiogram import executor, Dispatcher
from datetime import date, datetime, time
from dispatcher import dp
from handlers.reminder import scheduler, data_time, year, month, day, hours, minutes
from db import reminderdb
from aiogram.dispatcher.filters.state import State, StatesGroup
import sqlite3 as sq
year = datetime.now().year
base = sq.connect("reminder.db")
cur = base.cursor()
# db_text = cur.execute("SELECT text FROM reminder WHERE id=1")
# text = cur.fetchone()[0]

# current_year = datetime.now().year
# date_str = date
# time_str = time

# Задаємо формат дати та часу
# date_format = '%m-%d'
# time_format = '%H:%M'

# Перетворюємо рядки у об'єкти datetime
# date_obj = datetime.strptime(date_str, date_format).date()
# time_obj = datetime.strptime(time_str, time_format).time()
# datetime_obj = datetime.combine(date_obj, time_obj)
# datetime_obj = datetime_obj.replace(year=current_year)
# datetime_upd = str(datetime_obj)
# # ormatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
# str(datetime_obj)
# int(datetime_obj)
# datetime_upd = int(datetime_upd)
# datetime_int = int(datetime_obj.strftime('%Y-%m-%d %H:%M'))
# 
# cur.execute("SELECT date FROM reminder WHERE id=1")
# send_date = cur.fetchone()[0]
# send = datetime.strptime(send_date, '%Y-%m-%d %H:%M')
# 


class FSMRe(StatesGroup):
    qtext = State()
    qdate = State()
    qtime = State()


async def send_message_to_admin(dp: Dispatcher, chat_id:str, text:str):
    await dp.bot.send_message(chat_id, text)
    db_text = cur.execute("SELECT text FROM reminder WHERE id=1")
    text = cur.fetchone()[0]
    cur.execute("SELECT date FROM reminder WHERE id=1")
    send_date = cur.fetchone()[0]
    send = datetime.strptime(send_date, '%Y-%m-%d %H:%M')
def schedule_jobs(chat_id, text):
    scheduler.add_job(send_message_to_admin, "date", run_date=f"{send}",
                      timezone='Europe/Kiev', args=(dp, chat_id, text))

async def on_startup(_):
    # print("time_obj", time_obj)
    # print("text", text)
    # print("date_obj", date_obj)
    # print(type(time_obj))
    # print(type(text))
    # print(type(date_obj))
    # print(type(datetime_obj), datetime_obj)
    # print(type(datetime_upd), datetime_upd)
    # print(type(datetime_int), datetime_int)
    schedule_jobs('5197139803', text)
    reminderdb.start()
    

if __name__ == "__main__":
    scheduler.start()
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)