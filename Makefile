# Create Docker network
network:
	docker network create confluent || true

# Build Docker images using airflow/docker-compose.yaml
build:
	docker-compose -f airflow/docker-compose.yaml build

# Start Docker Compose services
up: network
	docker-compose up -d
	docker-compose -f airflow/docker-compose.yaml up -d

# Stop and remove Docker containers and network
down:
	docker-compose down
	docker-compose -f airflow/docker-compose.yaml down
	docker network rm confluent || true

# Restart Docker Compose services
restart:
	docker-compose restart
	docker-compose -f airflow/docker-compose.yaml restart

# Remove all Docker images from all Docker Compose files
clean:
	docker-compose down --rmi all -v
	docker-compose -f airflow/docker-compose.yaml down --rmi all -v
	docker network rm confluent || true
