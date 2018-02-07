import json
import urllib.request

def get_list_of_countries():
    url = 'http://country.io/names.json'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    return data
