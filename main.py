import asyncio

from price import get_usdt_price
from telegram import send_price

from config import UPDATE_INTERVAL


async def main():

    while True:

        try:
            price = await get_usdt_price()

            await send_price(price)

            print(f"Price sent: {price}")

        except Exception as error:
            print(f"Error: {error}")

        await asyncio.sleep(UPDATE_INTERVAL)


if __name__ == "__main__":
    asyncio.run(main())