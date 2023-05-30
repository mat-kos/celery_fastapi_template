from celery import Celery
from concurrent.futures import ThreadPoolExecutor
from dependency_injector import containers, providers
from .config import wire_packages
from .celery_app import create_celery_app
from .services.worker import WorkerService


class AppContainer(containers.DeclarativeContainer):

    # MAIN

    config = providers.Configuration()

    celery_app: providers.Provider[Celery] = providers.Resource(
        create_celery_app,
        config.broker_url,
        config.backend_url
    )

    worker_pool: providers.Provider[ThreadPoolExecutor] = providers.Resource(
        ThreadPoolExecutor,
        max_workers=config.pool_workers
    )

    # SERVICES

    worker_service: providers.Provider[WorkerService] = providers.Factory(
        WorkerService,
        celery_app
    )


