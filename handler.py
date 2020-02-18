from connections import dp,bot,query
from aiogram import types
from config import *

@dp.message_handler(lambda message : message.chat.id == chat_id,commands=['reg'])
async def send_welcome(m: types.Message):
    try:
        query(f"INSERT INTO chat_users VALUES({m.from_user.id},'{m.from_user.username}') ON CONFLICT DO NOTHING",out=False)
        await m.answer("Вы зарегестрированы!")
    except Exception as E:
        print(E)



@dp.message_handler(lambda message : message.chat.id == chat_id)
async def not_a_test(m: types.Message):
    print("h")
    username = query(f"SELECT username from chat_users where user_id = {m.from_user.id}",fetchone=True)
    if username != m.from_user.username:
        query(f"UPDATE chat_users SET username = {m.from_user.username} WHERE user_id = {m.from_user.id}",out=False)

    if "#отчет" in m.text:
        query(f"insert into query(user_id) values({m.from_user.id})",out=False)

