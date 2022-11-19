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


def get_and_write_wordlist(file_name: str) -> None:
    words = ''.join(str(uuid.uuid4()) + '\n' for _ in range(1_000_000))

    dir_name = os.path.abspath('files/generated_files')
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)

    with open(f'{dir_name}/{file_name}', 'w') as f:
        f.write(words)  # len = 37_000_000
