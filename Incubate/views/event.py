from Incubate.views.home import *

@app.route('/event', methods=['GET', 'POST'])
@login_required
def event():
    event = session['event']
    del session['event']

    if request.method == 'POST':
        pass
    else:
        db = mysql.connection.cursor()
        rows = db.execute("SELECT * FROM users WHERE id = '{}'".format(session['user_id']))
        rv = db.fetchone()

        render_template('event.html', event = event)


@app.route('/createteam', methods=['GET', 'POST'])
def createteam():
    if request.method == 'POST':
        event = request.args.get('event')

        table = event + 'team'

        db = mysql.connection.cursor()
        db.execute("SELECT email FROM users WHERE id = '{}'".format(session['user_id']))
        email = db.fetchone()

        db.execute(
            "INSERT IGNORE INTO " + table +" (team_name, user1, user2, user3, user4, user5) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(
            request.form.get("team_name"), email, request.form.get("user2"), request.form.get("user3"), request.form.get("user4"), request.form.get("user5")))
        mysql.connection.commit()

        return redirect(url_for('questions', event = event))

    else:
        event = request.args.get('event')
        return render_template('createteam.html', event = event)

@app.route('/jointeam', methods=['GET', 'POST'])
def jointeam():
    event = str(request.args.get('event'))
    table = event + 'team'
    db = mysql.connection.cursor()

    if request.method == 'POST':

            rows = db.execute("SELECT * FROM " + table + " WHERE team_name = '{}'".format(request.form.get("team")))
            if rows is 0:
                return render_template('failure.html', msg = "Team not found")
            team = db.fetchone()
            if team['user2'] == '':
                user = 'user2'
            elif team['user3'] == '':
                user = 'user3'
            elif team['user4'] == '':
                user = 'user4'
            elif team['user5'] == '':
                user = 'user5'
            else:
                return render_template('failure.html', msg='Sorry, this team is already filled')

            db.execute("UPDATE " + table + " SET " + user + " = '{0}' WHERE team_name = '{1}'".format(request.form.get("email"), team['team_name']))
            mysql.connection.commit()
            return redirect(url_for('questions', event = event))


    else:
        db.execute("SELECT team_name, user5 FROM " + table)
        rows = db.fetchall()
        teams = list()
        for row in rows:
            temp = dict()
            temp['team_name'] = row['team_name']
            if row['user5'] == '':
                temp['availability'] = True
            else:
                temp['availability'] = False
            teams.append(temp)

        return render_template('jointeam.html', teams = teams, event = event)



@app.route('/questions', methods=['GET', 'POST'])
def questions():
    return render_template('failure.html')