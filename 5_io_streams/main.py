
# %matplotlib inline
import os
import aiohttp
import asyncio
import pathlib
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)

with open('password.txt', 'w', encoding='utf-8') as f:
    f.write('20123')
    f.write('321')

with os.scandir('.') as entries:
    for entry in entries:
        print(f'{entry.name} -> {entry.stat().st_size} bytes')

# async def roots():
#
#     async with aiohttp.ClientSession() as session:
#         async with session.get('http://python.org') as responce:
#             print(responce.status)
#             print(responce.headers)
#
#             html = await responce.text()
#             print(html)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(roots())

pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
data = pd.read_csv('bikes.csv',
                   sep=';', encoding='latin1',
                   parse_dates=['Date'], dayfirst=True,
                   index_col='Date')
print(data['Berri 1'])
print(data['Rachel1'].sum())
data['Berri 1'].plot()
plt.savefig('plot.png')


# Создание Series из списка
s = pd.Series([1, 3, 5, 7, 9])
print(s)

# Создание Series с указанием индексов
s = pd.Series([1, 3, 5], index=['a', 'b', 'c'])
print(s)
