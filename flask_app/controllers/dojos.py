from flask import render_template, request, redirect
from flask_app.models.dojo import Dojo
from flask_app import app

@app.route('/dojos', methods=['GET', 'POST'])
def create_and_display_dojos():
    dojos = Dojo.get_all()
    if request.method == 'POST':
        data = {
            'name': request.form['name']
        }
        Dojo.save(data)
        return redirect('/dojos')
    else:
        return render_template('dojo.html', dojos=dojos)

@app.route('/dojos/<int:dojo_id>')
def dojo_show(dojo_id):
    dojo = Dojo.get_one(dojo_id)
    ninjas = dojo.get_ninjas()
    return render_template('dojo_show.html', dojo=dojo, ninjas=ninjas)
