# VK Link Shortener & Click Counter

Этот скрипт позволяет работать с VK API для сокращения ссылок и получения статистики переходов по ним.  
Он принимает ссылку в качестве аргумента командной строки и выполняет одно из следующих действий:
- Проверяет, является ли ссылка сокращённой через VK.cc.
- Если ссылка сокращённая, возвращает количество переходов по ней.
- Если ссылка длинная, сокращает её с помощью VK API.

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/your-username/count_clicks.git
    cd count_clicks
    ```

2. Создайте виртуальное окружение:

    ```bash
    python -m venv venv
    ```

    Для активации виртуального окружения:

    - **Linux/MacOS**:
    
    ```bash
    source venv/bin/activate
    ```

    - **Windows**:
    
    ```bash
    venv\Scripts\activate
    ```

3. Установите зависимости:

    Установите необходимые библиотеки с помощью следующей команды:

    ```bash
    pip install -r requirements.txt
    ```

4. Создайте файл `.env` и добавьте в него ваш токен доступа к VK API:

    ```plaintext
    VK_ACCESS_TOKEN=ваш_токен_доступа
    ```
Получить токен можно, создав приложение VK на [странице разработчиков VK.](https://dev.vk.com/ru)

## Использование

Запустите скрипт, передав ссылку в качестве аргумента:
```bash
python main.py <ваша_ссылка>
```

## Примеры использования

1. **Сокращение длинной ссылки:**
   - Передайте длинную ссылку, чтобы получить её сокращённый вариант.
   - Пример команды:
        ```bash
        python main.py https://example.com
        ```

    - Результат:
        ```
        https://vk.cc/cvPDML # Сокращенная ссылка 
        ```

2. **Получение статистики переходов**:
    - Если передать уже сокращённую ссылку, скрипт вернёт количество переходов по ней.
    - Пример команды:
        ```bash
        python main.py https://vk.cc/cvPDML
        ```
    - Результат:
        ```
        Переходы по ссылке: 7
        ```

## Обработка ошибок

Скрипт обрабатывает следующие ошибки:

- **Ошибка VK API:** Если произошла ошибка на стороне VK API, будет выведено сообщение с кодом ошибки.
- **Ошибка HTTP:** Если запрос к API завершился неудачно, будет указана причина.
- **Отсутствие токена:** Если токен доступа не указан, скрипт предупредит об этом.

## Требования
- Python 3.9 или выше.
- Установленные зависимости из requirements.txt

## Лицензия

MIT License

Copyright (c) 2024 Raman Sashyn

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
