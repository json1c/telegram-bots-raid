import config
import random
import time

from loguru import logger
from multiprocessing import Process
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


class RaidBot:
    def __init__(self, token):
        self.token = token
        self.bot = Bot(token=self.token)
        self.dp = Dispatcher(self.bot)

    async def on_startup(self, _):
        me = await self.bot.get_me()
        username = me.username
        logger.info(f"@{username} is ready to attack!")

    def start(self):
        @self.dp.message_handler(commands=["raid"])
        async def on_message(message: types.Message):
            if message.from_user.id == config.ADMIN_ID:
                for _ in range(config.COUNT):
                    await message.answer(random.choice(config.MESSAGES))
                    time.sleep(config.DELAY)

        executor.start_polling(self.dp, skip_updates=True, on_startup=self.on_startup)

if __name__ == '__main__':
    if config.ADMIN_ID == 1:
        logger.error("Check config.")
        exit(1)

    for token in config.TOKENS:
        bot = RaidBot(token)
        Process(target=bot.start).start()

