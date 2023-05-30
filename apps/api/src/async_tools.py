from asyncio import get_event_loop
from typing import Callable, Coroutine, TypeVar, ParamSpec
from concurrent.futures import ThreadPoolExecutor
from dependency_injector.wiring import Provide, inject


T = ParamSpec('T')
R = TypeVar('R')


def run_async(
            f: Callable[T, R]
        ) -> Coroutine[None, T, R]:
    # lambda args and kwargs unpacking because run_in_executor don't accept kwargs
    packed_f = lambda args, kwargs: f(*args, **kwargs)
    @inject
    async def wrapper(
                *args, 
                worker_pool: ThreadPoolExecutor = Provide["worker_pool"], 
                **kwargs
            ):
        loop = get_event_loop()
        return await loop.run_in_executor(worker_pool, packed_f, args, kwargs)
    return wrapper