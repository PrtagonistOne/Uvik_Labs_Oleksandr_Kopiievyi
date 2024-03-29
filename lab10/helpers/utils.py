import uuid
from functools import wraps
import time
import os

import requests
from bs4 import BeautifulSoup


def time_track_factory(behaviour_name: str):
    def time_track(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            end = time.time()
            final_time = end - start
            print(f'Using {behaviour_name} - {round(final_time, 2)} seconds')

        return wrapper

    return time_track


def get_img_links(links_to_scrape: tuple) -> list:
    total_img_links = []

    for url_to_scrape in links_to_scrape:
        r = requests.get(url_to_scrape, stream=True)
        soup = BeautifulSoup(r.content, features="html.parser")
        category_name = url_to_scrape.split('/')[-3]

        dir_name = os.path.abspath('files/')
        if not os.path.isdir(dir_name):
            os.mkdir(dir_name)
            dir_name = os.path.abspath('files/scraped_images/')
            os.mkdir(dir_name)

        dir_name = os.path.abspath(f'files/scraped_images/{category_name}')
        if not os.path.isdir(dir_name):
            os.mkdir(dir_name)

        image_selectors = soup.select('img')

        total_img_links.extend((image.attrs['src'], dir_name) for image in image_selectors)
    return total_img_links


def parse_images_links(total_img_links: list) -> None:
    for img_link in total_img_links:
        image_link = img_link[0]
        path_to_image = img_link[1]
        res = requests.get(image_link, stream=True)
        with open(os.path.join(path_to_image, f'{uuid.uuid4()}.jpg'), 'wb') as f:
            for block in res.iter_content(1024):
                f.write(block)


def get_and_write_wordlist(file_name: str) -> str:
    with open('Monte_Cristo.txt', 'r') as mc, open('Robinson.txt', 'r') as rc:
        robinson = rc.read()
        monte_cristo = mc.read()

    case_text = robinson + monte_cristo

    raw_text = ''.join(filter(str.isalpha, case_text))

    alph = list(filter(str.isalpha, case_text))  # Вибираємо тільки літери з тексту
    upper_case_perc = round(sum(map(str.isupper, alph)) / len(alph), 2)
    lower_case_perc = round(sum(map(str.islower, alph)) / len(alph), 2)

    dir_name = os.path.abspath('files/')

    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
        dir_name = f'{dir_name}/generated_files'
        os.mkdir(dir_name)
    else:
        dir_name = f'{dir_name}/generated_files'

    with open(f'{dir_name}/{file_name}', 'w') as f:
        f.write(raw_text)
    return f"Amount of uppercase letters {upper_case_perc}, Amount of lowercase letters {lower_case_perc}"
