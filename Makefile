
SHELL := /bin/bash

define setup_venv
	python -m venv --clear venv \
	&& source /venv/bin/activate \
	&& pip install pip pip-tools \
	&& pip install --upgrade setuptools wheel
endef

define activate_venv
	source venv/bin/activate
endef

s.setup_venv:
	$(call setup_venv)

s.venv:
	$(call activate_venv)

s.start:
	uvicorn src.app:app --reload