#!/usr/bin/python3

import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dataclasses import dataclass

from datetime import datetime
import json
from os import environ

import db_creds

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
    'dbURL') or 'mysql+mysqlconnector://' + db_creds.username + ':' + db_creds.password + '@' + db_creds.hostname + ':3306/ljps'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

@dataclass
class Courses_Catalog(db.Model):
    __tablename__ = 'courses_catalog'

    Course_ID = db.Column(db.String(20), primary_key=True)
    Course_Name = db.Column(db.String(50), nullable=False)
    Course_Description = db.Column(db.String(255), nullable=False)
    Course_Status = db.Column(db.String(20), nullable=False)
    Course_Type = db.Column(db.String(20), nullable=False)
    Course_Category = db.Column(db.String(20), nullable=False)

    def __init__(self, Course_ID, Course_Name, Course_Description, Course_Status, Course_Type, Course_Category):
        self.Course_ID = Course_ID
        self.Course_Name = Course_Name
        self.Course_Description = Course_Description
        self.Course_Status = Course_Status
        self.Course_Type = Course_Type
        self.Course_Category = Course_Category

    def json(self):
        return {"Course_ID": self.Course_ID, "Course_Name": self.Course_Name, "Course_Description": self.Course_Description, "Course_Status": self.Course_Status, "Course_Type": self.Course_Type, "Course_Category" : self.Course_Category}

class Skill(db.Model):
    __tablename__ = 'skill'

    Skill_ID = db.Column(db.Integer, primary_key=True)
    Skill_Name = db.Column(db.String(50), nullable=False)
    Skill_Description = db.Column(db.String(255), nullable=False)
    Skill_Type = db.Column(db.String(20))
    Status = db.Column(db.String(20))
    Created_Date  = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


    def __init__(self, Skill_ID, Skill_Name, Skill_Description, Skill_Type, Status, Created_Date):
        self.Skill_ID = Skill_ID
        self.Skill_Name = Skill_Name
        self.Skill_Description = Skill_Description
        self.Skill_Type = Skill_Type
        self.Status = Status
        self.Created_Date = Created_Date


    def json(self):
        return {"Skill_ID": self.Skill_ID, "Skill_Name": self.Skill_Name, "Skill_Description": self.Skill_Description, "Skill_Type": self.Skill_Type, "Status": self.Status, "Created_Date": self.Created_Date}

class course_skills(db.Model):
    __tablename__ = 'course_skills'

    Skill_ID = db.Column(db.Integer, db.ForeignKey(Skill.Skill_ID), primary_key=True)
    Course_ID = db.Column(db.String(20), db.ForeignKey(Courses_Catalog.Course_ID), primary_key=True)

    def __init__(self, Skill_ID, Course_ID):
        self.Skill_ID = Skill_ID
        self.Course_ID = Course_ID

class job_role(db.Model):
    __tablename__ = 'job_role'

    Job_Role_ID = db.Column(db.Integer, primary_key=True)
    Job_Role_Name = db.Column(db.String(50), nullable=False)
    Job_Role_Description = db.Column(db.String(255), nullable=False)
    Department = db.Column(db.String(50))
    Created_Date  = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


    def __init__(self, Job_Role_ID, Job_Role_Name, Job_Role_Description, Department, Created_Date):
        self.Job_Role_ID = Job_Role_ID
        self.Job_Role_Name = Job_Role_Name
        self.Job_Role_Description = Job_Role_Description
        self.Department = Department
        self.Created_Date = Created_Date

class job_role_skills(db.Model):
    __tablename__ = 'job_role_skills'

    Job_Role_ID = db.Column(db.String(20), db.ForeignKey(job_role.Job_Role_ID), primary_key=True)
    Skill_ID = db.Column(db.Integer, db.ForeignKey(Skill.Skill_ID), primary_key=True)

    def __init__(self, Job_Role_ID, Skill_ID):
        self.Job_Role_ID = Job_Role_ID
        self.Skill_ID = Skill_ID

class system_role(db.Model):
    __tablename__ = 'system_role'

    Role_ID = db.Column(db.Integer, primary_key=True)
    Role_Name = db.Column(db.String(50))

class staff(db.Model):
    __tablename__ = 'staff'

    Staff_ID = db.Column(db.Integer, primary_key=True)
    Staff_FName = db.Column(db.String(50))
    Staff_LName = db.Column(db.String(50)) 
    Dept = db.Column(db.String(50)) 
    Email = db.Column(db.String(50)) 
    System_Role = db.Column(db.Integer, db.ForeignKey(system_role.Role_ID))

