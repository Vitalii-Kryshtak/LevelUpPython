from api_pixabay_settings import *
import time
import requests
from threading import Thread as th
from PIL import Image
from io import BytesIO
import os

image_dir = os.path.join(os.getcwd(), IMAGE_PATH)


def preparation_query(query: str) -> str:
    query = query.lower()
    query = query.strip()
    query = '+'.join(query.split())
    return query


def get_request(API_KEY: str, URL: str, query: str, PER_PAGE: int, order='popular') -> dict:
    if PER_PAGE > 200:
        PER_PAGE = 200
    request = f"{URL}{API_KEY}&q={query}&order={order}&per_page={PER_PAGE}"
    response = requests.get(request)
    if response:
        result = response.json()
        return result


def download_save_images(img_url: str, idx: str, image_dir: str):
    res = requests.get(img_url)
    img = Image.open(BytesIO(res.content))
    file_format = img_url[(img_url.rindex(".") + 1) : ]
    dir = os.path.join(image_dir, f"id_{idx}.{file_format}")
    img.save(dir)


def download_save_image_threads(result: dict, image_dir: str, X_RATE_LIMIT: int, TIME_SLEEP:int):
    threads = []
    rate_limit = 0
    for set_image in result["hits"]:
        threads.append(th(target=download_save_images, args=(set_image["webformatURL"], set_image["id"], image_dir)))
        rate_limit += 1
        if rate_limit >= X_RATE_LIMIT:
            res = [th.start() for th in threads]
            time.sleep(TIME_SLEEP)
            threads = []
            rate_limit = 0
            continue
    res = [th.start() for th in threads]


if __name__ == "__main__":
    query = "birds"
    query = preparation_query(query)
    result = get_request(API_KEY, URL, query, PER_PAGE)
    download_save_image_threads(result, image_dir, X_RATE_LIMIT, TIME_SLEEP)

