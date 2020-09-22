#!/bin/bash

pyenv install -v 2.7.0
pyenv install -v 3.7.0

pyenv virtualenv 3.7.0 py_v37
pyenv virtualenv 2.7.0 py_v27
