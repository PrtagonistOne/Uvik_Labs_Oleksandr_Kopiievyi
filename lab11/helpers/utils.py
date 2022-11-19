import asyncio
from functools import wraps
import time
import os

import aiofiles
from bs4 import BeautifulSoup
import aiohttp


def time_track_factory(behaviour_name: str):
    def time_track(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            start = time.time()
            await func(*args, **kwargs)
            end = time.time()
            final_time = end - start
            print(f'Using {behaviour_name} - {round(final_time, 2)} seconds')
        return wrapper
    return time_track


class AsyncImageParser:
    def __init__(self, urls):
        self.dir_name = None
        self.urls = urls
        # Global Place To Store The Data:
        self.total_img_links = []
        # Run The Scraper:
        asyncio.run(self.main())

    async def get_img_links(self, session, url_to_scrape) -> None:
        async with session.get(url_to_scrape) as response:
            html = await response.text()

            image_links_per_url = await self.extract_image_links(html=html, url_to_scrape=url_to_scrape)
            await self.get_category_images_links(link_per_url=image_links_per_url,
                                                 dir_name=self.dir_name)

    async def get_category_images_links(self, link_per_url: list, dir_name: str) -> None:
        self.total_img_links.extend((image.attrs['src'], dir_name) for image in link_per_url)

    @staticmethod
    async def check_folder(category_name: str) -> str:
        dir_name = os.path.abspath('files/')
        if not os.path.isdir(dir_name):
            os.mkdir(dir_name)
            dir_name = os.path.abspath('files/scraped_images/')
            os.mkdir(dir_name)

        dir_name = os.path.abspath(f'files/scraped_images/{category_name}')
        if not os.path.isdir(dir_name):
            os.mkdir(dir_name)
        return dir_name

    async def extract_image_links(self, html: str, url_to_scrape: str):
        soup = BeautifulSoup(html, features="html.parser")
        category_name = url_to_scrape.split('/')[-3]

        self.dir_name = await self.check_folder(category_name=category_name)
        return soup.select('img')

    @staticmethod
    async def async_safe_image(img_link: str, session) -> None:
        image_link = img_link[0]
        path_to_image = img_link[1]
        img_name = f"{image_link.split('/')[-1]}"

        async with session.get(image_link) as response:
            if response.status == 200:
                f = await aiofiles.open(os.path.join(path_to_image, img_name), mode='wb')
                await f.write(await response.read())
                await f.close()

    @time_track_factory('Using Async')
    async def main(self):
        total_links_tasks = []
        download_img_tasks = []
        async with aiohttp.ClientSession() as session:
            total_links_tasks.extend(self.get_img_links(session, url) for url in self.urls)
            await asyncio.gather(*total_links_tasks)
            print(f'Total images links - {len(self.total_img_links)}')
            download_img_tasks.extend(self.async_safe_image(img_link=img, session=session) for img in self.total_img_links)
            await asyncio.gather(*download_img_tasks)

