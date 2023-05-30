from pydantic import BaseSettings, AmqpDsn, RedisDsn


# INTERNAL CONFIGURATION


wire_packages = [
    "src.routers.worker",
    "src.async_tools"
]


routers_paths = [
    "src.routers.state.state_router",
    "src.routers.worker.worker_router"
]


# USER CONFIGURATION


class AppConfig(BaseSettings):
    
    pool_workers: int = 1
    broker_url: AmqpDsn = "amqp://user:password@localhost:5001//"
    backend_url: RedisDsn = "redis://:password@localhost:5003/0/"