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


df = pd.read_csv("./mtga_app/data/all_data.csv")


def clean_data(df):
    df = df[df["user_group"] == "All Users"]
    df = df[["Name", "Color", "Rarity", "ATA", "GD WR", "extension_name", "format", "user_group"]]  
    df["Color"] = df["Color"].fillna("C")
    df["Color"] = df["Color"].apply(lambda x: x if len(x) == 1 else 'M')
    df = df.dropna()  
    df["GD WR"] = df["GD WR"].apply(lambda x: float(x[:-1]))
    df = df.rename(columns={"Name":"name", 
                       "Color":"color", 
                       "Rarity": "rarity",
                        "ATA": "average_turn_taken", 
                        "GD WR": "win_rate", 
                        "extension_name": "expansion", 
                        "format": "draft_format"})
    
    return df

df = clean_data(df)

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db}?charset=utf8mb4")

df.to_sql("draft_data", engine, if_exists="append", index=False)
