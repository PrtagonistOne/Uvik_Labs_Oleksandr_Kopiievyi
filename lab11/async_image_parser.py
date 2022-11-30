from helpers.constants import URLS_TO_SCRAPE
from helpers.utils import AsyncImageParser


if __name__ == "__main__":
    # main()   # ~61s, default execution as per lab 10
    AsyncImageParser(urls=URLS_TO_SCRAPE)  # ~6 seconds
