from concurrent.futures import ThreadPoolExecutor

from helpers.constants import NUM_OF_THREADS, CHUNKS, URLS_TO_SCRAPE
from helpers.utils import time_track_factory, get_img_links, parse_images_links


@time_track_factory(f'Using Threads({NUM_OF_THREADS})')
def main_concurrent():
    with ThreadPoolExecutor(max_workers=NUM_OF_THREADS) as executor:
        img_links = executor.map(get_img_links, CHUNKS)
        for images in img_links:
            future = executor.submit(parse_images_links, images)
        future.result()


@time_track_factory('Using Neither Concurrent, nor Parallel')
def main():
    img_links = get_img_links(URLS_TO_SCRAPE)
    parse_images_links(img_links)


if __name__ == "__main__":
    main_concurrent()  # 14.0s
    # main()   # 61.76
