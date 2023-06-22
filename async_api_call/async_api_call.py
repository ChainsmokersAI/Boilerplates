import argparse

import asyncio
import aiohttp
from tqdm import tqdm

async def api_call(i, p_bar):
    # Interval
    await asyncio.sleep(i)

    # Headers
    headers = {}
    # Data
    data = {}

    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.post("https://lorem.ipsum", json=data) as res:
                response = await res.json()
                # Update Progress Bar
                p_bar.update(1)

                if res.status != 200:
                    """ Handle Error Here """

                """ Handle Response Here """
    except Exception as e:
        # Update Progress Bar
        p_bar.update(1)

        """ Handle Exception Here """

async def call_api():
    # Progress Bar
    p_bar = tqdm(total=, desc="Lorem Ipsum")

    # Tasks (Jobs)
    api_calls = [asyncio.create_task(
        api_call(i=i, p_bar=p_bar)
    ) for i in range()]

    # Gather
    results = await asyncio.gather(*api_calls)

def main():
    # Arguments Parsing
    parser = argparse.ArgumentParser(description="Lorem Ipsum")
    #parser.add_argument("", type=, required=True, choices=, help="")
    #parser.add_argument("", type=, default=, choices=, help="")
    args = parser.parse_args()

    asyncio.run(call_api())

if __name__ == "__main__":
    main()
