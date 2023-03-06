import sqlite3 as sq
base = sq.connect("reminder.db")
cur = base.cursor()

def start():
    if base:
        print('БД була підключенна успішно!')
    cur.execute('CREATE TABLE IF NOT EXISTS reminder(id INTEGER KEY AUTO_INCREMENT text TEXT, date DATETIME)')
    base.commit()


async def sqlite_add(state):
    async with state.proxy() as data:
        print(data.values())
        cur.execute('INSERT INTO reminder (text, date) VALUES (?, ?)', tuple(data.values()))
        base.commit()