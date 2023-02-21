from flask_app.config.mysqlconnection import connectToMySQL
from flask import render_template, request, redirect
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

from flask_app import app
@app.route('/dojos/<int:dojo_id>/ninjas', methods=['GET', 'POST'])
def ninjas(dojo_id):
    dojo = Dojo.get_one(dojo_id)
    if request.method == 'POST':
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'age': request.form['age'],
            'dojo': dojo
        }
        ninja = Ninja(**data)
        ninja.save()
        return redirect(f'/dojos/{dojo_id}')


    dojos = Dojo.get_all()
    return render_template('ninja.html', dojo=dojo, dojos=dojos)
