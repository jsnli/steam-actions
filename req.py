import asyncio
import json
import os
import aiohttp
from dotenv import load_dotenv

if os.path.isfile('./.env'):
    load_dotenv()

base = "https://api.steampowered.com/IStoreService/GetAppList/v1/?"
key = os.environ['STEAM_KEY']
url = f"{base}key={key}&include_games=true&max_results=50000"


async def fetch(last_appid=0):
    async with aiohttp.ClientSession() as session:
        async with session.get(url + f"&last_appid={last_appid}") as response:
            result = await response.json()
            return result["response"]