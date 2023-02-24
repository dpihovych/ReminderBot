# import sqlite3 as sq


# def start():
#     global base, cur
#     base, cur
#     base = sq.connect("reminder.db")
#     cur = base.cursor()
#     if base:
#         print('БД була підключенна успішно!')
#     base.execute('CREATE TABLE IF NOT EXISTS re(text TEXT, date TEXT , time TEXT)')
#     base.commit()


# async def sqlite_add(state):
#     async with state.proxy() as data:
#         cur.execute('INSERT INTO re VALUES (?, ?, ?)', tuple(data.values()))
#         base.commit()
import sqlite3 as sq
base = sq.connect("reminder.db")
cur = base.cursor()

def start():
    if base:
        print('БД була підключенна успішно!')
    cur.execute('CREATE TABLE IF NOT EXISTS reminder(text TEXT, date TEXT , time TEXT)')
    base.commit()


async def sqlite_add(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO reminder VALUES (?, ?, ?)', tuple(data.values()))
        base.commit()