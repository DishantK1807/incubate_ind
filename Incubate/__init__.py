from tempfile import gettempdir

from flask import Flask
from flask_mysqldb import MySQL
from flask_session import Session
from flask_mail import Mail

app = Flask(__name__)

mysql = MySQL(app)

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    db = mysql.connection.cursor()
    with app.open_resource('SQL/incubate.sql', mode='r') as f:
        db.execute(f.read())
    print('Initialized the database.')

MAIL_SERVER = '127.0.0.1'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None
DEFAULT_MAIL_SENDER = 'Incubate IND'
mail = Mail(app)

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
