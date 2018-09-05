import requests
import sys
import pickle

BASE_URL = "https://api.groupme.com/v3"
GROUPS_URL = "/groups"
ACCESS_TOKEN = ""
GROUPS_PER_PAGE = "&per_page=100"

def get_group_url():
    return BASE_URL + GROUPS_URL + ACCESS_TOKEN + GROUPS_PER_PAGE

def get_group_ids(url):
    response = requests.get(url);
    json_content = response.json()
    return [group['id'] for group in json_content['response']]

def read_content_text(file_name):
    pass

def read_content_image(file_name):
    pass

def post_all_groups(content):
    pass


url = get_group_url();
print(get_group_ids(url))

