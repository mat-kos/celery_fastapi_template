from enum import StrEnum
from pydantic import BaseSettings, AmqpDsn, RedisDsn


class LogLevel(StrEnum):

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class PoolType(StrEnum):

    PREFORK = "prefork"
    THREADS = "threads"
    SOLO = "solo"
    EVENTLET = "eventlet"
    GEVENT = "gevent"


class AppConfig(BaseSettings):

    log_level: LogLevel = LogLevel.INFO
    pool_type: PoolType = PoolType.PREFORK
    concurrency: int = 1
    prefetch_multiplier: int = 1
    broker_url: AmqpDsn = "amqp://user:password@localhost:5001//"
    backend_url: RedisDsn = "redis://:password@localhost:5003/0/"
    imports: list[str] = ["src.tasks"]
    heartbeat: int = 10