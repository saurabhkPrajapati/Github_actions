PYTHON ?= python
TEST_DIR ?= tests
TEST_PATTERN ?= test_*.py

.PHONY: test coverage

test:
	$(PYTHON) -m unittest discover -s $(TEST_DIR) -p "$(TEST_PATTERN)" -v

coverage:
	coverage run -m unittest discover -s $(TEST_DIR) -p "$(TEST_PATTERN)" -v
	coverage report -m
	coverage html
