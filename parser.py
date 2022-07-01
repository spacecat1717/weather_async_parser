import asyncio
from aiohttp import ClientSession

async def get_weather(city):
    """getting weather"""
    async with ClientSession() as session:
        #connect to api
        url = f'http://api.openweathermap.org/data/2.5/weather?&units=metric'
        params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}

        async with session.get(url=url, params=params) as response:
            #getting weather
            weather_json = await response.json()
            return f'{city}: {weather_json["main"]["temp"]}'

async def main(cities):
    tasks = []
    for city in cities:
        tasks.append(asyncio.create_task(get_weather(city)))

    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)

cities = ['St. Petersburg', 'Moscow', 'Dublin']

asyncio.run(main(cities))