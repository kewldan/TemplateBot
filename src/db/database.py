import math
import time
from typing import Optional

from beanie import Document, init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from config import config


class User(Document):
    id: int
    username: Optional[str] = None
    joined: int


client = AsyncIOMotorClient(config['bot']['mongo'])


async def connect():
    await init_beanie(database=client.db_name, document_models=[User])


async def get_user(user_id: int, username: Optional[str]) -> User:
    user = await User.find_one(User.id == user_id)
    if not user:
        user = User(id=user_id, username=username, joined=math.floor(time.time()))
        await user.insert()
    return user
