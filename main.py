import requests


def get_shorten_url(VK_API, long_url):
    url = "https://api.vk.com/method/utils.getShortLink"
    params = {
        "access_token": VK_API,
        "v": "5.199",
        "url": long_url
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()["response"]["short_url"]


def long_url(VK_API, url):
    long_url = input("Введите ссылку: ")

def shorten_url(VK_API, long_url):
    return get_shorten_url(VK_API, long_url)


def main():
    VK_API = '360755ac360755ac360755ac703521e8d433607360755ac51636c720d2a5a73361619a6'
    long_url = input("Введите ссылку: ")
    short_url = get_shorten_url(VK_API, long_url)
    print('Сокращенная ссылка: ', shorten_url)


if __name__ == '__main__':
    main()