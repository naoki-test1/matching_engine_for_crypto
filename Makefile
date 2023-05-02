
start-mongod:
	sh mongodb_init.sh

deps-install:
	echo "Dependencies"
	pip install -r requirements.txt

install:
	echo "Application"
	python setup.py install  --record files.txt

run-tests:
	python -m unittest discover

run-script:
	# make install
	script_runner.py < ./sample_data/largeOrder600K.txt

run-benchmarks:
	benchmark.py

run-threaded-script:
	echo "Multithreaded script, entries are dumped to database."
	threaded_script.py < ./sample_data/largeOrder600K.txt
