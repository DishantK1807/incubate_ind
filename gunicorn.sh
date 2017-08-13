#!/bin/bash

NAME="Incubate"
FLASKDIR=/home/deploy/sites/incubate_ind/Incubate
SOCKFILE=/home/ubuntu/Incubate/sock
USER=deploy
GROUP=sudo
NUM_WORKERS=3

echo "Starting $NAME"

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your gunicorn
exec gunicorn Incubate:app -b 0.0.0.0:8080 \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE
