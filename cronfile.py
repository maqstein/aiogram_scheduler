# from connections import query,bot,dp
# from aiogram import executor
# import asyncio

# async def at_8_am():
#     users = query("select * from chat_users")

#     data = query("select user_id from query where send_time >= NOW() - INTERVAL '17 HOURS'")
#     reports = []

#     for report in data:
#         reports.append(report[0])

#     notice = "По состоянию на 8-00 текущего дня отчет не сдали:"
#     print(reports)
#     for user,username in users:
#         if user not in reports:
#             notice += f"@{username},"

#     notice += "\nПереведите штраф 1000 рублей Игорю по мобильному до конца дня и пришлите скриншот"

# executor.start_polling(dp,loop=ioloop)

# ioloop = asyncio.get_event_loop()
# ioloop.run_until_complete(at_8_am)
# ioloop.close()
