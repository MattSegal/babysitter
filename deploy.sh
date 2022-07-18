#!/bin/bash
git add .
git commit -m "Deploy $1"
git push
ssh -o StrictHostKeyChecking=no root@raspi /bin/bash << EOF
  cd /srv/babysitter/
  git reset --hard
  git pull
  #./setup.sh
  ./prod.sh
EOF
