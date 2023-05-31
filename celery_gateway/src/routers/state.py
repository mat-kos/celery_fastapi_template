from fastapi import APIRouter


state_router = APIRouter(prefix="/state", tags=["state"])


@state_router.get("/healthy")
async def healthy() -> bool:
    return True