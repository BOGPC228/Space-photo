# Загружаем фотографии космоса

Модули для загрузки фотографий космоса с источников api.nasa и SpaceX, nasa.epic.

## Запуск

Для запуска блога у вас уже должен быть установлен Python 3.

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Запустите один из модулей командой `python3 nasa.py` , доступные модули (`fetch_spacex_images.py`, `nasa.py`, `epic.py`, `publish_image_to_telegram.py`)
- Для загрузки фотографий с проекта NASA запустите команду `python3 nasa.py` 
- Для загрузки фотографий с проекта NASA.EPIC запустите команду `python3 epic.py`
- Для загрузки фотографий с проекта SpaceX запустите команду `fetch_spacex_images.py`
- Для публикации изображения в Telegram запустите команду `publish_image_to_telegram.py`

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` в папке с модулями `fetch_spacex_images.py`,`epic.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны следущие переменные:

- `TOKEN_NASA` — см секретный ключ проекта. [сайт API.NASA](https://api.nasa.gov/?search=#apod). Например: `TOKEN_NASA=erofheronoirenfoernfx49389f43xf3984xf9384`.
- `TOKEN_BOT` = ключ вашего бота полученный от Botfather(Telegram). Например: `TOKEN_BOT=5312643774:AAGvL_lkprDLpDivGeSTFaNQjO7rYDx-VpU`.
- `TIME` = время отправки ваших фотографий в Telegram. Значение указывается в секундах. Пример: `TIME=20`
- `CHAT_ID_TG` = отвечает за канал на котором вы хотите выкладывать фотографии. Пример: `CHAT_ID_TG=@cosmos_py`

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
