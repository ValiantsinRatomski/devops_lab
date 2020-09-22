DevOps Lab 2020 summer

This package checks the system load. Metrics are written to a file in json or txt format(selected using the 't' key).

----------------------------
	INSTRUCTION
----------------------------

1) pip install wheel
2) python setup.py bdist
3) python setup.py bdist_wheel
4) pip install .
5) snapshot -i=${interval} -t="${file_type}"

