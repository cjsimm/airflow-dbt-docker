#initiates the example database 
init-example:
	get-data 
get-data:
	@echo "Getting data..." 
	rm -rf ./example-db/seed-data/
	mkdir ./example-db/seed-data
	curl -o ./example-db/seed-data/titanic.csv https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
clean-logs:
	rm -rf ./airflow/logs
	mkdir ./airflow/logs
docker-spin:
	docker compose up airflow-init && docker compose up --build -d
up:
	get-data 
	docker-spin
down:
	docker compose down
