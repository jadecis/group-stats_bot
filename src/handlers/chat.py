from aiogram.types import Message, CallbackQuery, ChatMemberUpdated, ChatType
from aiogram.dispatcher.filters import ChatTypeFilter
from datetime import datetime, timedelta
from loader import dp, db, bot
from config import group_id

@dp.chat_member_handler()
async def some_handler(msg: ChatMemberUpdated):
    if msg.new_chat_member.status == 'member':
        refferer_id= msg["from"].id
        refferer_username= msg["from"].username
        user_id= msg.new_chat_member.user.id
        username= msg.new_chat_member.user.username
        try:
            db.add_user(
                {
                    'user_id' : user_id,
                    'username' : username,
                    'refferer_id' : refferer_id,
                    'refferer_username' : refferer_username,
                    'date' : datetime.timestamp(datetime.now())
                }
            )
        except:
            pass
        
@dp.message_handler(ChatTypeFilter(ChatType.SUPERGROUP))
async def chat_message_handler(msg: Message):
    if msg.chat.id == group_id:
        try:
            db.add_usermsg(msg.from_id, msg.from_user.username)
        except:
            db.set_usermsg(msg.from_id)
            db.reset_username(msg.from_id, msg.from_user.username)

