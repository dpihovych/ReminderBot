from aiogram.dispatcher import FSMContext
import asyncio
import functools
from aiogram import executor, Dispatcher
from datetime import date, datetime, time
from dispatcher import dp
from handlers.reminder import scheduler
from db import reminderdb
from aiogram.dispatcher.filters.state import State, StatesGroup
import sqlite3 as sq
base = sq.connect("reminder.db")
cur = base.cursor()
text = "" 

async def send_message_to_admin(dp: Dispatcher, chat_id:str, text:str, send:datetime):
    # global sendfunc
    # global send 
    # send = None
    cur.execute("SELECT date FROM reminder WHERE id=1")
    send_date = cur.fetchone()[0]
    send = datetime.strptime(send_date, '%Y-%m-%d %H:%M') # перевожу в дейттайм
    cur.execute("SELECT text FROM reminder WHERE id=1")
    text = cur.fetchone()[0]
    await dp.bot.send_message(chat_id, text)
    print("Сенд в функції",send)
    print("Тип сенда в функції",type(send))
    

def schedule_jobs(chat_id, text):
    global send 
    send = None
    print("Сенд в функції джобс",send)
    print("Тип сенда в функції джобс",type(send))
    # send = sendfunc
    scheduler.add_job(send_message_to_admin, "date", run_date=send, args=(dp, chat_id, text, send))

async def on_startup(_, text):
    schedule_jobs('5197139803', text)
    reminderdb.start()
    
if __name__ == "__main__":
    scheduler.start()
    on_startup_with_args = functools.partial(on_startup, text=text)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup_with_args)