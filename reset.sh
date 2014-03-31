#!/bin/bash
rm dev.db
./manage.py createdb < createdb.txt
./manage.py migrate
./install.py

./manage.py runserver
