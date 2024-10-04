import asyncio
import random
from asyncio import InvalidStateError

from django.db.models.expressions import result


async def shield_system():
    await asyncio.sleep(3)

    if random.random() < 0.3:
        raise Exception("Ошибка в системе щитов: перегрев!")
    return  "Щиты подняты"

async def weapon_system():
    await asyncio.sleep(4)
    return "Оружие заряжено"

async def navigation_system():
    await asyncio.sleep(1)

    if random.random() < 0.2:
        raise Exception("Ошибка в системе навигации: сбой связи!")

    return "Курс задан"


async def launch_battle_systems():
    results = await asyncio.gather(
        shield_system(),
        weapon_system(),
        navigation_system(),
        return_exceptions=True
    )

    for result in results:
        if isinstance(result, Exception):
            print(f'Произошла ошибка :{result}')
        else:
            print(result)



if __name__ == '__main__':
    asyncio.run(launch_battle_systems())
