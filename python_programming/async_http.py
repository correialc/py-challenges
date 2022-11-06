import aiohttp
import asyncio

async def get_cat(url, session):
        async with session.get(url, ssl=False) as resp:
            print(await resp.text)

async def main(url):
    await session = aiohttp.ClientSession()
    await get_cat(url, session)
    #await asyncio.gather(get_cat(url, session), get_cat(url, session))

if __name__ == "__main__":
    url = "https://cataas.com/cat?json=true"
    asyncio.run(main(url))