VIRTUAL_ENV := venv
PYTHON_PATH := $(VIRTUAL_ENV)/bin/python

########################################################################################################################
# Init
########################################################################################################################

.PHONY: main
main:
	$(VIRTUAL_ENV)/bin/pip install -U pip setuptools

.PHONY: update
update:
	$(VIRTUAL_ENV)/bin/pip install --upgrade .

.PHONY: update-all
update-all:
	$(VIRTUAL_ENV)/bin/pip install --upgrade --force-reinstall .


########################################################################################################################
# Blackify code
########################################################################################################################

.PHONY: black
black:
	$(PYTHON_PATH) -m black `git ls-files "*.py"` --line-length=79

.PHONY: lint
lint:
	$(PYTHON_PATH) -m pylint tio

.PHONY: type
type:
	$(PYTHON_PATH) -m mypy tio

.PHONY: style
style: black lint type
