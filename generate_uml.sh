#!/usr/bin/env bash
# Make sure to install pydotplus, e.g.: `pip install pydotplus` (not in requirements because only used for development)

APPS="data_model"
python manage.py graph_models $APPS -o doc/class_diagram.png
