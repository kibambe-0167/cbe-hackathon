from serpapi import GoogleSearch

class Authors(object):
  def __init__(self) -> None:
    '''constructor for the class.'''
    
  def search_scholar(self, ):
    '''search author from google scholar...'''
    search = GoogleSearch({
        "engine": "google_scholar",
        "q": "nlp",
        "author": "Mercy Mpinganjira",
        "location": "south africa",
        "api_key": "623e7e74cde13a07079ea444adbbb7b0fd7070796b34b061e21fc1be638c7c9b"
      })
    result = search.get_dict()
    return result['organic_results']

  def search_author(self, author_id: str ):
    '''search result by author'''
    search = GoogleSearch({
      "engine": "google_scholar_author",
      "author_id": author_id,
      "api_key":"623e7e74cde13a07079ea444adbbb7b0fd7070796b34b061e21fc1be638c7c9b"
    })
    result = search.get_dict()
    return result

  def get_author_profile(self, names: str):
    params = {
      "engine": "google_scholar_profiles",
      "mauthors": names,
      "api_key": "623e7e74cde13a07079ea444adbbb7b0fd7070796b34b061e21fc1be638c7c9b"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    profiles = results["profiles"]
    return profiles