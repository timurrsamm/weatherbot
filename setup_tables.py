import sqlite3
from import_cities import import_cities
import locale
import sys
import os
from dotenv import load_dotenv

load_dotenv()
sqlite_file = os.getenv('SQLITE_FILE')
print('sqlite file: ', sqlite_file)

def create_users_table(conn):
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, user_chat_id int NOT NULL, city_id varchar(25) NOT NULL, time_zone varchar(10) NOT NULL, bot_message_time varchar(20), user_message_time varchar(20), is_running bool)')
    conn.commit()
    cur.close()

def main_setup():
    conn = sqlite3.connect(sqlite_file)
    if sys.platform == 'win32':
        locale.setlocale(locale.LC_ALL, 'rus_rus')
    else:
        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    import_cities(conn)
    create_users_table(conn)
    conn.close()

