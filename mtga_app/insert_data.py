import requests as req
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import time


load_dotenv()
user = os.getenv('DB_USERNAME')
db = os.getenv('DB')
host = os.getenv('DB_HOST')
password = os.getenv('DB_PASSWORD')

config = {
  'user': user,
  'password': password,
  'host': host,
  'database': db,
  'raise_on_warnings': True
}



df = pd.read_csv("./mtga_app/data/draft_data.csv")

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db}?charset=utf8mb4")

df.to_sql("draft_data_all2", engine, if_exists="replace", index=False)


engine.dispose()
