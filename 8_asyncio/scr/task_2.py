import asyncio
import aiofiles
import os


async def create_file(directory, template, index):
    filename = os.path.join(directory, template.format(index=index))
    async with aiofiles.open(filename, 'w', encoding='UTF-8') as f:
        content = f'Это файл под номером - {index}'
        await f.write(content)


async def main():
    directory = 'templates'
    template = "file_{index}.txt"

    os.makedirs(directory, exist_ok=True)

    tasks = [create_file(directory, template, i) for i in range(1, 11)]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())