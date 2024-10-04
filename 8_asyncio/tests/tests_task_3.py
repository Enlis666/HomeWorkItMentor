import pytest
from aioresponses import aioresponses
from scr.task_3 import fetch_multiple_urls


@pytest.mark.asyncio
async def test_fetch_multiple_urls():
    urls = ['http://google.com'] * 10

    with aioresponses() as m:
        for url in urls:
            m.get(url, body='Test Response')

        responses = await fetch_multiple_urls(urls)

        assert len(responses) == len(urls)
        for response in responses:
            assert response == 'Test Response'

