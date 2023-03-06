# from datetime import datetime

# now = datetime.now()  # Поточна дата і час
# formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")  # Форматуємо дату та час


# dt_obj = datetime.strptime(formatted_datetime, "%Y-%m-%d %H:%M:%S")
# timestamp = int(dt_obj.timestamp())

# print(formatted_datetime)
# print(type(formatted_datetime))
# print(timestamp)
# print(type(timestamp))
from datetime import date, datetime, time
from db import reminderdb
import sqlite3 as sq
base = sq.connect("reminder.db")
cur = base.cursor()

cur.execute("SELECT date FROM reminder WHERE id=1")
sqlite_date = cur.fetchone()[0]
send = datetime.strptime(sqlite_date, '%Y-%m-%d %H:%M')

print(send)
print(type(send))
print(send.time())
print(send.date())
print(type(send.time()))
print(type(send.date()))