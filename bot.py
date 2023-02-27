from aiogram.dispatcher import FSMContext
import asyncio
from aiogram import executor, Dispatcher
from datetime import date, datetime, time
from dispatcher import dp
from handlers.reminder import scheduler, data_time, year, month, day, hours, minutes
from db import reminderdb
from aiogram.dispatcher.filters.state import State, StatesGroup
import sqlite3 as sq
base = sq.connect("reminder.db")
cur = base.cursor()
seconds = '00'
# year = int(year)
# day = int(day)
# hours = int(hours)
# minutes = int(minutes)
# seconds = int(seconds)
text_msg = 'text'



class FSMRe(StatesGroup):
    qtext = State()
    qdate = State()
    qtime = State()


async def send_message_to_admin(dp: Dispatcher, chat_id:str, text:str):
    # cur.execute("SELECT text FROM reminder LIMIT 1")
    # row = cur.fetchone()
    # reminder_text = row[0]
    # text_msg = 'text'   #cur.execute("SELECT text FROM reminder LIMIT 1")
    message = await dp.bot.send_message(chat_id, text)
    # await message.answer(text) 

# run_scheduler = datetime(year=year, month=month, day=day, hour=hours, minute=minutes, second=seconds)

def schedule_jobs(chat_id, text):
    scheduler.add_job(send_message_to_admin, "date", run_date="{year}-{month}-{day} {hours}:{minutes}:00",
                      timezone='Europe/Kiev', args=(dp, chat_id, text))


async def on_startup(_):
    schedule_jobs('5197139803', text_msg)
    reminderdb.start()
    

if __name__ == "__main__":
    scheduler.start()
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)