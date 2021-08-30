import asyncio


async def main():
    print('Tim')


async def pack():
    print('pack')


async def foo(text):
    print(text)
    await asyncio.sleep(1)


asyncio.run(foo('main'))
