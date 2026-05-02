import asyncio


async def fazer_arroz():
    while True:
        print('Fazendo arroz...')
        await asyncio.sleep(3)
        print('Arroz pronto!')


async def fazer_carne():
    while True:
        print('Fazendo carne...')
        await asyncio.sleep(5)
        print('Carne pronta!')


async def fazer_feijao():
    while True:
        print('Fazendo feijão...')
        await asyncio.sleep(7)
        print('Feijão pronto!')


async def main():
    tasks = [
        asyncio.create_task(fazer_arroz()),
        asyncio.create_task(fazer_carne()),
        asyncio.create_task(fazer_feijao()),
    ]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())