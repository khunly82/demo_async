import asyncio
import os
from types import CoroutineType

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
URL = 'https://api.openai.com/v1/chat/completions'
COUNTRIES = ['France', 'Vietnam', 'Ghana', 'Lettonie']

from httpx import AsyncClient

async def get_capitale(country: str) -> CoroutineType[str]:
    async with AsyncClient() as client:
        result = await client.post(URL, headers={
             'Content-Type': 'application/json',
             'Authorization': f'Bearer {API_KEY}'
        }, json={
            'model': 'gpt-4o-mini-2024-07-18',
            'messages': [
                { 'role': 'system', 'content': 'Ton role est de repondre à user en lui donner la capitale du pays qu\'il va te donner' },
                { 'role': 'user', 'content': country }
            ]    
        })

        return result.json().get('choices')[0].get('message').get('content')

async def main_async():
    # async with AsyncClient() as client:
    #     result = await client.post(URL, headers={
    #         'Content-Type': 'application/json',
    #         'Authorization': f'Bearer {API_KEY}'
    #     }, json={
    #         'model': 'gpt-4o-mini-2024-07-18',
    #         'messages': [
    #             { 'role': 'system', 'content': 'Tu es un assistant super chiant qui repond à coté de la plaque et qui insulte le user. Soit tres tres vulgaire !!' },
    #             { 'role': 'user', 'content': 'Comment en fait de l\'asynchrone en python ?' }
    #         ]
    #     })

    result = await asyncio.gather(*[get_capitale(c) for c in COUNTRIES])
    print(result)

    #     print(result.json())

def main():
    asyncio.run(main_async())