import asyncio, random, time
from aiohttp import ClientSession

async def get_word(num):
    """getiing word"""
    #connect
    async with ClientSession() as session:
        url=f'https://www.randomlists.com/data/words.json'

        async with session.get(url=url) as response:
            word_json = await response.json()
            #add return
            return f'{word_json["data"][num]}'

async def main(num):
    """create task"""
    
    task = asyncio.create_task(get_word(num))
    res = await task
    return res
     
  



