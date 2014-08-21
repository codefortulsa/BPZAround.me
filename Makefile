.PHONY: clean-pyc clean-build docs clean qa qa-all

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo
	@echo "develop - get setup for development"
	@echo "test - run tests quickly with the default Python"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "lint - check style with flake8"
	@echo "test-all - run tests on every Python version with tox"
	@echo "qa - run tests, lint, and coverage"
	@echo
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "dist - package without uploading"
	@echo "qa-all - run qa, plus packaging QA"
	@echo "release - package and upload a release"

clean: clean-build clean-pyc clean-test

qa: coverage lint

qa-all: qa docs dist test-all

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

lint:
	flake8 --exclude='.tox' .

test:
	./manage.py test

test-all:
	tox

coverage:
	./manage.py test --with-coverage --cover-erase --cover-tests --cover-branches --cover-html --cover-html-dir=htmlcov/
	open htmlcov/index.html

docs:
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	open docs/_build/html/index.html

release: clean qa-all
	python setup.py sdist upload
	python setup.py bdist_wheel upload

dist: clean
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist
	check-manifest
	pyroma `ls -t dist/*.tar.gz | head -n1`; if [ $$? -ne 1 ]; then exit 1; fi
