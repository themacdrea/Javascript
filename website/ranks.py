from flask import Blueprint, render_template, jsonify
from pathlib import Path
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from config import username, password, host, port, database_name

engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{database_name}")

ranks = Blueprint('ranks', __name__)

@ranks.route('/')
def graph_1():
    session = Session(engine)

    result1 = session.execute('SELECT "Zodiac_Sign" FROM Male')
    # result2 = session.execute('SELECT "Zodiac_Sign" FROM Female')
    print(result1)

    return render_template("ranks.html", text=result1)