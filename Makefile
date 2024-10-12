ifneq ("$(wildcard .env)","")
	include .env
	export
endif

.PHONY: install
install: ## Install Python requirements.
	python -m pip install --upgrade pip setuptools wheel poetry
	poetry lock
	poetry install --no-root

.PHONY: run
run: ## Run the project.
	python -m src.app

.PHONY: run-transform
run-transform: ## Run first example script.
	python src/scripts/transform.py

.PHONY: run-split
run-split: ## Run first example script.
	python src/scripts/split_base.py

.PHONY: clean
clean: ## Clean project's temporary files.
	find . -wholename '*/.ipynb_checkpoints' -exec rm -rf {} +
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.log' -exec rm -f {} +

.DEFAULT_GOAL := help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sed 's/Makefile://g' | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
