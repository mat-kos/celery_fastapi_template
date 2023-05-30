from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject
from ..api_models.worker import Worker
from ..services.worker import WorkerService


worker_router = APIRouter(prefix="/worker", tags=["worker"])


@worker_router.get("/")
@inject
async def list_workers(
            worker_service: WorkerService = Depends(Provide["worker_service"])
        ) -> list[Worker]:
    return [
        Worker(**worker_dto.dict()) \
            for worker_dto in await worker_service.list_workers()]