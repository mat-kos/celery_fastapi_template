from celery import shared_task


@shared_task(name="add")
def add(x: int, y: int) -> int:
    return x + y


@shared_task(name="multiply")
def multiply(x: int, y: int) -> int:
    return x * y


@shared_task(name="divide")
def divide(x: int, y: int) -> float:
    return x / y