import requests
from bs4 import BeautifulSoup
import json

def crawl_website(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        json_data = json.loads(soup.text)

        with open('./chat/data/data.json', 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)

        return True
    except:
        return False
    
def read_json():
    try:
        with open('./chat/data/data.json') as json_file:
            data = json.load(json_file)
        return data
    except:
        return None