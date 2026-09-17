import aiohttp
import requests

url = "https://api.bitpin.org/api/v1/mkt/tickers/"

response = requests.get(url)




async def get_usdt_price():
    async with aiohttp.ClientSession(url) as session:

        async with session.get(url) as response:

            data = await response.json()

            price = (data[2]["price"])

            return float(price)