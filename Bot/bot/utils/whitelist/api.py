import os
import aiohttp

request_url = os.getenv("WHITELIST_API_URL")
request_headers = {
    "Content-Type": "application/json",
    "Authorization": f"WHA {os.getenv('WHITELIST_API_TOKEN')}"
}


async def get_whitelist() -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get(request_url, headers=request_headers) as response:
            data = await response.json()
            return data


async def add_nickname_to_whitelist(nickname: str) -> None:
    request_data = {
        "name": nickname
    }
    async with aiohttp.ClientSession() as session:
        response = await session.post(request_url, headers=request_headers, json=request_data)


async def remove_nickname_from_whitelist(nickname: str) -> None:
    request_data = {
        "name": nickname
    }
    async with aiohttp.ClientSession() as session:
        response = await session.delete(request_url, headers=request_headers, json=request_data)
