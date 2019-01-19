start:
	. env/bin/activate
	python3 manage.py runserver 8080

install:
	python3 -m virtualenv env
	. env/bin/activate
	pip3 install -r requirements.txt

clean:
	rm -rf */__pycache__ 
	rm -rf env/
