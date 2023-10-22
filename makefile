help:
	@echo "Available targets:"
	@echo "  run - Run the FastAPI app using Uvicorn"
	@echo "  test - Run unit tests using pytest"
	@echo "  clean - Remove generated files"
	@echo "  pre-commit - Add all files to staging and run pre-commit"
	@echo "  git-commit - Commit changes to git with message"

run:
	uvicorn src.main:app --reload

pre-commit:
	git add .
	pre-commit run -a

test:
	pytest tests/

clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	rm -rf .coverage htmlcov

git-commit:
	@if [ -z "$(message)" ]; then \
		echo "Please provide a commit message: make git-commit message='your message'"; \
	else \
		git add .; \
		git commit -m "$(message)"; \
	fi

.PHONY: help run pre-commit test clean git-commit
