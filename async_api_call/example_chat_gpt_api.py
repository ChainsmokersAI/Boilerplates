import argparse
import os

import asyncio
import aiohttp
from tqdm import tqdm

async def api_call(api_key, prompt, i, p_bar):
    # Interval
    await asyncio.sleep(i)

    # Headers
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }
    # Data
    data = {
        "model": "gpt-3.5-turbo-0613",
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.post("https://api.openai.com/v1/chat/completions", json=data) as res:
                response = await res.json()
                # Update Progress Bar
                p_bar.update(1)

                if res.status != 200:
                    """ Handle Error Here """
                    return "Error"

                """ Handle Response Here """
                return response["choices"][0]["message"]["content"]
    except Exception as e:
        # Update Progress Bar
        p_bar.update(1)

        """ Handle Exception Here """
        return "Exception"

async def call_api(n_calls, api_key, prompt):
    # Progress Bar
    p_bar = tqdm(total=n_calls, desc="ChatGPT Generated")

    # Tasks (Jobs)
    api_calls = [asyncio.create_task(
        api_call(api_key=api_key, prompt=prompt, i=i, p_bar=p_bar)
    ) for i in range(n_calls)]

    # Gather
    results = await asyncio.gather(*api_calls)
    for result in results:
        print("===")
        print(result)

def main():
    # Arguments Parsing
    parser = argparse.ArgumentParser(description="ChatGPT API Example")
    parser.add_argument("--api-key", type=str, default=os.getenv("OPENAI_API_KEY"), help="OpenAI API Key")
    parser.add_argument("--n-calls", type=int, required=True, help="Number of API Calls")
    parser.add_argument("--prompt", type=str, required=True, help="Single Prompt")
    args = parser.parse_args()

    asyncio.run(call_api(n_calls=args.n_calls, api_key=args.api_key, prompt=args.prompt))

if __name__ == "__main__":
    main()
