# nginx-gunicorn-flask

FROM ubuntu:16.04
MAINTAINER Siddharth

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install aptitude git -y
RUN aptitute update
RUN aptitude upgrade
RUN aptitude install python3-pip python3-dev nginx gunicorn supervisor=3.3.*

git config --global credential.helper "cache --timeout=3600"
RUN git clone git@github.com:DishantK1807/incubate_ind.git
# Setup flask application

RUN mkdir -p /deploy/incubate_ind
COPY incubate /deploy/incubate_ind
#RUN apt-get install libmysqlclient-dev
#RUN apt-get install mysql-server
#RUN mysql_secure_installation

RUN pip install -r /deploy/incubate_ind/requirements.txt

# Setup nginx
RUN rm /etc/nginx/sites-enabled/default
COPY Incubate.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/Incubate.conf /etc/nginx/sites-enabled/Incubate.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Setup supervisord
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY gunicorn.conf /etc/supervisor/conf.d/gunicorn.conf

RUN supervisord -c /etc/supervisor/conf.d/Incubate.conf

# Start processes
CMD ["/usr/bin/supervisord"]