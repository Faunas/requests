import requests
from bs4 import BeautifulSoup
import lxml
import fake_useragent

image_number = 0
storage_number = 1
url = f'https://zastavok.net'


responce = requests.get(f'{url}/{storage_number}').text
soup = BeautifulSoup(responce, 'lxml')

block = soup.find('div', class_='block-photo')
all_image = block.find_all('div', class_='short_full')


for image in all_image:
    image_link = image.find('a').get('href')
    download_storage = requests.get(f'{url}{image_link}').text
    download_soup = BeautifulSoup(download_storage, 'lxml')
    download_block = download_soup.find('div', class_='image_data').find('div', class_='block_down')
    result_link = download_block.find('a').get('href')
    image_bytes = requests.get(f'{url}{result_link}').content
    print(result_link)

    with open(f"image/{image_number}.jpg", "wb") as file:
        file.write(image_bytes)

    image_number += 1
    print(f'Изображение {image_number}.jpg успешно скачано')

