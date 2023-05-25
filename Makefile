.DEFAULT_GOAL := about
VERSION := $(shell cat text_grade/__init__.py | grep '__version__ ' | cut -d'"' -f 2)

lint:
ifeq ($(SKIP_STYLE), )
	@echo "> running isort..."
	isort text_grade
	isort tests
	@echo "> running black..."
	black text_grade
	black tests
endif
	@echo "> running flake8..."
	flake8 text_grade
	flake8 tests
	@echo "> running mypy..."
	mypy text_grade

tests:
	@echo "> running tests..."
	python -m pytest -vv --no-cov-on-fail --color=yes --cov-report xml --cov-report term --cov=text_grade tests

docs:
	@echo "> generate project documentation..."
	@cp README.md docs/index.md
	mkdocs serve -a 0.0.0.0:8000

install-deps:
	@echo "> installing dependencies..."
	pip install -r requirements-dev.txt

about:
	@echo "> text-grade: $(VERSION)"
	@echo ""
	@echo "make lint         - Runs: [isort > black > flake8 > mypy]"
	@echo "make tests        - Runs: tests."
	@echo "make ci           - Runs: [lint > tests]"
	@echo "make docs         - Generate project documentation."
	@echo "make install-deps - Install development dependencies."
	@echo ""
	@echo "mailto: alexandre.fmenezes@gmail.com"

ci: lint tests
ifeq ($(GITHUB_HEAD_REF), false)
	@echo "> uploading report..."
	codecov --file coverage.xml -t $$CODECOV_TOKEN
	./cc-test-reporter format-coverage -t coverage.py -o codeclimate.json
	./cc-test-reporter upload-coverage -i codeclimate.json -r $$CC_TEST_REPORTER_ID
endif

all: install-deps ci


.PHONY: lint tests ci docs install-deps all
