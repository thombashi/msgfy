PACKAGE := msgfy
PYTHON := python3


.PHONY: build
build: clean
	@tox -e build
	ls -lh dist/*

.PHONY: check
check:
	travis lint
	@tox -e lint

.PHONY: clean
clean:
	@tox -e clean

.PHONY: fmt
fmt:
	@tox -e fmt

.PHONY: release
release:
	@$(PYTHON) setup.py release --sign
	@make clean

.PHONY: setup
setup:
	@$(PYTHON) -m pip install -q --disable-pip-version-check --upgrade -e .[test] releasecmd tox
	@$(PYTHON) -m pip check
