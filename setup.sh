#!/bin/bash
sudo apt install python3-dev portaudio19-dev --yes
if [ ! -d ./env ]
then
  python3 -m venv env
fi
. ./env/bin/activate
pip3 install -r requirements.txt
