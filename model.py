import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return pymysql.connect(
        host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
        user="8LasdzwWekkncUN.root",
        password=os.getenv("TIDB_PASSWORD"),
        database="portfolio",
        port=4000,
        ssl={"ssl": {}},
        cursorclass=pymysql.cursors.DictCursor
    )