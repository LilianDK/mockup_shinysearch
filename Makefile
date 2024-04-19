install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		pip install --upgrade "ibm-watson>=7.0.0"

test:
	#python -m pytest -vv test_hello.py
	
download:
	python -m textblob.download_corpora

format:
	black *.py

lint:
	#pylint --disable=R,C hello.py

all: install lint test