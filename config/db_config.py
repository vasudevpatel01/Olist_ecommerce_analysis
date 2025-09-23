from dotenv import load_dotenv
import os

load_dotenv()

DB_Config = {
    'user' : 'root',
    'password' : os.getenv('DB_PASSWORD'),
    'host' : 'localhost',
    'DB' : 'Olist'
}