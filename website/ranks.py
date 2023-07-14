from flask import Blueprint, render_template

ranks = Blueprint('ranks', __name__)

@ranks.route('/')
def graph_1():
    return render_template("ranks.html", text="Testing")