class registration(db.Model):
    __tablename__ = 'registration'

    Reg_ID = db.Column(db.Integer, primary_key=True)
    Course_ID = db.Column(db.String(20), db.ForeignKey(Courses_Catalog.Course_ID))
    Staff_ID = db.Column(db.Integer, db.ForeignKey(staff.Staff_ID))
    Reg_Status = db.Column(db.String(20))
    Completion_Status = db.Column(db.String(20))

class learning_journey(db.Model):
    __tablename__ = 'learning_journey'

    LJ_ID = db.Column(db.Integer, primary_key=True)
    Staff_ID = db.Column(db.Integer, db.ForeignKey(staff.Staff_ID), primary_key=True)
    Job_Role_ID = db.Column(db.Integer, db.ForeignKey(job_role.Job_Role_ID))

    def __init__(self, LJ_ID, Staff_ID, Job_Role_ID):
        self.LJ_ID = LJ_ID
        self.Staff_ID = Staff_ID
        self.Job_Role_ID = Job_Role_ID

    def json(self):
        return {"LJ_ID": self.LJ_ID, "Staff_ID": self.Staff_ID, "Job_Role_ID": self.Job_Role_ID}

class learning_journey_skill(db.Model):
    __tablename__ = 'learning_journey_skill'

    LJ_ID = db.Column(db.Integer, db.ForeignKey(learning_journey.LJ_ID), primary_key=True)
    Staff_ID = db.Column(db.Integer, db.ForeignKey(learning_journey.Staff_ID), primary_key=True)
    Skill_ID = db.Column(db.Integer, db.ForeignKey(Skill.Skill_ID), primary_key=True)

    def __init__(self, LJ_ID, Staff_ID, Skill_ID):
        self.LJ_ID = LJ_ID
        self.Staff_ID = Staff_ID
        self.Skill_ID = Skill_ID

    def json(self):
        return {"LJ_ID": self.LJ_ID, "Staff_ID": self.Staff_ID, "Skill_ID": self.Skill_ID}

class learning_journey_course(db.Model):
    __tablename__ = 'learning_journey_course'

    LJ_ID = db.Column(db.Integer, db.ForeignKey(learning_journey_skill.LJ_ID), primary_key=True)
    Staff_ID = db.Column(db.Integer, db.ForeignKey(learning_journey_skill.Staff_ID), primary_key=True)
    Skill_ID = db.Column(db.Integer, db.ForeignKey(learning_journey_skill.Skill_ID), primary_key=True)
    Course_ID = db.Column(db.String(20), db.ForeignKey(Courses_Catalog.Course_ID))
    Reg_ID = db.Column(db.Integer, db.ForeignKey(registration.Reg_ID))

    def __init__(self, LJ_ID, Staff_ID, Skill_ID, Course_ID, Reg_ID):
        self.LJ_ID = LJ_ID
        self.Staff_ID = Staff_ID
        self.Skill_ID = Skill_ID
        self.Course_ID = Course_ID
        self.Reg_ID = Reg_ID

    def json(self):
        return {"LJ_ID": self.LJ_ID, "Staff_ID": self.Staff_ID, "Skill_ID": self.Skill_ID, "Course_ID": self.Course_ID, "Reg_ID": self.Reg_ID}

## Course Related Functions
@app.route("/courses", methods=['GET'])
def get_all_courses():
    catalog = Courses_Catalog.query.all()
    if len(catalog):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "courseCatalog": [course.json() for course in catalog]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no courses."
        }
    )

@app.route("/getCourseSkills/<course>", methods=['GET'])
def get_farming(course):
    query = db.session.query(course_skills, Skill, Courses_Catalog
        ).filter(Courses_Catalog.Course_ID == course_skills.Course_ID,
                course_skills.Skill_ID == Skill.Skill_ID,
                Courses_Catalog.Course_Name == course).with_entities(Skill.Skill_Name, Skill.Skill_Description)
    if query.count() > 0:
        return  jsonify(
            {
                "code":200,
                "data": {
                    "course" : course,
                    "courseSkills" : [dict(row) for row in query]
                }
            }
        )
    
    return jsonify(
        {
            "code": 404,
            "message": "Course not found."
        }
    )

