import asyncio
import aiohttp
import cProfile
import pstats
import io

MAX_CONCURRENT_REQUESTS = 10


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def fetch_with_semaphore(semaphore, session, url):
    async with semaphore:
        return await fetch(session, url)


async def fetch_multiple_urls(urls):
    semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_with_semaphore(semaphore, session, url) for url in urls]
        responses = await asyncio.gather(*tasks)
        return responses


def profile_main():
    urls = ['http://google.com'] * 20

    pr = cProfile.Profile()
    pr.enable()

    responses = asyncio.run(fetch_multiple_urls(urls))
    print(f"Received {len(responses)} responses.")

    pr.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())


if __name__ == '__main__':
    profile_main()
