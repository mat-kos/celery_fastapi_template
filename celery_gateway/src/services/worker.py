from celery import Celery
from ..dto.worker import WorkerDTO
from ..async_tools import run_async


# usefull links:
#   - https://docs.celeryq.dev/en/stable/reference/celery.app.control.html
#   - https://docs.celeryq.dev/en/stable/reference/celery.app.task.html#celery.app.task.Task


class WorkerService:

    celery_app: Celery

    def __init__(self, celery_app: Celery) -> None:
        self.celery_app = celery_app

    @run_async
    def list_workers(self) -> list[WorkerDTO]: 
        workers_plain_stats = self.celery_app.control.inspect().stats()
        return [
            WorkerDTO(
                name=worker_name,
                tasks=[], # TODO attach information about worker tasks
                **worker_info
            ) for worker_name, worker_info in workers_plain_stats.items()
        ]