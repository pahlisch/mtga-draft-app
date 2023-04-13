import requests as req
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import json


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



params= "?expansion=SIR&format=TradDraft&user_group="

base_url = "https://www.17lands.com/card_ratings/data"

sets = ["BRO", "NEO", "ONE"]
formats =  ["QuickDraft", "PremierDraft"]

df = pd.DataFrame()

for set in sets:
    for format in formats:
        url = f"https://www.17lands.com/card_ratings/data?expansion={set}&format={format}"
        resp = req.get(url)
        data = resp.json()
        temp_df = pd.DataFrame(data)
        temp_df["scryfall_id"] = temp_df["url"].apply(lambda x: x.split("/")[-1].split(".")[0])
        temp_df["drat_format"] = format 
        temp_df["set"] = set
        if len(df.index) == 0:
            df = temp_df
        else:
            df = pd.concat([df, temp_df])

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db}?charset=utf8mb4")

df.to_sql("draft_data", engine, if_exists="replace", index=False)

engine.dispose()
