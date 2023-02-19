import sqlite3 as sq

def start():
    global base
    global cur
    base = sq.connect("reminder.db")
    cur = base.cursor()
    if base:
        print('БД була підключенна успішно!')
    # base.execute('CREATE TABLE re(text TEXT, date TEXT , time TEXT)')
    # base.commit()

async def sqlite_add(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO re VALUES (?, ?, ?)', tuple(data.values()))
        base.commit()