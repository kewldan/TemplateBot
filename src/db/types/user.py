from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: Optional[str]
    joined: int
