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



params= "?expansion=SIR&format=TradDraft&user_group="

base_url = "https://www.17lands.com/card_ratings/data"

sets = ['MOM', 'SIR', '23ONE', 'ONE', '23BRO', 'BRO', '23DMU', 'DMU', 'HBG', '22SNC', 'SNC', 'NEO', 'DBL', 'VOW', 'RAVM', 'MID', 'AFR', 'STX', 'CORE', 'KHM', 'KLR', 'ZNR', 'AKR', 'M21', 'IKO', 'THB', 'ELD', 'M20', 'WAR', 'M19', 'DOM', 'XLN', 'RIX', 'GRN', 'RNA']
sets_no_alch = ['SIR', 'ONE', 'BRO', 'DMU', 'HBG', 'SNC', 'NEO', 'DBL', 'VOW', 'RAVM', 'MID', 'AFR', 'STX', 'CORE', 'KHM', 'KLR', 'ZNR', 'AKR', 'M21', 'IKO', 'THB', 'ELD', 'M20', 'WAR', 'M19', 'DOM', 'XLN', 'RIX', 'GRN', 'RNA']

formats =  ["PremierDraft"]

df = pd.DataFrame()

for set in sets:
    for format in formats:
        print(f"{set=} {format=}")
        url = f"https://www.17lands.com/card_ratings/data?expansion={set}&format={format}&start_date=2015-11-11&end_date=2023-04-20"
        resp = req.get(url)
        time.sleep(20)
        print(resp.status_code)
        try:
            data = resp.json()
        except:
            print(resp.headers)
            print(resp.content)

        if data != []:
            temp_df = pd.DataFrame(data)
            temp_df["scryfall_id"] = temp_df["url"].apply(lambda x: x.split("/")[-1].split(".")[0])
            temp_df["drat_format"] = format 
            temp_df["set"] = set
            if len(df.index) == 0:
                df = temp_df
            else:
                df = pd.concat([df, temp_df])

df.to_csv("draft_data.csv")

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db}?charset=utf8mb4")

df.to_sql("draft_data_all", engine, if_exists="replace", index=False)


engine.dispose()
