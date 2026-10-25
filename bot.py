import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import aiohttp
from config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

CURRENCIES = ["USD", "EUR", "GBP", "RUB", "KZT", "CNY"]
API_URL = "https://api.exchangerate-api.com/v4/latest/{base}"


async def fetch_rates(base: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL.format(base=base)) as resp:
            data = await resp.json()
            return data["rates"]


def currency_keyboard() -> InlineKeyboardMarkup:
    buttons = [[InlineKeyboardButton(text=c, callback_data=f"base:{c}")] for c in CURRENCIES]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


@dp.message(Command("start"))
async def cmd_start(msg: Message):
    await msg.answer(
        "Привет! Я показываю актуальные курсы валют.\n"
        "Выбери базовую валюту:",
        reply_markup=currency_keyboard()
    )


@dp.callback_query(F.data.startswith("base:"))
async def on_base_selected(cb: CallbackQuery):
    base = cb.data.split(":")[1]
    rates = await fetch_rates(base)
    lines = [f"1 {base} = {rates[c]:.4f} {c}" for c in CURRENCIES if c != base]
    await cb.message.edit_text(
        f"Курсы к {base}:\n\n" + "\n".join(lines),
        reply_markup=currency_keyboard()
    )
    await cb.answer()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
