DOCKER_COMPOSE = docker compose
DOCKER = docker
IMAGE_NAME = sre-bootcamp-api
IMAGE_TAG = 1.0.0
MIGRATION_MARKER = .migrations-applied
DOCKER_USERNAME = tibbsdocker

start-db:
	@$(DOCKER_COMPOSE) up -d db
	@echo "Database container started."

migrate-db:
	@$(DOCKER_COMPOSE) run --rm app1 alembic upgrade head
	@touch $(MIGRATION_MARKER)
	@echo "Database migrations applied."

build-api:
	@$(DOCKER) build -t $(DOCKER_USERNAME)/$(IMAGE_NAME):$(IMAGE_TAG) .
	@echo "REST API Docker image built and tagged as $(IMAGE_NAME):$(IMAGE_TAG)."

run-api:
ifeq ($(wildcard $(MIGRATION_MARKER)),)
	@echo "Migrations not applied. Running migrations first..."
	@$(DOCKER_COMPOSE) run --rm app1 alembic upgrade head
	@touch $(MIGRATION_MARKER)
else
	@echo "Migrations already applied. Skipping Alembic upgrade."
endif
	@$(DOCKER_COMPOSE) up -d
	@echo "REST API container started."

start: start-db migrate-db run-api
	@echo "Containers up and running"

stop:
	@$(DOCKER_COMPOSE) down
	@echo "Stopped all containers."

clean:
	@$(DOCKER) system prune -f
	@rm -f $(MIGRATION_MARKER)
	@echo "Cleaned up Docker system."

lint:
	flake8 --exclude __init__.py,__pycache__ --max-line-length 100 . || true

help:
	@echo "Available targets:"
	@echo "  start-db      - Start the DB container"
	@echo "  migrate-db    - Run DB DML migrations"
	@echo "  build-api     - Build REST API Docker image"
	@echo "  run-api       - Run REST API Docker container (skips migrations if already applied)"
	@echo "  start         - Start db, migrate db and run api containers"
	@echo "  stop          - Stop all containers"
	@echo "  clean         - Clean up Docker system"
	@echo "  lint		   - Run python linting"
