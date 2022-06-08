#!/bin/bash
ssh -o StrictHostKeyChecking=no root@raspi /bin/bash << EOF
  cd /srv/babysitter/
  git reset --hard
  git pull
  #./setup.sh
  ./prod.sh
EOF
