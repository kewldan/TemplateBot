import math
import time
from typing import Optional

import motor.motor_asyncio

from config import config
from db.types.user import User

client = motor.motor_asyncio.AsyncIOMotorClient(config['bot']['mongo'])
database = client[config['bot']['database']]
users = database['users']


async def get_user(user_id: int, username: Optional[str]) -> User:
    user = await users.find_one({'id': user_id})
    if not user:
        await users.insert_one({
            'id': user_id,
            'username': username,
            'joined': math.floor(time.time())
        })
        user = await users.find_one({'id': user_id})
    return User(**user)
