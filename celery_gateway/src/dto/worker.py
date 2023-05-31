from pydantic import BaseModel


class WorkerDTO(BaseModel):

    name: str
    prefetch_count: int
    rusage: dict
    tasks: list[str]
    broker: dict
    pool: dict
    uptime: int
    pid: int
    clock: str
    total: dict