@app.route("/getCoursesBySkill/<skill_id>", methods=['GET'])
def getCoursesBySkill(skill_id):
    query = db.session.query(course_skills, Courses_Catalog
        ).filter(course_skills.Skill_ID == skill_id,
                course_skills.Course_ID == Courses_Catalog.Course_ID,
                ).with_entities(Courses_Catalog.Course_ID, Courses_Catalog.Course_Name, Courses_Catalog.Course_Description, Courses_Catalog.Course_Type, Courses_Catalog.Course_Category)
    if query.count() > 0:
        return  jsonify(
            {
                "code":200,
                "data": {
                    "courses" : [dict(row) for row in query]
                }
            }
        )
    
    return jsonify(
        {
            "code": 404,
            "message": "Course not found."
        }
    )

## Skills Related Functions
@app.route("/skills", methods=['GET'])
def get_all_skills():
    skills = Skill.query.all()
    if len(skills):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "skills": [skill.json() for skill in skills]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no skills."
        }
    )

@app.route("/skills/addNewSkill", methods=['POST'])
def addnNewSkill():
    # Convert JSON string into JSON object
    # data = json.loads(request.get_json())

    # Convert JSON to object
    data = json.loads(request.get_json()["skillFormData"])

    # to verify if Skill_ID is unique
    if (Skill.query.filter_by(Skill_Name = data["name"].title()).first()):
        print("Hey exist la")
        return jsonify(
            {
                "code": 400,
                "message": "Skill_ID already exists. Please pick a unique ID."
            }
        ), 400 
    
    # Initialize Menu class
    newSkill = Skill(
        Skill_ID = 0,
        Skill_Name = data['name'].title(),
        Skill_Description = data['description'],
        Skill_Type = data['type'],
        Status = data['status'],
        Created_Date = datetime.today().strftime('%Y-%m-%d'),
    )
    
    try:
        db.session.add(newSkill)
        db.session.commit()
        
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating a new skill. " + str(e)
            }
        ), 500
    
    return jsonify(
        {
            "code": 201,
            "message": 'Successfully added a new skill!'
        }
    ), 201

## Learning Journey Related Functions
@app.route("/learningJourney/viewLearningJourney/<LJ_ID>", methods=['GET'])
def viewLearningJourney(LJ_ID):
    learningJourney = learning_journey.query.filter_by(LJ_ID=LJ_ID).first()

    if learningJourney:
        return jsonify(
            {
                "code": 200,
                "data": learningJourney.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "LJ_ID": LJ_ID
            },
            "message": "Learning Journey not found."
        }
    ), 404

@app.route("/learningJourney/viewStaffLearningJourneys/<Staff_ID>", methods=['GET'])
def viewStaffLearningJourneys(Staff_ID):

    learningJourneys = db.session.query(learning_journey, job_role
        ).filter(learning_journey.Job_Role_ID == job_role.Job_Role_ID,
                learning_journey.Staff_ID == Staff_ID
                ).with_entities(learning_journey.LJ_ID, learning_journey.Staff_ID, learning_journey.Job_Role_ID, job_role.Job_Role_Name, job_role.Job_Role_Description, job_role.Department, job_role.Created_Date)

    if learningJourneys.count() > 0:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "learning_journeys" : [dict(row) for row in learningJourneys]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "Staff_ID": Staff_ID
            },
            "message": "No Learning Journey found for specified user."
        }
    ), 404

@app.route("/learningJourney/createLearningJourney", methods=['POST'])
def createLearningJourney():
    data = request.form

    # Initialize LearningJourney class
    newLearningJourney = learning_journey(
        LJ_ID = 0,
        Staff_ID = data['staff_id'],
        Job_Role_ID = data['job_role_id']
    )
    
    try:
        db.session.add(newLearningJourney)
        db.session.commit()
        
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating a new learning journey. " + str(e)
            }
        ), 500
    
    return jsonify(
        {
            "code": 201,
            "message": 'Successfully added a new learning journey!'
        }
    ), 201

@app.route("/learningJourney/createLearningJourneySkill", methods=['POST'])
def createLearningJourneySkill():
    data = request.form

    # Initialize LearningJourney class
    newLearningJourneySkill = learning_journey_skill(
        LJ_ID = data['lj_id'],
        Staff_ID = data['staff_id'],
        Skill_ID = data['skill_id']
    )
    
    try:
        db.session.add(learning_journey_skill)
        db.session.commit()
        
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating a new learning journey. " + str(e)
            }
        ), 500
    
    return jsonify(
        {
            "code": 201,
            "message": 'Successfully added a new learning journey!'
        }
    ), 201

