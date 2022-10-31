from Backend import db
from app import app
from flask import request, jsonify, json
from datetime import datetime
from Backend.models import Courses_Catalog, learning_journey, Skill, course_skills, learning_journey_course, learning_journey_skill, registration, job_role, job_role_skills

# Course Related Functions


@app.route("/courses", methods=['GET'])
def get_all_courses():
    catalog = Courses_Catalog.query.all()
    if len(catalog):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "courseCatalog": [course.json() for course in catalog]
                    # "courseCatalog": [dict(row) for row in catalog]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no courses."
        }
    )


@app.route("/learningJourney/createLearningJourneyCourse", methods=['POST'])
def createLearningJourneyCourse():
    data = request.get_json()

    # Initialize LearningJourney class
    newLearningJourneyCourse = learning_journey_course(
        LJ_ID=data['lj_id'],
        Staff_ID=data['staff_id'],
        Skill_ID=data['skill_id'],
        Course_ID=data['course_id'],
        Reg_ID=data['reg_id']
    )

    try:
        db.session.add(newLearningJourneyCourse)
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

# Get courses based on selected skill


@app.route("/getCoursesBySkill/<skillID>", methods=['GET'])
def get_courses_by_skill(skillID):

    courses = db.session.query(Courses_Catalog
                               ).join(course_skills
                                      ).filter(course_skills.Skill_ID == skillID
                                               ).filter(course_skills.Course_ID == Courses_Catalog.Course_ID
                                                        ).filter(Courses_Catalog.Course_Status == "Active"
                                                                 ).all()

    if len(courses):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "courseCatalog": [course.json() for course in courses]
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
    print(course)
    query = db.session.query(course_skills, Skill, Courses_Catalog
                             ).filter(Courses_Catalog.Course_ID == course_skills.Course_ID,
                                      course_skills.Skill_ID == Skill.Skill_ID,
                                      Courses_Catalog.Course_Name == course).with_entities(Skill.Skill_Name, Skill.Skill_Description)
    if query.count() > 0:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "course": course,
                    "courseSkills": [dict(row) for row in query]
                }
            }
        )

    return jsonify(
        {
            "code": 404,
            "message": "Course not found."
        }
    )


@app.route("/getCoursesWithSkills", methods=['GET'])
def getCoursesWithSkills():
    # rolesWithSkills = job_role.query.all()

    query = db.session.query(Courses_Catalog, course_skills, Skill
                             ).filter(Courses_Catalog.Course_ID == course_skills.Course_ID,
                                      course_skills.Skill_ID == Skill.Skill_ID,
                                      Skill.Status == "Active").with_entities(Courses_Catalog.Course_ID, Skill.Skill_ID, Skill.Skill_Name, Skill.Skill_Description, Skill.Skill_Type, Skill.Status)

    if query.count() > 0:
        return jsonify(
            {
                "code": 200,
                "data": [dict(row) for row in query]
            }
        )

    return jsonify(
        {
            "code": 404,
            "message": "Course not found."
        }
    )


@app.route("/getCoursesBySkillId/<skill_id>", methods=['GET'])
def getCoursesBySkill(skill_id):
    query = db.session.query(course_skills, Courses_Catalog
                             ).filter(course_skills.Skill_ID == skill_id,
                                      course_skills.Course_ID == Courses_Catalog.Course_ID,
                                      ).with_entities(Courses_Catalog.Course_ID, Courses_Catalog.Course_Name, Courses_Catalog.Course_Description, Courses_Catalog.Course_Type, Courses_Catalog.Course_Category)
    if query.count() > 0:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "courses": [dict(row) for row in query]
                }
            }
        )

    return jsonify(
        {
            "code": 404,
            "message": "Course not found."
        }
    )


@app.route("/updateCourseSkills", methods=['POST'])
def update_course_skills():

    # Convert JSON to object
    data = json.loads(request.get_json()["updateInfo"])
    skills_data = data['skillsForUpdate']
    course_id = data['courseId']

    # Remove all skills currently assigned to courseId
    existing_assigned_skills = db.session.query(course_skills
                                                ).filter(course_skills.Course_ID == course_id,
                                                         ).all()

    # If there is assigned Skills, delete all
    if len(existing_assigned_skills) > 0:
        for eachSkill in existing_assigned_skills:
            db.session.delete(eachSkill)
        db.session.commit()

    # Assign all the skills in skillsData
    if len(skills_data) > 0:

        for skill in skills_data:
            # Initialize course_skills class
            skill_id = db.session.query(Skill).filter(Skill.Skill_Name == skill,
                                                      ).with_entities(Skill.Skill_ID).one()

            new_course_skill = course_skills(
                Skill_ID=skill_id[0],
                Course_ID=course_id
            )

            try:
                db.session.add(new_course_skill)
                db.session.commit()

            except Exception as e:
                return jsonify(
                    {
                        "code": 500,
                        "message": "An error occurred while updating course" + str(e)
                    }
                ), 500

    return jsonify(
        {
            "code": 201,
            "message": 'Successfully updated courses.'
        }
    ), 201

