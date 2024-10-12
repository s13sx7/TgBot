from aiogram import Router
import aiohttp

from aiogram import F
from aiogram import types
from aiogram.filters.command import Command
from config import settings
from kb import menu
    
    
router = Router()

@router.message(Command('start'))
async def command_start(msg: types.Message):
    await msg.answer("Привет! Это бот для погоды!\nУкажите город в котором хоите узнать погоду", reply_markup=menu)

@router.message(F.text =='/help')
async def command_help(msg: types.Message):
    await msg.answer('Коректно укажите название города!')

@router.message(F.text)
async def query_name(msg: types.Message):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(f'https://api.openweathermap.org/data/2.5/weather?q={msg.text}&units={settings.Units}&lang=ru&appid={settings.WeatherToken}') as response:
                if response.status==200:
                    data = await response.json()
                    await msg.answer(f'Город: {data['name']}\nПогода: {data['weather'][0]['description']}\nТемпература(C): {data['main']['temp']}')
                else:
                    await msg.answer('Не удалось получит ответ')
        except Exception as e:
            print(e)  
            await msg.answer('Ошибка запроса')