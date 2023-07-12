# Import the modules
from flask import Flask, jsonify
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import Session

# Setup Database 
engine = create_engine(f"postgresql://postgres:postgres@pgAdmin:5432/Divorce_Schema")

# Create our session (link) from Python to the DB
session = Session(engine)

# Setup Flask 
app = Flask(__name__)

@app.route('/')
def home_page():
    return ('Home Page Why Divorce!')

if __name__ == '__main__':
    app.run(debug=False)
