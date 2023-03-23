import pandas as pd

def get_matches_data():
  return pd.read_csv("static/datasets/matches.csv")
  
def get_deliveries_data():
  return pd.read_csv("static/datasets/deliveries.csv")