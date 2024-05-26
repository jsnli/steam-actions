import psycopg
import os
import asyncio
import json
from dotenv import load_dotenv
from req import fetch

if os.path.isfile('./.env'):
    load_dotenv()

user = os.environ['POSTGRES_USER']
host = os.environ['POSTGRES_HOST']
password = os.environ['POSTGRES_PASSWORD']
name = os.environ['POSTGRES_DATABASE']


async def get_app_list(last_appid=0):
    app_list = await fetch(last_appid)
    data = []

    for index, app in enumerate(app_list["apps"]):
        data.append((app["appid"], app["name"], app["last_modified"]))

    post_app_list(data)

    if "have_more_results" in app_list:
        await get_app_list(app_list["last_appid"])


def post_app_list(data):
    conn = psycopg.connect(f"host={host} dbname={name} user={user} password={password}")
    cur = conn.cursor()

    query = """
        INSERT INTO Games (AppID, Name, LastModified) VALUES (%s, %s, %s)
    """

    cur.executemany(query, data)

    conn.commit()
    cur.close()
    conn.close()


async def main():
    await get_app_list()

asyncio.run(main())
