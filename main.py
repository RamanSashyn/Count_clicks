import os
import requests
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv


def is_shorten_link(url, access_token):
    parsed_url = urlparse(url)
    if parsed_url.netloc != "vk.cc":
        return False

    key = parsed_url.path.replace("/", "")
    url = "https://api.vk.com/method/utils.getLinkStats"
    params = {
        "access_token": access_token,
        "v": "5.199",
        "key": key,
        "interval": "forever",
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    response_data = response.json()

    return "error" not in response_data

def get_shorten_url(access_token, long_url):
    url = "https://api.vk.com/method/utils.getShortLink"
    params = {"access_token": access_token, "v": "5.199", "url": long_url}

    response = requests.get(url, params=params)
    response.raise_for_status()

    response_data = response.json()

    if "error" in response_data:
        error_message = response_data["error"].get(
            "error_msg", "Неизвестная ошибка"
        )
        error_code = response_data["error"].get(
            "error_code", "Неизвестный код ошибки"
        )
        raise ValueError(
            f"Ошибка VK API: {error_message} (Код ошибки: {error_code})"
        )

    return response_data["response"]["short_url"]


def count_clicks(
    access_token, short_url, interval="forever", intervals_count=1, extended=0
):
    parsed_url = urlparse(short_url)
    key = parsed_url.path.split("/")[-1]

    url = "https://api.vk.com/method/utils.getLinkStats"
    params = {
        "access_token": access_token,
        "v": "5.199",
        "key": key,
        "interval": interval,
        "intervals_count": intervals_count,
        "extended": extended,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    response_data = response.json()

    if "error" in response_data:
        error_message = response_data["error"].get(
            "error_msg", "Неизвестная ошибка"
        )
        error_code = response_data["error"].get(
            "error_code", "Неизвестный код ошибки"
        )
        raise ValueError(
            f"Ошибка VK API: {error_message} (Код ошибки: {error_code})"
        )

    stats = response_data["response"]["stats"]

    if stats:
        return [stat['views'] for stat in stats]
    else:
        return []


def main():
    load_dotenv()

    try:
        vk_access_token = os.environ["VK_ACCESS_TOKEN"]
    except KeyError:
        print("Переменная окружения VK_ACCESS_TOKEN не установлена.")
        return

    parser = argparse.ArgumentParser(
        description='Скрипт для работы с сокращенными ссылками.'
    )
    parser.add_argument(
        'url',
        help='Ссылка, которую нужно сократить или проверить'
    )
    args = parser.parse_args()
    long_url = args.url

    try:
        if is_shorten_link(long_url, vk_access_token):
            clicks_info = count_clicks(vk_access_token, long_url)
            if clicks_info:
                for click in clicks_info:
                    print(f"По вашей ссылке перешли {click} раз")
            else:
                print("Нет данных по переходам.")
        else:
            short_url = get_shorten_url(vk_access_token, long_url)
            print(short_url)

    except ValueError as error:
        print(f"Ошибка: {error}")

    except requests.exceptions.HTTPError as error:
        print(f"Ошибка HTTP: {error}")

    except KeyError as error:
        print(f"Ошибка с ключом: {error}")


if __name__ == "__main__":
    main()

