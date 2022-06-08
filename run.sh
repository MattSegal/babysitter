#!/bin/bash
export FLASK_APP=app
export FLASK_ENV=development
. ./env/bin/activate
flask run --host=0.0.0.0
