#!/bin/bash
export FLASK_APP=app
export FLASK_ENV=production
. ./env/bin/activate
pkill -9 flask
nohup flask run --host=0.0.0.0 &
