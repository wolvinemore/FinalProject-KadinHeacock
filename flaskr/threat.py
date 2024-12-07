@bp.route('/threat', methods=('GET', 'POST'))
def threat():
    if request.method == 'POST':

        Field1 = request.form['Field1']
        Field2 = request.form['Field2']
        db = get_db()

        threat = db.execute(
            'INSERT INTO threat(username, author_user_id, Field1, Field2, created_at, updated_at) VALUES (username, author_user_id, Field1, Field2, created_at, updated_at)'
        ).fetchall()

        error = None

        print('It kinda worked')


        flash(error)


    return render_template('threat/threat.html')