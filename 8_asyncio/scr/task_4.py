import asyncio
import aiohttp
import aiofiles


async def fetch(session, url):
    async with session.get(url) as response:
        return response.status


async def fetch_with_semaphore(semaphore, session, url):
    async with semaphore:
        return await fetch(session, url)


async def fetch_statuses(url, num_requests, max_concurrent_requests, output_file):
    semaphore = asyncio.Semaphore(max_concurrent_requests)
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_with_semaphore(semaphore, session, url) for _ in range(num_requests)]
        statuses = await asyncio.gather(*tasks)

        async with aiofiles.open(output_file, 'w', encoding='UTF-8') as file:
            for status in statuses:
                await file.write(f"{status}\n")

        print(f"Всего выполнено запросов: {len(statuses)}")
        print(f"Статусы записаны в файл {output_file}")


if __name__ == '__main__':
    url = 'https://example.com/'
    num_requests = 50
    max_concurrent_requests = 10
    output_file = 'statuses.txt'

    asyncio.run(fetch_statuses(url, num_requests, max_concurrent_requests, output_file))
