# Telegram Currency Bot

Телеграм-бот для просмотра актуальных курсов валют с интерактивной клавиатурой.

## Возможности
- Курсы USD, EUR, GBP, RUB, KZT, CNY
- Выбор базовой валюты через inline-кнопки
- Актуальные данные из exchangerate-api.com

## Запуск
```bash
pip install -r requirements.txt
cp .env.example .env   # и вписать свой токен от @BotFather
python bot.py
```

Токен хранится в `.env`, который игнорируется git. Переменная окружения `BOT_TOKEN` тоже работает.

## Стек
- Python 3.11+
- aiogram 3.x (async framework для Telegram Bot API)
- aiohttp (асинхронные HTTP-запросы к API курсов)
