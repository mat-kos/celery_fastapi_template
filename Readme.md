# Celery gateway

- tasks and workers autodiscovery (in progress)
- tasks and workers information retrival (in progress)
- performing tasks (in progress)


## Simple cluster integration example
### Prerequisites:
- docker
- make
- git
```
git clone ...
cd celery_gateway
make build_celery_gateway_image
make build_simple_worker_image
make run
```
