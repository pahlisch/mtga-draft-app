import requests as req
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

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

columns_to_format = ["related_uris", "prices", "artist_ids", "finishes", "games", "legalities", "mana_cost", "image_uris", "multiverse_ids"]
df = pd.read_json("mtga_app/data/oracle-cards.json")

df = df.fillna("no_data")

excluded = ["uri", "scryfall_uri", "image_uris"]

col_type_list = ["colors", "color_identity", "keywords"]

columns = ["id", "oracle_id", "arena_id", "name",  "oracle_text", "mana_cost", "cmc", "colors", "color_identity", "keywords", "type_line", "set_id", "set_name", "set_type", "rarity", "power", "toughness", "produced_mana", "loyalty", "life_modifier", "hand_modifier", "color_indicator"]
columns = df.columns
df = df[columns]

for col in columns:
    df[col] = df[col].apply(str)


engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db}?charset=utf8mb4")

df.to_sql("scryfall_cards", engine, if_exists="replace", index=False)

engine.dispose()