VENV := venv

all: setup test clean

setup: venv
	python -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

venv:
	test -d venv || python3 -m venv venv

test:
	python -m unittest

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete