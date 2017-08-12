import hashlib
from codecs import encode
from tempfile import gettempdir

from flask import Flask, request, render_template
from flask_mysqldb import MySQL
from flask_session import Session
from flask_mail import Message

from Incubate.helpers import *
from Incubate import app
from Incubate import mysql
# from Incubate import mail

from Incubate.views import login
from Incubate.views import event


@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    event = request.args.get('event')
    db = mysql.connection.cursor()

    if event is None:
        rows = db.execute("SELECT * FROM event")
        eventslist = db.fetchall()

        return render_template('index.html', eventslist = eventslist)

    else:
        if request.method == 'POST':
            if request.form.get('join') == 'createteam':
                return redirect(url_for('createteam', event = event))

            elif request.form.get('join') == 'jointeam':
                return redirect(url_for('jointeam', event=event))

            else:
                return render_template('failure.html', msg = 'Invalid Option')

        else:
            return render_template('event.html', event = event)