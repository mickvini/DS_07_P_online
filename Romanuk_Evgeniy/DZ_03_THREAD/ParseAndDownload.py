import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin


def parse_images(url, img_urls, current_page=1):
    # Отправляем GET-запрос на указанный URL
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Инициализируем BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Находим все теги <img> на странице
        img_tags = soup.find_all('img')

        # Извлекаем src атрибуты из тегов <img>
        for img in img_tags:
            img_url = img.get('src')
            if img_url and not img_url.startswith(('http://', 'https://')):
                img_urls.add(urljoin(url, img_url))

        # Проверяем количество изображений
        if len(img_urls) >= 100:
            return img_urls
        else:
            # Генерируем URL для следующей страницы
            current_page += 1
            next_page_url = f"{url.rstrip('/0123456789')}/{current_page}/"
            print(f"Переходим на следующую страницу: {next_page_url}")
            return parse_images(next_page_url, img_urls, current_page)

    else:        
        print(f"Error {response.status_code}: Failed to fetch page {url}")
        return None


def download_image(url, save_folder):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            img_data = response.content
            img_filename = os.path.join(save_folder, os.path.basename(url))
            with open(img_filename, 'wb') as img_file:
                img_file.write(img_data)
                #print(f"Сохранено изображение: {img_filename}")
        else:
            print(f"Не удалось скачать изображение по URL: {url}")
    except Exception as e:
        print(f"Ошибка при скачивании изображения по URL: {url}")
        print(e)

