import psycopg2
from aiogram import Bot, Dispatcher
from config import *

connection = psycopg2.connect(
    dbname='traf',
    user='traf',
    password='traf',
    host='localhost'
)

bot = Bot(token=token)
dp = Dispatcher(bot)

def query(query,out=True,fetchone=False):
    try:
        with connection.cursor() as cur:
            cur.execute(query)
            if out:
                if fetchone:
                    return cur.fetchone()[0]
                else:
                    return cur.fetchall()
            else:
                connection.commit()
    except Exception as E:
        connection.rollback()
