#!/bin/bash
sudo apt install python3-dev portaudio19-dev
if [ ! -d ./env ]
then
  python3 -m venv env
fi
. ./env/bin/activate
pip install -r requirements.txt
