init:
	pip install -r requirements.txt

fmt:
	yapf -r -i *

test:
	python setup.py test
