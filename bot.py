from aiogram.dispatcher import FSMContext
import asyncio
import sqlite3
from aiogram import executor, Dispatcher
from datetime import date, datetime, time
from dispatcher import dp
from handlers.reminder import scheduler, data_time, year, month, day, hours, minutes
from db import reminderdb
from aiogram.dispatcher.filters.state import State, StatesGroup
import sqlite3 as sq

base = sq.connect("reminder.db")
cur = base.cursor()
class FSMRe(StatesGroup):
    qtext = State()
    qdate = State()
    qtime = State()

async def send_message_to_admin(dp: Dispatcher, state: FSMContext):
    # cur.execute("SELECT text FROM reminder LIMIT 1")
    # row = cur.fetchone()
    # reminder_text = row[0]
    await dp.bot.send_message.answer()

def schedule_jobs(state: FSMContext):
    scheduler.add_job(send_message_to_admin, "date", run_date="2023-02-24 21:10:00", timezone='Europe/Kiev', args=(dp,     state     ))

async def on_startup(_):
    schedule_jobs()
    reminderdb.start()
    


if __name__ == "__main__":
    scheduler.start()
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)