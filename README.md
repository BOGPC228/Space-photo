# Загружаем фотографии космоса

Модули для загрузки фотографий космоса с источников api.nasa и SpaceX, nasa.epic.

## Запуск

Для запуска блога у вас уже должен быть установлен Python 3.

- Скачайте код
- Установите зависимости командой 
```python
    pip install -r requirements.txt
```
- Для загрузки фотографий с проекта NASA запустите команду 
```python
    python3 picture_day_nasa.py
```
- Для загрузки фотографий с проекта NASA.EPIC запустите команду 
```python
    python3 photo_planet_epic.py
```
- Для загрузки фотографий с проекта SpaceX запустите команду 
```python
    python3 fetch_spacex_images.py
```
- Для публикации изображения в Telegram запустите команду 
```python
    python3 publish_image_to_telegram.py
```

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` в папке с модулями `fetch_spacex_images.py`,`photo_planet_epic.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны следущие переменные:

- `TOKEN_NASA` — см секретный ключ проекта. [сайт API.NASA](https://api.nasa.gov/?search=#apod). Например: `TOKEN_NASA=erofheronoirenfoernfx49389f43xf3984xf9384`.
- `BOT_TOKEN` = ключ вашего бота полученный от Botfather(Telegram). Например: `BOT_TOKEN=5312643774:AAGvL_lkprDLpDivGeSTFaNQjO7rYDx-VpU`.
- `DELAY_TIME` = время отправки ваших фотографий в Telegram. Значение указывается в секундах. Пример: `DELAY_TIME=20`
- `TG_CHAT_ID` = отвечает за канал на котором вы хотите выкладывать фотографии. Пример: `TG_CHAT_ID=@cosmos_py`

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
