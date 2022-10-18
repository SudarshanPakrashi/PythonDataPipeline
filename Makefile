install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format code
	black *.py mylib/*.py
lint:
	#flake8 or pylint
	pylint --disable=R,C *.py mylib/*.py
test:
	#test
	python -m pytest -vv --cov=mylib test_logic.py
	python -m pytest -vv test_main.py
build:
	#build container
	docker build -t deploy-fastapi .
run:
	#run
	docker run -p 0.0.0.0:8080:8086 82321c692480
deploy:
	#deploy
all: install lint test deploy
