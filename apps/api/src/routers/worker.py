from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject
from ..api_models.worker import Worker
from ..services.worker import WorkerService
from ..containers import AppContainer


worker_router = APIRouter(prefix="/worker", tags=["worker"])


@worker_router.get("/")
@inject
def list_workers(worker_service: WorkerService = Depends(Provide[AppContainer.worker_service])) -> list[Worker]:
    return [Worker(**worker_dto.dict()) for worker_dto in worker_service.list_workers()]