#!/bin/bash
rm dev.db
./manage.py createdb < ./initialdata/createdb.txt
./manage.py migrate
./install.py

./manage.py runserver
