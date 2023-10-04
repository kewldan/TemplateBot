from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message

from db import database


class UserFetchMiddleware(BaseMiddleware):

    async def __call__(self, handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]], event: Message,
                       data: Dict[str, Any]) -> Any:
        user = await database.get_user(event.from_user.id, event.from_user.username)

        if user.username and user.username != event.from_user.username:
            await user.update({'$set': {'username': event.from_user.username}})

        data['user'] = user

        return await handler(event, data)
