from flask import (
    Blueprint, render_template, request, redirect, url_for, jsonify
)
import pandas as pd
import plotly.express as px
import os
import json
import plotly

bp = Blueprint('index', __name__)

def clean_data(df):
    df = df[df["user_group"] == "All Users"]
    df = df[["Name", "Color", "Rarity", "ATA", "GD WR", "IWD", "extension_name", "format"]]  
    df["Color"] = df["Color"].fillna("C")
    df["Color"] = df["Color"].apply(lambda x: x if len(x) == 1 else 'M')
    
    df = df.dropna()  
    df["GD WR"] = df["GD WR"].apply(lambda x: float(x[:-1]))
    df["IWD"] = df["IWD"].apply(lambda x: float(x[:-2]))

    df["rounded_pick_order"] = df["ATA"].apply(lambda x: round(x, 0))
    



    return df

def plot_win_rate_over_ata(df):

    fig = px.scatter(df, 
                     y="GD WR", 
                     x="ATA", 
                     title="Win rate when in hand or drawn by average turn picked",
                     labels={
                        "GD WR":"Average win rate when in hand or drawn",
                        "ATA":"Average turn picked",
                        "Color":"Card Color"
                     },
                     hover_name="Name", 
                     hover_data=[ 
                            "ATA"
                            ],
                    template="plotly_dark"
                            )
    
    fig.update_traces(marker_size=7)
    fig.update_layout(autosize=True, 
                      height=700, 
                      width=1200,
                      xaxis=dict(dtick=1))


    return fig

def get_df():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_filename = "data/all_data.csv"

    data_filepath = os.path.join(script_dir, data_filename)

    df = pd.read_csv(data_filepath)

    df = clean_data(df)

    return df

@bp.route('/', methods=["POST", "GET"])
def index():

    df = get_df()

    if request.form.to_dict() == {}:
        extension = df["extension_name"].iloc[0]
        format = df["format"].iloc[0]
    else:
        extension = request.form["extension_list"]
        format = request.form["format_list"]


    extension_list = list(df["extension_name"].unique())

    format_list = list(df["format"].unique())

    if extension != None:
        df = df[df["extension_name"] == extension]
    if format != None:
        df = df[df["format"] == format]

    if len(df.index) > 0:
        fig = plot_win_rate_over_ata(df)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    else:
        graphJSON = None



    return render_template("index.html", 
                           graphJSON=graphJSON, 
                           extension_list=extension_list, 
                           selected_value=extension, 
                           format_list = format_list, 
                           selected_format=format
                           )

@bp.route('/update_graph', methods=['POST'])
def update_graph():

    format = request.form['format']
    extension = request.form['extension']

    df = get_df()

    if extension != None:
        df = df[df["extension_name"] == extension]
    if format != None:
        df = df[df["format"] == format]

    if len(df.index) > 0:
        fig = plot_win_rate_over_ata(df)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return graphJSON
    else:
        return "df is empty"

@bp.route('/draft_status', methods=['POST'])
def draft_status():

    return "coucou"