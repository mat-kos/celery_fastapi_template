from celery import Celery
from .config import AppConfig


def create_app() -> Celery:
    config = AppConfig()
    celery_app = Celery(
        broker=config.broker_url, 
        backend=config.backend_url
    )
    setattr(celery_app, "user_config", config)
    celery_app.conf.update(
        task_serializer="pickle",
        result_serializer="pickle",
        accept_content=["pickle", "json"],
        broker_heartbeat=config.heartbeat,
        imports=config.imports,
        worker_pool=config.pool_type,
        worker_prefetch_multiplier=config.prefetch_multiplier,
        worker_concurrency=config.concurrency,
        worker_send_task_events=True,
        task_ignore_result=False,
    )
    return celery_app