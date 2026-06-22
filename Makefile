.PHONY: setup check heal ci clean help

setup:
	@echo "=== Setting up ==="
	@pip3 install -r requirements.txt 2>/dev/null || pip install -r requirements.txt 2>/dev/null || echo "No requirements.txt found"
	@echo "Setup complete!"

check:
	@echo "=== Compliance Check ==="
	@python scripts/enforce_check.py

heal:
	@echo "=== Compliance Check + Auto-Heal (pass@3) ==="
	@python scripts/enforce_check.py --pass-n 3 --heal

ci:
	@echo "=== CI Pipeline (pass@3 + heal) ==="
	@python scripts/enforce_check.py --pass-n 3 --heal

clean:
	@echo "=== Cleaning ==="
	@rm -rf __pycache__ */__pycache__ .pytest_cache 2>/dev/null || true
	@echo "Clean complete!"

help:
	@echo "Available commands:"
	@echo "  make setup   - Install dependencies"
	@echo "  make check   - Run compliance check"
	@echo "  make heal    - Run with pass@3 + auto-heal"
	@echo "  make ci      - Full CI pipeline"
	@echo "  make clean   - Clean cache files"
	@echo "  make help    - Show this help"
