init:
	cd ./apps/api; \
		python3.11 -m venv env; \
		./env/bin/python -m pip install -r requirements.txt
	cd ./apps/worker; \
		python3.11 -m venv env; \
		./env/bin/python -m pip install -r requirements.txt
	
update_requirements:
	cd ./apps/api; \
		./env/bin/python -m pip freeze > requirements.txt
	cd ./apps/worker; \
		./env/bin/python -m pip freeze > requirements.txt

run:
	docker compose -f ./docker/compose.yml up -d

run_dev:
	docker compose -f ./docker/compose.yml up -d rabbitmq redis flower