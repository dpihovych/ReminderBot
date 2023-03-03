from datetime import date, datetime, time
from db import reminderdb
import sqlite3 as sq
year = datetime.now().year
base = sq.connect("reminder.db")
cur = base.cursor()
db_time = cur.execute("SELECT time FROM reminder")
time = cur.fetchone()[0]
db_text = cur.execute("SELECT text FROM reminder")
text = cur.fetchone()[0]
db_date = cur.execute("SELECT date FROM reminder")
date = cur.fetchone()[0]

date_str = date
time_str = time

# Задаємо формат дати та часу
date_format = '%m-%d'
time_format = '%H:%M'

# Перетворюємо рядки у об'єкти datetime
date_obj = datetime.strptime(date_str, date_format).date()
time_obj = datetime.strptime(time_str, time_format).time()
print(type(date_obj), date_obj)
print(type(time_obj), time_obj)

# Об'єднуємо дату та час у новий об'єкт datetime
datetime_obj = datetime.combine(date_obj, time_obj)

# Виводимо результат
print(datetime_obj)