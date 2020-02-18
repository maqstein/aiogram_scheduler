from aiogram import executor
from connections import dp,bot
import asyncio
import schedule
import time 

from config import *
from handler import *

def notice_at_8():
    try:
        users = query("select * from chat_users")

        data = query("select user_id from query where send_time >= NOW() - INTERVAL '17 HOURS'")
        reports = []

        for report in data:
            reports.append(report[0])

        notice = "По состоянию на 8-00 текущего дня отчет не сдали:"
        cool_guys = 0
        for user,username in users:
            if user not in reports:
                notice += f"@{username},"
                cool_guys+=1

        notice += "\nНапоминаю вам о необходимости предоставления отчета до 10-00 текущего дня!"

        if not cool_guys: 
            notice = "отчет сдали все"

        asyncio.run_coroutine_threadsafe(bot.send_message(chat_id,notice),loop)
    except Exception as E:
        print(E)


def notice_at_10():
    try:
        users = query("select * from chat_users")

        data = query("select user_id from query where send_time >= NOW() - INTERVAL '19 HOURS'")
        reports = []

        for report in data:
            reports.append(report[0])

        notice = "Отчет не сдали:"

        cool_guys = 0
        for user,username in users:
            if user not in reports:
                notice += f"@{username},"
                cool_guys+=1


        notice += "\nПереведите штраф 1000 рублей Игорю по мобильному до конца дня и пришлите скриншот"
        if not cool_guys: 
            notice = "отчет сдали все"

        asyncio.run_coroutine_threadsafe(bot.send_message(chat_id,notice),loop)
    except Exception as E:
        print(E)


schedule.every().day.at("05:00").do(notice_at_8)

schedule.every().day.at("07:00").do(notice_at_10)

async def pedant():
    schedule.run_pending()


def repeat(coro, loop):
    asyncio.ensure_future(coro(), loop=loop)
    loop.call_later(1, repeat, coro, loop)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.call_later(1,repeat,pedant,loop)
    executor.start_polling(dp, skip_updates=True,loop=loop)