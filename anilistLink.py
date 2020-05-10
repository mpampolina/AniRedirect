import requests, json

query = '''
query ($id: Int) { # Define which variables will be used in the query (id)
  Media (id: $id, type: ANIME) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
    id
    title {
      romaji
      english
      native
    }
  }
}
'''

variables = {
    'id': 15125
}

url = 'https://graphql.anilist.co'

def anilistTitle(titleCode):
    variables['id'] = titleCode
    response = requests.post(url, json={'query': query, 'variables': variables})
    anime_dict = json.loads(response.text)  # response object has a .text member variable whose contents are json data
    return anime_dict['data']['Media']['title']['romaji']   # returns title of anime