# Roles Related Functions


@app.route("/roles", methods=['GET'])
def get_all_roles():
    roles = job_role.query.all()
    if len(roles):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "roles": [role.json() for role in roles]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no roles."
        }
    )


@app.route("/getRolesWithSkills", methods=['GET'])
def getRolesWithSkills():
    # rolesWithSkills = job_role.query.all()

    query = db.session.query(job_role, job_role_skills, Skill
                             ).filter(job_role.Job_Role_ID == job_role_skills.Job_Role_ID,
                                      job_role_skills.Skill_ID == Skill.Skill_ID).with_entities(job_role.Job_Role_ID, job_role.Job_Role_Name, job_role.Job_Role_Description, job_role.Department, job_role.Status, Skill.Skill_ID, Skill.Skill_Name)
    # query= ["test"]

    print(query)

    return jsonify(
        {
            "code": 200,
            "data": [dict(row) for row in query]
        }
    )

    # if len(rolesWithSkills):
    #     return jsonify(
    #         {
    #             "code": 200,
    #             "data": {
    #                 "roles": [role.json() for role in roles]
    #             }
    #         }
    #     )
    # return jsonify(
    #     {
    #         "code": 404,
    #         "message": "There are no roles."
    #     }
    # )


@app.route('/createRole', methods=['POST'])
def create_role():
    data = request.get_json()
    print(data)

    # to verify if Role is unique by checking role name
    if (job_role.query.filter_by(Job_Role_Name=data['name']).first()):
        return jsonify(
            {
                "code": 400,
                "message": "Role already exists. Please create another role."
            }
        ), 400

    # Initialize new job_role class
    newRole = job_role(
        Job_Role_ID=0,
        Job_Role_Name=data['name'],
        Job_Role_Description=data['description'],
        Department=data['department'],
        Status='Active',
        Created_Date=datetime.today().strftime('%Y-%m-%d')
    )

    try:
        db.session.add(newRole)
        db.session.commit()

        newRoleID_row = job_role.query.filter_by(
            Job_Role_Name=data['name']).with_entities(job_role.Job_Role_ID).one()

        if newRoleID_row == None:
            return jsonify(
                {
                    "code": 500,
                    "message": "There is no role ID associated with the role you are creating."
                }
            ), 500

        newRoleID = newRoleID_row[0]

        newSkills = data['skills']
        print(newSkills)
        for eachSkill in newSkills:
            newJobRoleSkill = job_role_skills(
                Job_Role_ID=newRoleID,
                Skill_ID=eachSkill
            )

            try:
                db.session.add(newJobRoleSkill)
                db.session.commit()

            except Exception as e:
                return jsonify(
                    {
                        "code": 500,
                        "message": "An error occurred while creating a new role with skill associated. " + str(e)
                    }
                ), 500

    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating a new role. " + str(e) + "."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "message": 'Successfully added a new role!'
        }
    ), 201


# Skills Related Functions
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

# get skills by role ID


