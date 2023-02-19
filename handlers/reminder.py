from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from datetime import date, datetime, time
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dispatcher import dp, bot
from db import reminderdb
from bot import my_function
import asyncio
import config
from aiogram import types, Bot
from aiogram.dispatcher.filters.state import State, StatesGroup

scheduler = AsyncIOScheduler()
now = datetime.now()
data_time = 0
year = now - now
month = now - now
day = now - now
hours = now - now
minutes = now - now
bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
class FSMRe(StatesGroup):
    qtext = State()
    qdate = State()
    qtime = State()


@dp.message_handler(state=None)
async def set_date(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['qtext'] = message.text
    await FSMRe.qtext.set()
    await FSMRe.next()
    await message.answer("Вкажіть дату нагадування")


@dp.message_handler(state=FSMRe.qdate)
async def set_text(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['qdate'] = message.text
    await FSMRe.next()
    await message.reply("Тепер введіть час нагадування")

@dp.message_handler(state=FSMRe.qtime)
async def set_time(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        print(data['qtime'])
        data_time = data['qtime']
        data['qtime'] = message.text
        await message.reply("Ваше нагадування було встановленно успішно!")
    my_function(time=data_time)
    year = now.year
    date_object = datetime.strptime(data['qdate'], '%d.%m')
    datetime_object = datetime.strptime(data['qtime'], '%H:%M')
    date = date_object.strftime("%d%m")
    time = datetime_object.strftime("%H%M")
    day = str(date[:2])
    month = str(date[2:])
    day = int(day)
    month = int(month)

    hours = str(time[:2])
    minutes = str(time[2:])
    hours = int(hours)
    minutes = int(minutes)
    print("hours is ",hours)
    print("minutes is ",minutes) 
    print("day is ",day)
    print("month is ",month)
    print("year is ",year)

    await state.finish()
    # await asyncio.sleep(get_time_to_sleep(data['qtime']))
    # await message.answer(data['qtext'])
    # print(data['qtext'])