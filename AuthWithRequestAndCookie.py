import requests
from bs4 import BeautifulSoup
import lxml
import fake_useragent

session = requests.session()

url = 'https://world-forum.ru/index.php?login/login'

user = fake_useragent.UserAgent().random

header = {
    'user-agent': user
}

data = {
    'login': 'BS4PARSER',
    'password': 'BS4PARSER1'
}

response = session.post(url, data=data, headers=header).text

profile_info = "https://world-forum.ru/index.php?members/bs4parser.61/"
profile_response = session.get(profile_info, headers=header).text

cookies_dict = [
    {'domain': key.domain, 'name': key.name, 'path': key.path, 'value': key.value}
    for key in session.cookies
]

session2 = requests.session()
for cookies in cookies_dict:
    session2.cookies.set(**cookies)
resp = session2.get(profile_info, headers=header)
print(resp.text)

# BS4PARSER; BS4PARSER1