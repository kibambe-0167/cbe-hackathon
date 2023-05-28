from serpapi import GoogleSearch
import json

file_path = "./articles.json"
def write_dict_file(data):
  d = load_data_file()
  if d:
    d.extend(data)
    with open(file_path , "w") as file: json.dump(d, file)
    return True
  else: 
    with open(file_path , "w") as file: json.dump(data, file)
    return True

def load_data_file():
  '''load current data and append new data'''
  data = None
  with open(file_path) as file:
      data = json.load(file)
  return data

class Authors(object):
  def __init__(self) -> None:
    '''constructor for the class.'''
    
  def search_scholar(self, query: str ):
    '''search author from google scholar...'''
    search = GoogleSearch({
        "engine": "google_scholar",
        "q": query,
        "author": "Mercy Mpinganjira",
        "location": "south africa",
        "api_key": "623e7e74cde13a07079ea444adbbb7b0fd7070796b34b061e21fc1be638c7c9b"
      })
    result = search.get_dict()
    if 'organic_results' in result.keys and result['organic_results']:
      return result['organic_results']
    else: return None

  def search_author(self, author_id: str ):
    '''search result by author'''
    search = GoogleSearch({
      "engine": "google_scholar_author",
      "author_id": author_id,
      "api_key":"623e7e74cde13a07079ea444adbbb7b0fd7070796b34b061e21fc1be638c7c9b"
    })
    result = search.get_dict()
    
    if 'articles' in result.keys():
      write_dict_file(result['articles'])
    return result

  def get_author_profile(self, names: str):
    params = {
      "engine": "google_scholar_profiles",
      "mauthors": names,
      "api_key": "623e7e74cde13a07079ea444adbbb7b0fd7070796b34b061e21fc1be638c7c9b"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    if "profiles" in results.keys():
      profiles = results["profiles"]
      return profiles
    else: 
      return None