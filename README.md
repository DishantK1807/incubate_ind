# incubate_ind

## Prerequisites
1) Python 3.6
2) PHPMyAdmin

## Installation
1) Open terminal in the main directory and enter the following commands
2) export FLASK_APP=Incubate
3) export FLASK_DEBUG=true
4) pip install -e .
5) flask initdb (To initialize the database the first time)
6) flask run
7) Go to the url given in the terminal to access the website


#Production
1) Open terminal in the main directory and enter the following commands
2) export FLASK_APP=Incubate
3) pip install -e .
4) flask initdb (To initialize the database the first time)
5) flask run
6) Go to the url given in the terminal to access the website

chmod 755 /home/deploy/sites/incubate_ind/gunicorn.sh
Move gunicorn.conf to /etc/init/
systemctl enable gunicorn.sh

/etc/lib/systemd/system/supervisord.service
sudo systemctl daemon-reload
sudo systemctl enable supervisord.service
sudo systemctl start supervisord.service


Steps for deployment(if server is down):
START:
sudo systemctl start supervisord.service

DEBUG:
sudo systemctl status supervisord.service