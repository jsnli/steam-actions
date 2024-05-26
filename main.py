# import psycopg
import os
from dotenv import load_dotenv
load_dotenv()

user = os.getenv("POSTGRES_USER")

if 'POSTGRES_USER' in os.environ:
    print("User found in environ")
    user = os.environ['POSTGRES_USER']
    print(user)