@app.route("/skills-by-role", methods=['GET'])
def get_skills_by_role():
    roleId = request.args.get('roleId')

    skills = db.session.query(Skill
                              ).join(job_role_skills
                                     ).filter(job_role_skills.Job_Role_ID == roleId
                                              ).filter(job_role_skills.Skill_ID == Skill.Skill_ID
                                                       ).all()

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
def addNewSkill():
    # Convert JSON string into JSON object
    # data = json.loads(request.get_json())

    # Convert JSON to object
    data = json.loads(request.get_json()["skillFormData"])

    # to verify if Skill_ID is unique
    if (Skill.query.filter_by(Skill_Name=data["name"].title()).first()):
        print("Hey exist la")
        return jsonify(
            {
                "code": 400,
                "message": "Skill_ID already exists. Please pick a unique ID."
            }
        ), 400

    # Initialize Skill class
    newSkill = Skill(
        Skill_ID=0,
        Skill_Name=data['name'].title(),
        Skill_Description=data['description'],
        Skill_Type=data['type'],
        Status=data['status'],
        Created_Date=datetime.today().strftime('%Y-%m-%d'),
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
        if (Skill.query.filter_by(Skill_Name=data["name"].title()).first()):
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

# Learning Journey Related Functions


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
    # learningJournies = learning_journey.query.filter_by(Staff_ID=Staff_ID).all()

    learningJourneys = db.session.query(learning_journey, job_role
                                        ).filter(learning_journey.Job_Role_ID == job_role.Job_Role_ID,
                                                 learning_journey.Staff_ID == Staff_ID
                                                 ).with_entities(learning_journey.LJ_ID, learning_journey.Staff_ID, learning_journey.Job_Role_ID, job_role.Job_Role_Name, job_role.Job_Role_Description, job_role.Department, job_role.Created_Date)

    # query = db.session.query(course_skills, Skill, Courses_Catalog
    #     ).filter(Courses_Catalog.Course_ID == course_skills.Course_ID,
    #             course_skills.Skill_ID == Skill.Skill_ID,
    #             Courses_Catalog.Course_Name == course).with_entities(Skill.Skill_Name, Skill.Skill_Description)

    if learningJourneys.count() > 0:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "learning_journeys": [dict(row) for row in learningJourneys]
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
    data = request.get_json()

    # Initialize LearningJourney class
    newLearningJourney = learning_journey(
        LJ_ID=13,
        Staff_ID=data['staff_id'],
        Job_Role_ID=data['job_role_id']
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

# @app.route("/learningJourney/createLearningJourneySkill", methods=['POST'])
# def createLearningJourneySkill():
#     data = request.form

#     # Initialize LearningJourney class
#     newLearningJourneySkill = learning_journey_skill(
#         LJ_ID = data['lj_id'],
#         Staff_ID = data['staff_id'],
#         Skill_ID = data['skill_id']
#     )

#     try:
#         db.session.add(learning_journey_skill)
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


@app.route("/learningJourney/getLearningJourneyRole/<LJ_ID>", methods=['GET'])
def getLearningJourneyRole(LJ_ID):
    learningJourneySkills = db.session.query(learning_journey, job_role
                                             ).filter(learning_journey.LJ_ID == LJ_ID,
                                                      learning_journey.Job_Role_ID == job_role.Job_Role_ID).with_entities(job_role.Job_Role_ID, job_role.Job_Role_Name, job_role.Job_Role_Description, job_role.Department)
    if learningJourneySkills.count() > 0:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "LJ_ID": LJ_ID,
                    "Role": [dict(row) for row in learningJourneySkills]
                }
            }
        )

    return jsonify(
        {
            "code": 404,
            "message": "Skills not found."
        }
    )

# @app.route("/learningJourney/getLearningJourneySkills/<LJ_ID>", methods=['GET'])
# def getLearningJourneySkill(LJ_ID):
#     learningJourneySkills = db.session.query(learning_journey_skill, Skill
#         ).filter(learning_journey_skill.Skill_ID == Skill.Skill_ID,
#                 learning_journey_skill.LJ_ID == LJ_ID).with_entities(Skill.Skill_ID, Skill.Skill_Name, Skill.Skill_Description, Skill.Skill_Type)
#     if learningJourneySkills.count() > 0:
#         return  jsonify(
#             {
#                 "code":200,
#                 "data": {
#                     "LJ_ID" : LJ_ID,
#                     "Skills" : [dict(row) for row in learningJourneySkills]
#                 }
#             }
#         )

#     return jsonify(
#         {
#             "code": 404,
#             "message": "Skills not found."
#         }
#     )

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


@app.route("/learningJourney/createLearningJourneySkill", methods=['POST'])
def createLearningJourneySkill():
    data = request.get_json()

    # Initialize LearningJourney class
    newLearningJourneySkill = learning_journey_skill(
        LJ_ID=data['lj_id'],
        Staff_ID=data['staff_id'],
        Skill_ID=data['skill_id']
    )

    try:
        db.session.add(newLearningJourneySkill)
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


@app.route("/learningJourney/getLearningJourneySkills/<LJ_ID>", methods=['GET'])
def getLearningJourneySkill(LJ_ID):
    learningJourneySkills = db.session.query(learning_journey_skill, Skill
                                             ).filter(learning_journey_skill.Skill_ID == Skill.Skill_ID,
                                                      learning_journey_skill.LJ_ID == LJ_ID).with_entities(Skill.Skill_Name)
    if learningJourneySkills.count() > 0:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "LJ_ID": LJ_ID,
                    "Skills": [dict(row) for row in learningJourneySkills]
                }
            }
        )

    return jsonify(
        {
            "code": 404,
            "message": "Skills not found."
        }
    )