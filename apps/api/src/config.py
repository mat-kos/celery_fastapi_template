from enum import StrEnum
from pydantic import BaseSettings, AmqpDsn, RedisDsn


routers_paths = [
    "src.routers.state.state_router",
    "src.routers.worker.worker_router"
]


class AppConfig(BaseSettings):
    
    broker_url: AmqpDsn = "amqp://user:password@localhost:5001//"
    backend_url: RedisDsn = "redis://:password@localhost:5003/0/"