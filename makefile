clean:
	buildozer android clean

init:
	buildozer init

update:
	buildozer android update

debug:
	buildozer android debug deploy run

release:
	buildozer android release deploy run

run-tests:
	python -m unittest discover -s './tests' -p '*test.py'

clear-compiled-files:
	rm -r **/__pycache__
	rm -r **/**/__pycache__
	rm -r **/**/**/__pycache__
	rm **/.pyc
	rm **/**/.pyc
	rm **/**/**/.pyc

coverage:
	coverage run main.py
	coverage report -m