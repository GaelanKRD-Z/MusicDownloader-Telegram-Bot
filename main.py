from run import Bot
import asyncio
from keep_alive import keep_alive

keep_alive()

async def main():
    await Bot.initialize()
    await Bot.run()

asyncio.run(main())
