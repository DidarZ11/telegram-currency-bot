# Telegram Currency Bot

Телеграм-бот для просмотра актуальных курсов валют с интерактивной клавиатурой.

## Возможности
- Курсы USD, EUR, GBP, RUB, KZT, CNY
- Выбор базовой валюты через inline-кнопки
- Актуальные данные из exchangerate-api.com

## Запуск
```bash
pip install -r requirements.txt
export BOT_TOKEN="your_token_from_botfather"
python bot.py
```

## Стек
- Python 3.11+
- aiogram 3.x (async framework для Telegram Bot API)
- aiohttp (асинхронные HTTP-запросы к API курсов)
