import time
import os
import requests
from io import BytesIO
from threading import Thread as th

from PIL import Image

from api_pixabay_settings import (
    API_KEY,
    URL,
    X_RATE_LIMIT,
    TIME_SLEEP,
    PER_PAGE,
    IMAGE_PATH,
)

image_dir = os.path.join(os.getcwd(), IMAGE_PATH)
FILENAME_NEXT_POSITION = 1


def preparation_query(query: str) -> str:
    query = query.lower()
    query = query.strip()
    query = '+'.join(query.split())
    # "Yellow bird" -> "yellow+bird"
    return query


def get_request(
        API_KEY: str,
        URL: str,
        query: str,
        PER_PAGE: int,
        order='popular'
) -> dict:
    if PER_PAGE > 200:
        PER_PAGE = 200
    # request = f"{URL}{API_KEY}&q={query}&order={order}&per_page={PER_PAGE}"
    url = f"{URL}{API_KEY}"
    params = {"q": query, "order": order, "per_page": PER_PAGE}
    response = requests.get(url, params=params)
    if response:
        result = response.json()
        return result


def download_save_images(img_url: str, idx: str, image_dir: str):
    res = requests.get(img_url)
    img = Image.open(BytesIO(res.content))
    file_format = img_url[(img_url.rindex(".") + FILENAME_NEXT_POSITION):]
    dir = os.path.join(image_dir, f"id_{idx}.{file_format}")
    img.save(dir)


def download_save_image_threads(
        result: dict,
        image_dir: str,
        X_RATE_LIMIT: int,
        TIME_SLEEP:int,
):
    threads = []
    rate_limit = 0
    for set_image in result["hits"]:
        threads.append(
            th(
                target=download_save_images,
                args=(set_image["webformatURL"], set_image["id"], image_dir)
            )
        )
        rate_limit += 1
        if rate_limit >= X_RATE_LIMIT:
            [th.start() for th in threads]
            time.sleep(TIME_SLEEP)
            threads = []
            rate_limit = 0
            continue
    [th.start() for th in threads]


def main():
    query = input("Type theme for images to download: ")
    query = preparation_query(query)
    result: dict = get_request(API_KEY, URL, query, PER_PAGE)
    download_save_image_threads(result, image_dir, X_RATE_LIMIT, TIME_SLEEP)


# Entrypoint
if __name__ == "__main__":
    main()
