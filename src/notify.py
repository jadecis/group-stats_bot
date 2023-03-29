from loader import db
import asyncio
import aioschedule


async def every_day():
    db.reset_msg()


async def scheduler():
    aioschedule.every().day.at('00:01').do(every_day)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)