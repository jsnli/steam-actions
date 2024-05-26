import psycopg
import os
from dotenv import load_dotenv


if os.path.isfile('./.env'):
    load_dotenv()

user = os.environ['POSTGRES_USER']
host = os.environ['POSTGRES_HOST']
password = os.environ['POSTGRES_PASSWORD']
name = os.environ['POSTGRES_DATABASE']

conn = psycopg.connect(f"host={host} dbname={name} user={user} password={password}")
cur = conn.cursor()
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",
            (200, "two hundred"))
conn.commit()
