from celery import Celery
from .config import AppConfig


def create_celery_app(
            broker_url: str,
            backend_url: str
        ) -> Celery:
    celery_app = Celery(
        broker=broker_url, 
        backend=backend_url,
    )
    celery_app.conf.update(
        accept_content=["pickle", "json"]
    )
    return celery_app