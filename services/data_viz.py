import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class DataViz(object):
  def __init__(self) -> None:
    ''''''
  
  def load_data(self,):
    ''''''
    with open("./articles.json") as obj:
      data = json.load(obj)
    return data
  
  def cite_year_title(self):
    '''extract citations, year and title of article'''
    data = self.load_data()
    ds = pd.DataFrame( [{"title":d['title'], "year":d['year'], 'cited':d['cited_by']['value']} for d in data] )
    # replace nan with zero.
    ds.fillna(0, inplace=True)
    ds['title'] = ds['title'].apply( lambda x : x.lower() )
    return ds