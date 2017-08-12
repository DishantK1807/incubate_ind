from tempfile import gettempdir
from flask import Flask
from flask_mysqldb import MySQL
from flask_session import Session
#from flask_mail import Mail

from flask_cli import FlaskCLI
import config
import os

app = Flask(__name__)

app.config.from_object('config.Production')
mysql = MySQL(app)
FlaskCLI(app)


@app.cli.command()
def initdb():
    print ("INIT",os.environ.get("MYSQL_PASSWORD"))
    """Initializes the database."""
    db = mysql.connection.cursor()
    with app.open_resource('SQL/incubate.sql', mode='r') as f:
        db.execute(f.read())
    print('Initialized the database.')

#mail = Mail(app)

# configure session to use filesystem (instead of signed cookies)
app.config['SESSION_FILE_DIR']  = gettempdir()
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE']      = 'filesystem'
Session(app)

from Incubate.views import home
from Incubate.views import login
from Incubate.views import event


if __name__ == '__main__':
    app.run()
