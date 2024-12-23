import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv


def is_shorten_link(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc == "vk.cc"


def get_shorten_url(VK_API, long_url):
    try:
        url = "https://api.vk.com/method/utils.getShortLink"
        params = {"access_token": VK_API, "v": "5.199", "url": long_url}

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

    except ValueError as error:
        raise error

    except requests.exceptions.HTTPError as error:
        raise error

    except Exception as error:
        raise Exception(f"Неожиданная ошибка: {error}")


def count_clicks(
    VK_API, short_url, interval="forever", intervals_count=1, extended=0
):
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
            return [f"Переходы по ссылке: {stat['views']}" for stat in stats]
        else:
            return ["Нет данных по переходам."]

    except ValueError as error:
        raise error

    except requests.exceptions.HTTPError as error:
        raise error

    except Exception as error:
        raise Exception(f"Неожиданная ошибка: {error}")


def main():
    load_dotenv()
    VK_API = os.getenv("VK_API")

    long_url = input("Введите ссылку: ")

    if is_shorten_link(long_url):
        try:
            clicks_info = count_clicks(VK_API, long_url)

            for click in clicks_info:
                print(click)

        except Exception as error:
            print(f"Ошибка при получении статистики: {error}")

    else:
        try:
            short_url = get_shorten_url(VK_API, long_url)
            print("Сокращенная ссылка:", short_url)

        except Exception as error:
            print(f"Ошибка при получении сокращенной ссылки: {error}")


if __name__ == "__main__":
    main()
