import requests
from urllib.parse import urlparse


def is_shorten_link(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc == 'vk.cc'


def get_shorten_url(VK_API, long_url):
    try:
        url = "https://api.vk.com/method/utils.getShortLink"
        params = {
            "access_token": VK_API,
            "v": "5.199",
            "url": long_url
        }
        response = requests.get(url, params=params)
        response.raise_for_status()

        response_data = response.json()
        if "error" in response_data:
            error_message = response_data["error"].get("error_msg", "Неизвестная ошибка")
            error_code = response_data["error"].get("error_code", "Неизвестный код ошибки")
            raise ValueError(f"Ошибка VK API: {error_message} (Код ошибки: {error_code})")

        return response_data["response"]["short_url"]

    except ValueError as error:
        print(f"Ошибка: {error}")
    except requests.exceptions.HTTPError as error:
        print(f"HTTP ошибка: {error}")
    except Exception as error:
        print(f"Неожиданная ошибка: {error}")


def count_clicks(VK_API, short_url, interval='forever', intervals_count=1, extended=0):
    parsed_url = urlparse(short_url)
    key = parsed_url.path.split("/")[-1]

    try:
        url = "https://api.vk.com/method/utils.getLinkStats"
        params = {
            "access_token": VK_API,
            "v": "5.199",
            "key": key,
            "interval": interval,
            "intervals_count": intervals_count,
            "extended": extended
        }
        response = requests.get(url, params=params)
        response.raise_for_status()

        response_data = response.json()
        if "error" in response_data:
            error_message = response_data["error"].get("error_msg", "Неизвестная ошибка")
            error_code = response_data["error"].get("error_code", "Неизвестный код ошибки")
            raise ValueError(f"Ошибка VK API: {error_message} (Код ошибки: {error_code})")

        stats = response_data["response"]["stats"]
        if stats:
            for stat in stats:
                print(f"Переходы по ссылке: {stat['views']}")
        else:
            print("Нет данных по переходам.")
    except ValueError as error:
        print(f"Ошибка: {error}")
    except requests.exceptions.HTTPError as error:
        print(f"HTTP ошибка: {error}")
    except Exception as error:
        print(f"Неожиданная ошибка: {error}")


def main():
    VK_API = '360755ac360755ac360755ac703521e8d433607360755ac51636c720d2a5a73361619a6'
    long_url = input("Введите ссылку: ")
    if is_shorten_link(long_url):
        count_clicks(VK_API, long_url)
    else:
        short_url = get_shorten_url(VK_API, long_url)
        if short_url:
            print('Сокращенная ссылка: ', short_url)
        else:
            print("Не удалось получить сокращенную ссылку!")


if __name__ == '__main__':
    main()