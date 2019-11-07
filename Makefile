
clean:
	rm -rf build dist request_chord.egg-info

build:
	python3 setup.py sdist bdist_wheel

pypi:
	$(MAKE) clean
	$(MAKE) build
	twine upload --repository testpypi dist/*

