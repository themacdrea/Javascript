from flask import Blueprint, render_template

years = Blueprint('years', __name__)

@years.route('/')
def graph_3():
    return render_template("years.html", text="Testing")