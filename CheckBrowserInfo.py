import requests
from bs4 import BeautifulSoup
import fake_useragent


user = fake_useragent.UserAgent().random

header = {'user-agent': user}

url = "https://browser-info.ru/"
ip_url = "http://icanhazip.com/"

ip_adress = requests.get(ip_url, headers=header).text.strip()
# ip_soup = BeautifulSoup(ip_responce, headers=header).text
ip_result = f'IP: {ip_adress}'



responce = requests.get(url, headers=header).text

soup = BeautifulSoup(responce, "lxml")
block = soup.find('div', id='tool_padding')

# Получение Джаваскрипта.
check_js = block.find('div', id='javascript_check')
status_js = check_js.find_all('span')[1].text
result_js = f'Javascript: {status_js}'


# Получение Флэша
check_flash = block.find('div', id='flash_version')
status_js_flash = check_flash.find_all('span')[1].text
result_flash = f'Flash: {status_js_flash}'


# Получение User-Agent
check_user_agent = block.find('div', id='user_agent').text[:43]


# Вывод всей информации
print(f'{ip_result}\n{result_js}\n{result_flash}\n{check_user_agent}')