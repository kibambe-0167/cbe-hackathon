import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from services.constants import _keys_word

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
  
  def cluster_ex(self):
    '''manipuilate data, to generate basic clusters, based on predefined sections.'''
    _result: list = list()
    data = self.load_data()
    
    # 
    for article in data:
        f_key, f_score = "", 0
        for k, cats in _keys_word.items():
            key, score = k, 0
            cats = ' '.join(cats).lower().split(' ')
            score = len(list(set( article['title'].lower().replace('-', ' ').strip().split(' ')).intersection(cats)) )
            
            if 'publication' in article.keys():
                score += len(list(set( article['publication'].lower().replace('-', ' ').strip().split(' ')).intersection(cats)) )
            
            if score > f_score:
                f_key = k
                f_score = score
        
        # 
        _result.append({"title":article['title'], "year":article['year'], 'cited':article['cited_by']['value'], "keyword": f_key, "score": f_score})


    ddd : pd.DataFrame = pd.DataFrame(_result)
    ddd.fillna(0, inplace=True)
    ddd['title'] = ddd['title'].apply( lambda x : x.lower() )
    return ddd
    