# celery gateway

init:
	cd ./apps/api; \
		python3.11 -m venv env; \
		./env/bin/python -m pip install -r requirements.txt
	
update_requirements:
	cd ./apps/api; \
		./env/bin/python -m pip freeze > requirements.txt

build_celery_gateway_image:
	docker build -t celery_gateway:latest -f ./celery_gateway/Dockerfile ./celery_gateway


# examples

build_simple_worker_image:
	docker build -t simple_celery_worker:latest -f ./examples/simple_stack_integration/simple_worker/Dockerfile ./examples/simple_stack_integration/simple_worker
	
run:
	docker compose -f ./examples/simple_stack_integration/docker-compose.yml up -d

run_dev:
	docker compose -f ./examples/simple_stack_integration/docker-compose.yml up -d rabbitmq redis flower worker