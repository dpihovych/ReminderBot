from aiogram.dispatcher import FSMContext
from aiogram import executor, Dispatcher
from datetime import date, datetime, time
from dispatcher import dp
import handlers
from handlers import reminder
from handlers.reminder import scheduler, data_time, FSMRe, year, month, day, hours, minutes
from db import reminderdb
from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMRe(StatesGroup):
    qtext = State()
    qdate = State()
    qtime = State()

# async def my_function(time1):
#     text = time

async def send_message_to_admin(dp: Dispatcher, state: FSMContext):
    await dp.bot.send_message.answer(text)
    await reminderdb.sqlite_add(state)

def schedule_jobs():
    scheduler.add_job(send_message_to_admin, "date", run_date=datetime(year, month, day, hours, minutes), timezone='Europe/Kiev', args=(dp,))

async def on_startup(dp):
    schedule_jobs()
    reminderdb.start()
    


if __name__ == "__main__":
    scheduler.start()
    executor.start_polling(dp, skip_updates=True) #, on_startup=on_startup