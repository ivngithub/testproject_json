import json

from flask import render_template, request, redirect, url_for, flash

from app import app
from .models import db, Json
from .forms import MainForm


@app.route('/', methods=['GET', 'POST'])
def index():

    form = MainForm()
    if request.method == 'POST' and form.validate_on_submit():
        data = json.loads(form.json.data)

        for item in data:
            s = Json(sensor_type=item.get("Sensor_type"),
                     num=item.get("num"),
                     name=item.get("name"),
                     temperature=item.get("temperature"),
                     humidity=item.get("humidity")
                     )

            db.session.add(s)
            db.session.commit()

        flash("saved to the database", 'success')
        return redirect(url_for('index'))

    with open(app.config['JSON_FILE_PATH'], 'r') as file:
        form.json.data = file.read()

    return render_template('index.html', form=form)


@app.route('/json-list/')
def json_list():

    jsons = db.session.query(Json).all()

    return render_template('json_list.html', jsons=jsons)


@app.route('/order/')
def order():

    orders = request.cookies.get("orders").split(',') if request.cookies.get("orders") else []
    items = []
    for order in orders[:-1]:
        items.append(db.session.query(Json).filter(Json.id==int(order)).first())

    return render_template('order.html', orders=items)


@app.errorhandler(404)
def http_404_handler(error):
    return "<p>HTTP 404 Error Encountered</p>", 404


@app.errorhandler(500)
def http_500_handler(error):
    return "<p>HTTP 500 Error Encountered</p>", 500
