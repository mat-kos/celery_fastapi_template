from datetime import datetime
from pydantic import BaseModel


class Worker(BaseModel):

    name: str
    tasks: list[str]