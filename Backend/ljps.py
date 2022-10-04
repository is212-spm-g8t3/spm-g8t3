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


    def __init__(self, Skill_ID, Skill_Name, Skill_Description):
        self.Skill_ID = Skill_ID
        self.Skill_Name = Skill_Name
        self.Skill_Description = Skill_Description

    def json(self):
        return {"Skill_ID": self.Skill_ID, "Skill_Name": self.Skill_Name, "Skill_Description": self.Skill_Description}

class course_skills(db.Model):
    __tablename__ = 'course_skills'

    Skill_ID = db.Column(db.Integer, db.ForeignKey(Skill.Skill_ID), primary_key=True)
    Course_ID = db.Column(db.String(20), db.ForeignKey(Courses_Catalog.Course_ID),primary_key=True)


@app.route("/courses", methods=['GET'])
def get_all():
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

@app.route("/getSkills/<course>", methods=['GET'])
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
