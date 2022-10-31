from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import db_creds
from flask_cors import CORS

db = SQLAlchemy()
# def create_app():

app = Flask(__name__)
CORS(app)
# Database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://' + db_creds.username + ':' + db_creds.password + '@' + db_creds.hostname + ':3306/ljps'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}
db.init_app(app)

def create_test_app():
    app.config['TESTING'] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
    # Dynamically bind SQLAlchemy to application
    db.init_app(app)
    app.app_context().push() # this does the binding
    return app


from Backend import routes
from Backend import models


# return app
