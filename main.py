# import psycopg
import os
from dotenv import load_dotenv
load_dotenv()


user = os.getenv("POSTGRES_USER")
print(user)
