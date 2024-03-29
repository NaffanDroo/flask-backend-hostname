.PHONY: deps pre-commit test


deps:
	@echo "=== Install dependencies ==="
	poetry install

pre-commit: deps
	@echo "=== Setting up pre-commit ==="
	poetry run pre-commit install

test: deps pre-commit
	@echo "=== Running pytest ==="
	poetry run pytest --cov=main.py --cov=blueprints --cov-report xml:.coverage.xml --cov-branch --cov-fail-under=100 .
	@echo "--- Listing files ---"
	ls -lart
