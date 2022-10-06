from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from invokes import invoke_http
from os import environ
import json
import db_creds
import ljps


# app = Flask(__name__, static_folder='public',
#             static_url_path='', template_folder='public')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
    'dbURL') or 'mysql+mysqlconnector://' + db_creds.username + ':' + db_creds.password + '@' + db_creds.hostname + ':3306/ljps'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

@app.route('/getRole', methods=['GET'])
def create_role():
    data = ljps.Skill.query.all()
    print(data)


@app.route('/createRole', methods=['POST'])
def create_role():
    data = request.get_json()
    print(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)