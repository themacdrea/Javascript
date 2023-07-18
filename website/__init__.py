# Import the modules
from flask import Flask

# from sqlalchemy.orm import Session

# # Create our session (link) from Python to the DB
# session = Session(engine)
# inspector = inspect(engine)
# table_names = inspector.get_table_names()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'randomgjdkrfsgr'
    
    from .about import about
    from .ranks import ranks
    from .family import family
    from .years import years
    from .income import income

    app.register_blueprint(about, url_prefix='/')
    app.register_blueprint(ranks, url_prefix='/ranks')
    app.register_blueprint(family, url_prefix='/family')
    app.register_blueprint(years, url_prefix='/years')
    app.register_blueprint(income, url_prefix='/income')

    return app


