from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from ljps import *
from invokes import invoke_http
from os import environ
import json
import db_creds
# import ljps


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
def get_role():
    try:
        data = job_role.query.all() 
        print(len(data))
        return jsonify(
            {
                "code": 200,
                "data": {
                    "allRoles": [item.json() for item in data]
                }
            }
        )
    except Exception as e:
        return jsonify(
            {
                "code": 404,
                "message": "Error in retrieving data. Please contact support."
            }
        )
    # data = job_role.query.all() 
    # print(len(data))
    # return jsonify(
    #     {
    #         "code": 200,
    #         "data": {
    #             "allRoles": [item.json() for item in data]
    #         }
    #     }
    # )

@app.route('/getRoleWithSkills', methods=['GET'])
def get_role_with_skills():
    try:
        data = db.session.query(job_role, Skill, job_role_skills).filter(job_role.Job_Role_ID == job_role_skills.Job_Role_ID, job_role_skills.Skill_ID == Skill.Skill_ID).with_entities(job_role.Job_Role_ID, job_role.Job_Role_Name, job_role.Job_Role_Description, Skill.Skill_Name, Skill.Skill_Description)
        print(data)
        return jsonify(
            {
                "code": 200,
                "data": {
                    "allRolesWithSkills": [dict(item) for item in data]
                }
            }
        )
    except Exception as e:
        return jsonify(
            {
                "code": 404,
                "message": "Error in retrieving data."
            }
        )
    # data = job_role.query(job_role.Job_Role_ID, job_role.Job_Role_Name, job_role.Job_Role_Description, Skill.Skill_ID, Skill.Skill_Name).join(job_role_skills, job_role.Job_Role_ID == job_role_skills.Job_Role_ID).join(Skill, job_role_skills.Skill_ID == Skill.Skill_ID)
    # print(data)

    # all_roles = [dict(item.json()) for item in job_role.query.all()]
    # for each_role in all_roles:
    #     each_role["skills"] = []
    #     role_skill = [item for item in job_role_skills.query.filter(job_role_skills.Job_Role_ID == each_role['Role_ID']).with_entities(job_role_skills.Skill_ID).all()]
    #     print(role_skill)
    # print(all_roles)
    # return "non"


@app.route('/createRole', methods=['POST'])
def create_role():
    data = request.get_json()
    print(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)