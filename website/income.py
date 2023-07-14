from flask import Blueprint, render_template

income = Blueprint('income', __name__)

@income.route('/')
def graph_4():
    return render_template("income.html", text="Testing")