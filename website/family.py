from flask import Blueprint, render_template

family = Blueprint('family', __name__)

@family.route('/')
def graph_2():
    return render_template("family.html", text="Testing")