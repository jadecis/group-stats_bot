from aiogram.types import Message
from datetime import datetime, timedelta
from loader import dp, db, bot
from config import group_id

@dp.message_handler(commands='mystats')
async def mystats_handler(msg: Message):
    await msg.delete()
    msg_inf= db.get_msg_stats(msg.from_user.id)
    all_invite_inf= db.get_invite_stats(msg.from_user.id)
    td= datetime.now()
    today= datetime.timestamp(datetime(year=td.year, month=td.month, day=td.day, hour=0))
    today_invite_inf= db.get_invite_stats_today(msg.from_user.id, today)
    name= f"@{msg.from_user.username}" if msg.from_user.username else "" 
    message=f"""
{msg.from_user.full_name}
{name}
    
Пригласил за сегодня: {len(today_invite_inf)}
Пригласил всего: {len(all_invite_inf)}

Написал сообщений за сегодня: {msg_inf[3]}
Написал сообщений всего: {msg_inf[2]}"""
    await msg.answer(text=message)
    
@dp.message_handler(commands='stats')
async def stats_handler(msg: Message):
    await msg.delete()
    temp= msg.text.replace("/stats", "").strip()
    try: 
        user_id= int(temp)
    except Exception as ex:
        print(ex)
        user_id=db.get_id_byUsername(username= temp[1:])
    if user_id:
        user_id= user_id[0]    
        print(user_id)
        msg_inf= db.get_msg_stats(user_id)
        all_invite_inf= db.get_invite_stats(user_id)
        td= datetime.now()
        today= datetime.timestamp(datetime(year=td.year, month=td.month, day=td.day, hour=0))
        today_invite_inf= db.get_invite_stats_today(user_id, today)
        today_refs= []
        for log in today_invite_inf:
            if log[2]:
                today_refs.append(f"@{log[2]}") 
            else:
                try:
                    user= await bot.get_chat_member(chat_id=group_id, user_id=log[1])
                    today_refs.append(f"{user.user.full_name}")
                except Exception as ex:
                        print(ex)
        print(user_id)
        try:
            user= await bot.get_chat_member(chat_id=group_id, user_id=user_id)
            full_name= user.user.full_name
            name= f"@{user.user.username}" if user.user.username else "" 
        except Exception as ex:
            print(ex)
            name= ""
            full_name= ""
        message=f"""
{full_name}
{name}

Пригласил за сегодня {len(today_invite_inf)}: {", ".join(today_refs)}
Пригласил всего: {len(all_invite_inf)}

Написал сообщений за сегодня: {msg_inf[2]}
Написал сообщений всего: {msg_inf[3]}"""
        print(123)
        await msg.answer(text=message)    
    
    