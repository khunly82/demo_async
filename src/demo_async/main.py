import asyncio
import os
from types import CoroutineType

from dotenv import load_dotenv
from httpx import AsyncClient

load_dotenv()

API_KEY = os.getenv('API_KEY')
URL = 'https://api.openai.com/v1/chat/completions'
COUNTRIES = ['France', 'Vietnam', 'Ghana', 'Lettonie']
MODEL = 'gpt-4o-mini-2024-07-18'
DEFAULT_HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {API_KEY}'
}

async def get_capitale_async(country: str) -> CoroutineType[str]:
    async with AsyncClient() as client:
        result = await client.post(URL, headers=DEFAULT_HEADERS, json={
            'model': MODEL,
            'messages': [
                { 'role': 'system', 'content': 'Ton role est de repondre à user en lui donner la capitale du pays qu\'il va te donner' },
                { 'role': 'user', 'content': country }
            ]    
        })

        return result.json().get('choices')[0].get('message').get('content')

async def main_async():
    # async with AsyncClient() as client:
    #     result = await client.post(URL, headers=DEFAULT_HEADERS, json={
    #         'model': MODEL,
    #         'messages': [
    #             { 'role': 'system', 'content': 'Tu es un assistant super chiant qui repond à coté de la plaque et qui insulte le user. Soit tres tres vulgaire !!' },
    #             { 'role': 'user', 'content': 'Comment en fait de l\'asynchrone en python ?' }
    #         ]
    #     })

    #     print(result.json())

    # envoi de toutes les requetes en même temps 
    result = await asyncio.gather(*[get_capitale_async(c) for c in COUNTRIES])
    print(result)

def main():
    asyncio.run(main_async())