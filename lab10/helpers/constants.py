import numpy as np

NUM_OF_THREADS = 4
URLS_TO_SCRAPE = ['https://ru.pinterest.com/ideas/living-room/908763436660/',
                  'https://ru.pinterest.com/ideas/dining-room/898729085959/',
                  'https://ru.pinterest.com/ideas/kitchens/946506078559/',

                  'https://ru.pinterest.com/ideas/bedroom/894848527867/',
                  'https://ru.pinterest.com/ideas/bathrooms/910556634715/',
                  'https://ru.pinterest.com/ideas/hanging-plants/902856619311/',

                  'https://ru.pinterest.com/ideas/weddings/903260720461/',
                  'https://ru.pinterest.com/ideas/birthday/928401580057/',
                  'https://ru.pinterest.com/ideas/classroom-posters/926000758433/',

                  'https://ru.pinterest.com/ideas/teaching-tips/897115731766/',
                  'https://ru.pinterest.com/ideas/interactive-whiteboard/934124601190/',
                  'https://ru.pinterest.com/ideas/furniture/936760250909/']
CHUNKS = np.array_split(URLS_TO_SCRAPE, NUM_OF_THREADS)