@app.route("/learningJourney/getLearningJourneyRole/<LJ_ID>", methods=['GET'])
def getLearningJourneyRole(LJ_ID):
    learningJourneySkills = db.session.query(learning_journey, job_role
        ).filter(learning_journey.LJ_ID == LJ_ID,
                learning_journey.Job_Role_ID == job_role.Job_Role_ID).with_entities(job_role.Job_Role_ID, job_role.Job_Role_Name,job_role.Job_Role_Description, job_role.Department)
    if learningJourneySkills.count() > 0:
        return  jsonify(
            {
                "code":200,
                "data": {
                    "LJ_ID" : LJ_ID,
                    "Role" : [dict(row) for row in learningJourneySkills]
                }
            }
        )
    
    return jsonify(
        {
            "code": 404,
            "message": "Skills not found."
        }
    )

@app.route("/learningJourney/getLearningJourneySkills/<LJ_ID>", methods=['GET'])
def getLearningJourneySkill(LJ_ID):
    learningJourneySkills = db.session.query(learning_journey_skill, Skill
        ).filter(learning_journey_skill.Skill_ID == Skill.Skill_ID,
                learning_journey_skill.LJ_ID == LJ_ID).with_entities(Skill.Skill_ID, Skill.Skill_Name, Skill.Skill_Description, Skill.Skill_Type)
    if learningJourneySkills.count() > 0:
        return  jsonify(
            {
                "code":200,
                "data": {
                    "LJ_ID" : LJ_ID,
                    "Skills" : [dict(row) for row in learningJourneySkills]
                }
            }
        )
    
    return jsonify(
        {
            "code": 404,
            "message": "Skills not found."
        }
    )

# @app.route("/skills/addNewSkill", methods=['POST'])
# def addnNewSkill():
#     # Convert JSON string into JSON object
#     # data = json.loads(request.get_json())

#     # Convert JSON to object
#     data = json.loads(request.get_json()["skillFormData"])

#     # Initialize LearningJourney class
#     newLearningJourneyCourse = learning_journey_course(
#         LJ_ID = data['lj_id'],
#         Staff_ID = data['staff_id'],
#         Skill_ID = data['skill_id'],
#         Course_ID = data['course_id'],
#         Reg_ID = data['reg_id']
#     )
    
#     try:
#         db.session.add(learning_journey_course)
#         db.session.commit()
        
#     except Exception as e:
#         return jsonify(
#             {
#                 "code": 500,
#                 "message": "An error occurred while creating a new learning journey. " + str(e)
#             }
#         ), 500
    
#     return jsonify(
#         {
#             "code": 201,
#             "message": 'Successfully added a new learning journey!'
#         }
#     ), 201

@app.route("/skills/updateSkill", methods=['POST'])
def updateSkill():
    # Convert JSON string into JSON object
    # data = json.loads(request.get_json())

    # Convert JSON to object
    data = json.loads(request.get_json()["skillFormData"])
    print(data)

    # Get existing data
    dbSkillData = Skill.query.get(data["id"])

    # If different skill name, check if skill name exists
    if data['name'] != dbSkillData.Skill_Name:
        # to verify if Skill_ID is unique
        if (Skill.query.filter_by(Skill_Name = data["name"].title()).first()):
            return jsonify(
                {
                    "code": 400,
                    "message": "This name already exists, please try another one."
                }
            ), 400 

    # Check if the rest is the same, if same return message
    if data['type'] == dbSkillData.Skill_Type and data['description'] == dbSkillData.Skill_Description and data['status'] == dbSkillData.Status:
        return jsonify(
            {
                "code": 400,
                "message": "No changes has been made."
            }
        ), 400 
    
    # Do the update
    if data['type'] != dbSkillData.Skill_Type:
        dbSkillData.Skill_Type = data['type']
    
    if data['description'] != dbSkillData.Skill_Description:
        dbSkillData.Skill_Description = data['description']

    if data['status'] != dbSkillData.Status:
        dbSkillData.Status = data['status']
    
    try:
        db.session.commit()

    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while updating skill. " + str(e)
            }
        ), 500
    
    return jsonify(
        {
            "code": 201,
            "message": 'Updated successfully'
        }
    ), 201    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
