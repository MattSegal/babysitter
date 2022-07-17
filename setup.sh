#!/bin/bash
sudo apt install python3-dev portaudio19-dev python3-venv pulseaudio libopenjp2-7-dev ffmpeg libgtk-3-0 libatlas-base-dev python3-pyaudio llvm --yes
if [ ! -d ./env ]
then
  python3 -m venv env
fi
. ./env/bin/activate
pip3 install -r requirements.txt
