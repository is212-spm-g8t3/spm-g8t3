import unittest
import flask_testing
from flask import json
from Backend import app, db
# from app import app
from Backend.models import Courses_Catalog, Skill, course_skills, learning_journey, learning_journey_course, learning_journey_skill, registration, job_role, job_role_skills, system_role, staff
from datetime import date, datetime
from Backend import db_creds


class TestApp(flask_testing.TestCase):

    # Setting a in-memory temporary database
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TESTING'] = True

    def create_app(self):
        return app

    # Run below each test function (method)
    def setUp(self):
        db.create_all()

    # Destroy after each test function (method)
    def tearDown(self):
        db.session.remove()
        db.drop_all()


''' Test Cases for Courses '''


class TestCourse(TestApp):
    def test_get_all_courses(self):

        # Uncomment below to see the full response of query
        # self.maxDiff = None

        course1 = Courses_Catalog(
            Course_ID="COR001",
            Course_Name="Systems Thinking and Design",
            Course_Description="This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking",
            Course_Status="Active",
            Course_Type="Internal",
            Course_Category="Core")

        course2 = Courses_Catalog(
            Course_ID='COR002',
            Course_Name='Lean Six Sigma Green Belt Certification',
            Course_Description='Apply Lean Six Sigma methodology and statistical tools such as Minitab to be used in process analytics',
            Course_Status='Active',
            Course_Type='Internal',
            Course_Category='Core')

        db.session.add(course1)
        db.session.add(course2)
        db.session.commit()

        response = self.client.get("/courses",
                                   content_type='application/json')

        self.assertEqual(response.json, {
            'code': 200,
            'data': {
                'courseCatalog': [
                    {
                        'Course_ID': 'COR001',
                        'Course_Name': 'Systems Thinking and Design',
                        'Course_Description': 'This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking',
                        'Course_Status': 'Active',
                        'Course_Type': 'Internal',
                        'Course_Category': 'Core'
                    },

                    {
                        'Course_ID': 'COR002',
                        'Course_Name': 'Lean Six Sigma Green Belt Certification',
                        'Course_Description': 'Apply Lean Six Sigma methodology and statistical tools such as Minitab to be used in process analytics',
                        'Course_Status': 'Active',
                        'Course_Type': 'Internal',
                        'Course_Category': 'Core'
                    }
                ]
            }
        })

    def test_get_courses_by_skill(self):

        # Uncomment below to see the full response of query
        # self.maxDiff = None

        course1 = Courses_Catalog(
            Course_ID="COR001",
            Course_Name="Systems Thinking and Design",
            Course_Description="This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking",
            Course_Status="Active",
            Course_Type="Internal",
            Course_Category="Core")

        course2 = Courses_Catalog(
            Course_ID='COR002',
            Course_Name='Lean Six Sigma Green Belt Certification',
            Course_Description='Apply Lean Six Sigma methodology and statistical tools such as Minitab to be used in process analytics',
            Course_Status='Active',
            Course_Type='Internal',
            Course_Category='Core')

        course3 = Courses_Catalog(
            Course_ID='SAL003',
            Course_Name='Optimising Your Brand For The Digital Spaces',
            Course_Description='Digital has fundamentally shifted communication between brands and their consumers from a one-way broadcast to a two-way dialogue. In a hastened bid to transform their businesses to be digital market-ready,',
            Course_Status='Active',
            Course_Type='External',
            Course_Category='Sales')

        skill1 = Skill(
            Skill_ID='1',
            Skill_Name='Sales',
            Skill_Description='Sell',
            Skill_Type='Active',
            Status='Active',
            Created_Date=datetime(2012, 3, 3, 10, 10, 10)
        )

        course_skill1 = course_skills(
            Course_ID='COR001',
            Skill_ID='1'
        )
        course_skill2 = course_skills(
            Course_ID='COR002',
            Skill_ID='1'
        )
        course_skill3 = course_skills(
            Course_ID='SAL003',
            Skill_ID='1'
        )

        db.session.add(course1)
        db.session.add(course2)
        db.session.add(course3)
        db.session.add(skill1)
        db.session.add(course_skill1)
        db.session.add(course_skill2)
        db.session.add(course_skill3)
        db.session.commit()

        response = self.client.get("/getCoursesBySkill/1",
                                   content_type='application/json')

        self.assertEqual(response.json, {
            'code': 200,
            'data': {
                'courseCatalog': [
                    {
                        'Course_ID': 'COR001',
                        'Course_Name': 'Systems Thinking and Design',
                        'Course_Description': 'This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking',
                        'Course_Status': 'Active',
                        'Course_Type': 'Internal',
                        'Course_Category': 'Core'
                    },
                    {
                        'Course_ID': 'COR002',
                        'Course_Name': 'Lean Six Sigma Green Belt Certification',
                        'Course_Description': 'Apply Lean Six Sigma methodology and statistical tools such as Minitab to be used in process analytics',
                        'Course_Status': 'Active',
                        'Course_Type': 'Internal',
                        'Course_Category': 'Core'
                    },
                    {
                        'Course_ID': 'SAL003',
                        'Course_Name': 'Optimising Your Brand For The Digital Spaces',
                        'Course_Description': 'Digital has fundamentally shifted communication between brands and their consumers from a one-way broadcast to a two-way dialogue. In a hastened bid to transform their businesses to be digital market-ready,',
                        'Course_Status': 'Active',
                        'Course_Type': 'External',
                        'Course_Category': 'Sales'
                    }
                ]
            }
        })

    """"Done By Aloysius"""

    def test_get_course_skills_by_course_name(self):

        # Uncomment below to see the full response of query
        # self.maxDiff = None

        course1 = Courses_Catalog(
            Course_ID="COR001",
            Course_Name="Systems Thinking and Design",
            Course_Description="This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking",
            Course_Status="Active",
            Course_Type="Internal",
            Course_Category="Core")

        skill1 = Skill(
            Skill_ID='1',
            Skill_Name='Sales',
            Skill_Description='Sell',
            Skill_Type='Active',
            Status='Active',
            Created_Date=datetime(2012, 3, 3, 10, 10, 10)
        )

        skill2 = Skill(
            Skill_ID='2',
            Skill_Name='HR',
            Skill_Description='Human Resources',
            Skill_Type='Active',
            Status='Active',
            Created_Date=datetime(2012, 3, 3, 10, 10, 10)
        )

        skill3 = Skill(
            Skill_ID='3',
            Skill_Name='Hacking',
            Skill_Description='Hacking',
            Skill_Type='Active',
            Status='Active',
            Created_Date=datetime(2012, 3, 3, 10, 10, 10)
        )

        course_skill1 = course_skills(
            Course_ID='COR001',
            Skill_ID='1'
        )

        course_skill2 = course_skills(
            Course_ID='COR001',
            Skill_ID='2'
        )

        course_skill3 = course_skills(
            Course_ID='COR001',
            Skill_ID='3'
        )

        db.session.add(course1)
        db.session.add(skill1)
        db.session.add(skill2)
        db.session.add(skill3)
        db.session.add(course_skill1)
        db.session.add(course_skill2)
        db.session.add(course_skill3)
        db.session.commit()

        response = self.client.get("/getCourseSkills/Systems Thinking and Design",
                                   content_type='application/json')

        self.assertEqual(response.json, {
            'code': 200,
            'data': {
                'course': 'Systems Thinking and Design',
                'courseSkills': [
                    {
                        "Skill_Description": "Sell",
                        "Skill_Name": "Sales"
                    },
                    {
                        "Skill_Description": "Human Resources",
                        "Skill_Name": "HR"
                    },
                    {
                        "Skill_Description": "Hacking",
                        "Skill_Name": "Hacking"
                    }
                ]
            }
        })

    """"Done By Aloysius"""

    def test_get_courses_with_skills(self):

        # Uncomment below to see the full response of query
        # self.maxDiff = None

        course1 = Courses_Catalog(
            Course_ID="COR001",
            Course_Name="Systems Thinking and Design",
            Course_Description="This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking",
            Course_Status="Active",
            Course_Type="Internal",
            Course_Category="Core")

        course2 = Courses_Catalog(
            Course_ID='COR002',
            Course_Name='Lean Six Sigma Green Belt Certification',
            Course_Description='Apply Lean Six Sigma methodology and statistical tools such as Minitab to be used in process analytics',
            Course_Status='Active',
            Course_Type='Internal',
            Course_Category='Core')

        skill1 = Skill(
            Skill_ID='1',
            Skill_Name='Sales',
            Skill_Description='Sell',
            Skill_Type='Active',
            Status='Active',
            Created_Date=datetime(2012, 3, 3, 10, 10, 10)
        )

        skill2 = Skill(
            Skill_ID='2',
            Skill_Name='HR',
            Skill_Description='Human Resources',
            Skill_Type='Active',
            Status='Active',
            Created_Date=datetime(2012, 3, 3, 10, 10, 10)
        )

        course_skill1 = course_skills(
            Course_ID='COR001',
            Skill_ID='1'
        )

        course_skill2 = course_skills(
            Course_ID='COR002',
            Skill_ID='2'
        )

        db.session.add(course1)
        db.session.add(course2)
        db.session.add(skill1)
        db.session.add(skill2)
        db.session.add(course_skill1)
        db.session.add(course_skill2)
        db.session.commit()

        response = self.client.get("/getCoursesWithSkills",
                                   content_type='application/json')

        self.assertEqual(response.json, {
            'code': 200,
            'data': [
                {
                    "Course_ID": "COR001",
                    "Skill_Description": "Sell",
                    "Skill_ID": 1,
                    "Skill_Name": "Sales",
                    "Skill_Type": "Active",
                    "Status": "Active"
                },
                {
                    "Course_ID": "COR002",
                    "Skill_Description": "Human Resources",
                    "Skill_ID": 2,
                    "Skill_Name": "HR",
                    "Skill_Type": "Active",
                    "Status": "Active"
                }
            ]
        })

    """"Done By Aloysius"""

    def test_get_courses_by_skill_id(self):
        # Uncomment below to see the full response of query
        # self.maxDiff = None

        course1 = Courses_Catalog(
            Course_ID="COR001",
            Course_Name="Systems Thinking and Design",
            Course_Description="This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking",
            Course_Status="Active",
            Course_Type="Internal",
            Course_Category="Core")

        course2 = Courses_Catalog(
            Course_ID='COR002',
            Course_Name='Lean Six Sigma Green Belt Certification',
            Course_Description='Apply Lean Six Sigma methodology and statistical tools such as Minitab to be used in process analytics',
            Course_Status='Active',
            Course_Type='Internal',
            Course_Category='Core')

        course3 = Courses_Catalog(
            Course_ID='SAL003',
            Course_Name='Optimising Your Brand For The Digital Spaces',
            Course_Description='Digital has fundamentally shifted communication between brands and their consumers from a one-way broadcast to a two-way dialogue. In a hastened bid to transform their businesses to be digital market-ready,',
            Course_Status='Active',
            Course_Type='External',
            Course_Category='Sales')

        skill1 = Skill(
            Skill_ID='1',
            Skill_Name='Sales',
            Skill_Description='Sell',
            Skill_Type='Active',
            Status='Active',
            Created_Date=datetime(2012, 3, 3, 10, 10, 10)
        )

        course_skill1 = course_skills(
            Course_ID='COR001',
            Skill_ID='1'
        )
        course_skill2 = course_skills(
            Course_ID='COR002',
            Skill_ID='1'
        )
        course_skill3 = course_skills(
            Course_ID='SAL003',
            Skill_ID='1'
        )

        db.session.add(course1)
        db.session.add(course2)
        db.session.add(course3)
        db.session.add(skill1)
        db.session.add(course_skill1)
        db.session.add(course_skill2)
        db.session.add(course_skill3)
        db.session.commit()

        response = self.client.get("/getCoursesBySkill/1",
                                   content_type='application/json')

        self.assertEqual(response.json, {
            'code': 200,
            'data': {
                'courseCatalog': [
                    {
                        'Course_ID': 'COR001',
                        'Course_Name': 'Systems Thinking and Design',
                        'Course_Description': 'This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking',
                        'Course_Status': 'Active',
                        'Course_Type': 'Internal',
                        'Course_Category': 'Core'
                    },
                    {
                        'Course_ID': 'COR002',
                        'Course_Name': 'Lean Six Sigma Green Belt Certification',
                        'Course_Description': 'Apply Lean Six Sigma methodology and statistical tools such as Minitab to be used in process analytics',
                        'Course_Status': 'Active',
                        'Course_Type': 'Internal',
                        'Course_Category': 'Core'
                    },
                    {
                        'Course_ID': 'SAL003',
                        'Course_Name': 'Optimising Your Brand For The Digital Spaces',
                        'Course_Description': 'Digital has fundamentally shifted communication between brands and their consumers from a one-way broadcast to a two-way dialogue. In a hastened bid to transform their businesses to be digital market-ready,',
                        'Course_Status': 'Active',
                        'Course_Type': 'External',
                        'Course_Category': 'Sales'
                    }
                ]
            }
        })

    """"Done By Aloysius"""

    def test_update_course_skills(self):

        course1 = Courses_Catalog(
            Course_ID="COR001",
            Course_Name="Systems Thinking and Design",
            Course_Description="This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking",
            Course_Status="Active",
            Course_Type="Internal",
            Course_Category="Core")

        skill1 = Skill(
            Skill_ID=1,
            Skill_Name='Plant Rice',
            Skill_Description='Gains the ability to plant rice',
            Skill_Type='Soft Skill',
            Status='Active',
            Created_Date=datetime(2022, 10, 27, 0, 0, 0)
        )

        skill2 = Skill(
            Skill_ID=2,
            Skill_Name='Plant Rice2',
            Skill_Description='Gains the ability to plant rice2',
            Skill_Type='Soft Skill',
            Status='Active',
            Created_Date=datetime(2022, 10, 27, 0, 0, 0)
        )

        course_skill1 = course_skills(
            Course_ID='COR001',
            Skill_ID='1'
        )

        course_skill2 = course_skills(
            Course_ID='COR001',
            Skill_ID='2'
        )

        db.session.add(course1)
        db.session.add(skill1)
        db.session.add(skill2)
        db.session.add(course_skill1)
        db.session.add(course_skill2)
        db.session.commit()

        updateForm = {
            'updateInfo': {
                'skillsForUpdate': ['Plant Rice'],
                'courseId': 'COR001'
            }
        }

        response = self.client.post("/updateCourseSkills",
                                    content_type='application/json',
                                    data=json.dumps(updateForm))

        self.assertEqual(response.json, {
            "code": 201,
            "message": 'Successfully updated courses.'
        })


''' Test Cases for Roles '''


class TestRoles(TestApp):
    # Done by: max
    def test_get_all_roles(self):
        role1 = job_role(
            Job_Role_ID=2,
            Job_Role_Name="Engineer",
            Job_Role_Description="Engineers, as practitioners of engineering, are professionals who invent, design, analyze, build and test machines, complex systems, structures, gadgets and materials to fulfill functional objectives and requirements while considering the limitations impo",
            Department="Engineering",
            Status="Active",
            Created_Date=datetime(2022, 10, 27, 0, 0, 0))

        role2 = job_role(
            Job_Role_ID=17,
            Job_Role_Name="Software Developer",
            Job_Role_Description="Develop software applications",
            Department="Technology",
            Status="Active",
            Created_Date=datetime(2022, 10, 18, 0, 0, 0))

        db.session.add(role1)
        db.session.add(role2)
        db.session.commit()

        response = self.client.get("/roles",
                                   content_type='application/json')

        self.assertEqual(response.json, {
            'code': 200,
            'data': {
                'roles': [
                    {
                        'Job_Role_ID': 2,
                        'Job_Role_Name': 'Engineer',
                        'Job_Role_Description': 'Engineers, as practitioners of engineering, are professionals who invent, design, analyze, build and test machines, complex systems, structures, gadgets and materials to fulfill functional objectives and requirements while considering the limitations impo',
                        'Department': 'Engineering',
                        'Status': 'Active',
                        'Created_Date': 'Thu, 27 Oct 2022 00:00:00 GMT'
                    },

                    {
                        'Job_Role_ID': 17,
                        'Job_Role_Name': 'Software Developer',
                        'Job_Role_Description': 'Develop software applications',
                        'Department': 'Technology',
                        'Status': 'Active',
                        'Created_Date': 'Tue, 18 Oct 2022 00:00:00 GMT'
                    }
                ]
            }
        })

    # Done by: max
    def test_get_roles_with_skills(self):
        role1 = job_role(
            Job_Role_ID=2,
            Job_Role_Name="Engineer",
            Job_Role_Description="Engineers, as practitioners of engineering, are professionals who invent, design, analyze, build and test machines, complex systems, structures, gadgets and materials to fulfill functional objectives and requirements while considering the limitations impo",
            Department="Engineering",
            Status="Active",
            Created_Date=datetime(2022, 10, 27, 0, 0, 0))

        role2 = job_role(
            Job_Role_ID=17,
            Job_Role_Name="Software Developer",
            Job_Role_Description="Develop software applications",
            Department="Technology",
            Status="Active",
            Created_Date=datetime(2022, 10, 18, 0, 0, 0))

        skill1 = Skill(
            Skill_ID=1,
            Skill_Name='Plant Rice',
            Skill_Description='Gains the ability to plant rice',
            Skill_Type='Soft Skill',
            Status='Active',
            Created_Date=datetime(2022, 10, 27, 0, 0, 0)
        )

        skill2 = Skill(
            Skill_ID=2,
            Skill_Name='Doom',
            Skill_Description='Inflicts a curse that dispels an enemy Hero and prevents them from casting spells or using items, while taking damage over time',
            Skill_Type='Hard Skill',
            Status='Inactive',
            Created_Date=datetime(2022, 10, 10, 0, 0, 0)
        )

        job_role_skill1 = job_role_skills(
            Job_Role_ID=2,
            Skill_ID=1
        )

        job_role_skill2 = job_role_skills(
            Job_Role_ID=17,
            Skill_ID=2
        )

        db.session.add(role1)
        db.session.add(role2)
        db.session.add(skill1)
        db.session.add(skill2)
        db.session.add(job_role_skill1)
        db.session.add(job_role_skill2)
        db.session.commit()

        response = self.client.get("/getRolesWithSkills",
                                   content_type='application/json')

        self.assertEqual(response.json, {
            'code': 200,
            'data': [
                {
                    "Department": "Engineering",
                    "Job_Role_Description": "Engineers, as practitioners of engineering, are professionals who invent, design, analyze, build and test machines, complex systems, structures, gadgets and materials to fulfill functional objectives and requirements while considering the limitations impo",
                    "Job_Role_ID": 2,
                    "Job_Role_Name": "Engineer",
                    "Skill_ID": 1,
                    "Skill_Name": "Plant Rice",
                    "Status": "Active"
                },
                {
                    "Department": "Technology",
                    "Job_Role_Description": "Develop software applications",
                    "Job_Role_ID": 17,
                    "Job_Role_Name": "Software Developer",
                    "Skill_ID": 2,
                    "Skill_Name": "Doom",
                    "Status": "Active"
                }
            ]
        })

    """ Done by: Aloysius"""

    def test_create_role(self):
        self.maxDiff = None

        skill1 = Skill(
            Skill_ID=1,
            Skill_Name='Plant Rice',
            Skill_Description='Gains the ability to plant rice',
            Skill_Type='Soft Skill',
            Status='Active',
            Created_Date=datetime(2022, 10, 27, 0, 0, 0)
        )

        db.session.add(skill1)
        db.session.commit()

        formData = {
            'name': 'Test Role',
            'department': 'HR',
            'description': 'This is a test role',
            'skills': [1],
            'status': "Active"
        }

        response = self.client.post("/createRole",
                                    content_type='application/json',
                                    data=json.dumps(formData))

        self.assertEqual(response.json, {
            "code": 201,
            "message": 'Successfully added a new role!'
        })

    """ Done by: Ho Zhi Ying """

    def test_update_role(self):

        role1 = job_role(
            Job_Role_ID=2,
            Job_Role_Name="Engineer",
            Job_Role_Description="Engineers, as practitioners of engineering, are professionals who invent, design, analyze, build and test machines, complex systems, structures, gadgets and materials to fulfill functional objectives and requirements while considering the limitations impo",
            Department="Engineering",
            Status="Active",
            Created_Date=datetime(2022, 10, 27, 0, 0, 0))

        role2 = job_role(
            Job_Role_ID=17,
            Job_Role_Name="Software Developer",
            Job_Role_Description="Develop software applications",
            Department="Technology",
            Status="Active",
            Created_Date=datetime(2022, 10, 18, 0, 0, 0))

        skill1 = Skill(
            Skill_ID=1,
            Skill_Name='Plant Rice',
            Skill_Description='Gains the ability to plant rice',
            Skill_Type='Soft Skill',
            Status='Active',
            Created_Date=datetime(2022, 10, 27, 0, 0, 0)
        )

        skill2 = Skill(
            Skill_ID=2,
            Skill_Name='Plant Rice2',
            Skill_Description='Gains the ability to plant rice2',
            Skill_Type='Soft Skill',
            Status='Active',
            Created_Date=datetime(2022, 10, 27, 0, 0, 0)
        )

        job_role_skill1 = job_role_skills(
            Job_Role_ID=17,
            Skill_ID=1
        )

        job_role_skill2 = job_role_skills(
            Job_Role_ID=17,
            Skill_ID=2
        )

        db.session.add(role1)
        db.session.add(role2)
        db.session.add(skill1)
        db.session.add(skill2)
        db.session.add(job_role_skill1)
        db.session.add(job_role_skill2)
        db.session.commit()

        # Change the name (Happy path)
        updateForm = {
            'id': 17,
            'name': 'Full Stack Developer',
            'description': 'Work on both front-end and back-end application.',
            'department': 'Technology',
            'status': 'Active',
            'skills': [1, 2]
        }

        response = self.client.post("/updateRole",
                                    content_type='application/json',
                                    data=json.dumps(updateForm))

        self.assertEqual(response.json, {
            "code": 201,
            "message": 'Successfully updated role.'
        })

        # Change to exact name of another role (Negative Case)
        updateForm = {
            'id': 17,
            'name': 'Engineer',
            'description': 'Develop software applications',
            'department': 'Technology',
            'status': 'Active',
            'skills': [1, 2]
        }

        response = self.client.post("/updateRole",
                                    content_type='application/json',
                                    data=json.dumps(updateForm))

        self.assertEqual(response.json, {
            "code": 400,
            "message": "Role already exists. Please use another role name."
        })
    
    '''Done by: Ho Zhi Ying'''
    def test_delete_role(self):
        role1 = job_role(
            Job_Role_ID=2,
            Job_Role_Name="Engineer",
            Job_Role_Description="Engineers, as practitioners of engineering, are professionals who invent, design, analyze, build and test machines, complex systems, structures, gadgets and materials to fulfill functional objectives and requirements while considering the limitations impo",
            Department="Engineering",
            Status="Active",
            Created_Date= datetime(2022, 10, 27, 0, 0, 0))

        db.session.add(role1)
        db.session.commit()

        role_ID_to_update = 2

        response = self.client.post("/deleteRole",
                                   content_type='application/json',
                                   data=json.dumps(role_ID_to_update))

        self.assertEqual(response.json, {
            "code": 201,
            "message": 'Successfully deleted role.'
        })
        pass


''' Test Cases for Skills '''


class TestSkills(TestApp):
    # Done by: max
    def test_get_all_skills(self):
        skill1 = Skill(
            Skill_ID=2,
            Skill_Name="Plant Rice",
            Skill_Description="Gains the ability to plant rice",
            Skill_Type="Soft Skill",
            Status="Active",
            Created_Date=datetime(2022, 10, 27, 0, 0, 0))

        skill2 = Skill(
            Skill_ID=6,
            Skill_Name="Kimchi Mixing",
            Skill_Description="Mixing veggies, chillis, sweat and tears.",
            Skill_Type="Hard Skill",
            Status="Active",
            Created_Date=datetime(2022, 10, 10, 0, 0, 0))

        db.session.add(skill1)
        db.session.add(skill2)
        db.session.commit()

        response = self.client.get("/skills",
                                   content_type='application/json')

        self.assertEqual(response.json, {
            'code': 200,
            'data': {
                'skills': [
                    {
                        'Skill_ID': 2,
                        'Skill_Name': 'Plant Rice',
                        'Skill_Description': 'Gains the ability to plant rice',
                        'Skill_Type': 'Soft Skill',
                        'Status': 'Active',
                        'Created_Date': 'Thu, 27 Oct 2022 00:00:00 GMT'
                    },

                    {
                        'Skill_ID': 6,
                        'Skill_Name': 'Kimchi Mixing',
                        'Skill_Description': 'Mixing veggies, chillis, sweat and tears.',
                        'Skill_Type': 'Hard Skill',
                        'Status': 'Active',
                        'Created_Date': 'Mon, 10 Oct 2022 00:00:00 GMT'
                    }
                ]
            }
        })

    """ Done by: Quentin """

    def test_get_skills_by_role(self):

        skill1 = Skill(
            Skill_ID='1',
            Skill_Name='Sales',
            Skill_Description='Sell',
            Skill_Type='Active',
            Status='Active',
            Created_Date=datetime(2022, 10, 27, 0, 0, 0)
        )

        skill2 = Skill(
            Skill_ID='2',
            Skill_Name='HR',
            Skill_Description='Human Resource',
            Skill_Type='Active',
            Status='Active',
            Created_Date=datetime(2022, 10, 27, 0, 0, 0)
        )

        role1 = job_role(
            Job_Role_ID=17,
            Job_Role_Name="Software Developer",
            Job_Role_Description="Develop software applications",
            Department="Technology",
            Status="Active",
            Created_Date=datetime(2022, 10, 18, 0, 0, 0))

        job_role_skill1 = job_role_skills(
            Job_Role_ID=17,
            Skill_ID=1
        )

        job_role_skill2 = job_role_skills(
            Job_Role_ID=17,
            Skill_ID=2
        )

        db.session.add(skill1)
        db.session.add(skill2)
        db.session.add(role1)
        db.session.add(job_role_skill1)
        db.session.add(job_role_skill2)
        db.session.commit()

        response = self.client.get("/skills-by-role?roleId=17",
                                   content_type='application/json')

        self.assertEqual(response.json, {
            "code": 200,
            "data": {
                "skills": [
                    {
                        'Skill_ID': 1,
                        'Skill_Name': 'Sales',
                        'Skill_Description': 'Sell',
                        'Skill_Type': 'Active',
                        'Status': 'Active',
                        'Created_Date': 'Thu, 27 Oct 2022 00:00:00 GMT'
                    },
                    {
                        'Skill_ID': 2,
                        'Skill_Name': 'HR',
                        'Skill_Description': 'Human Resource',
                        'Skill_Type': 'Active',
                        'Status': 'Active',
                        'Created_Date': 'Thu, 27 Oct 2022 00:00:00 GMT'
                    }
                ]
            }
        })

    '''Done by: Ho Zhi Ying'''
    def test_delete_skill(self):
        skill1 = Skill(
            Skill_ID='1',
            Skill_Name='Sales',
            Skill_Description='Sell',
            Skill_Type='Active',
            Status='Active',
            Created_Date= datetime(2022, 10, 27, 0, 0, 0)
        )

        db.session.add(skill1)
        db.session.commit()

        skill_ID_to_update = 1

        response = self.client.post("/deleteSkill",
                                   content_type='application/json',
                                   data=json.dumps(skill_ID_to_update))

        self.assertEqual(response.json, {
            "code": 201,
            "message": 'Successfully deleted skill.'
        })
        pass

    """Done By Aloysius"""
    # '/skills/AddNewSkill

    def test_create_skill(self):
        skill1 = Skill(
            Skill_ID=1,
            Skill_Name='Plant Rice',
            Skill_Description='Gains the ability to plant rice',
            Skill_Type='Soft Skill',
            Status='Active',
            Created_Date=datetime(2022, 10, 27, 0, 0, 0)
        )

        db.session.add(skill1)
        db.session.commit()

        formData = {
            'skillFormData': {
                'name': 'Test Skill',
                'type': 'Soft Skill',
                'description': 'This is a test role',
                'status': "Active"
            }
        }

        response = self.client.post("/skills/addNewSkill",
                                    content_type='application/json',
                                    data=json.dumps(formData))

        self.assertEqual(response.json, {
            "code": 201,
            "message": 'Successfully added a new skill!'
        })

    """Done By Aloysius"""

    def test_update_skill(self):
        skill1 = Skill(
            Skill_ID=1,
            Skill_Name='Plant Rice',
            Skill_Description='Gains the ability to plant rice',
            Skill_Type='Soft Skill',
            Status='Active',
            Created_Date=datetime(2022, 10, 27, 0, 0, 0)
        )

        db.session.add(skill1)
        db.session.commit()

        formData = {
            'skillFormData': {
                'id': 1,
                'name': 'Test Skill',
                'type': 'Soft Skill',
                'description': 'This is a test role',
                'status': "Active"
            }
        }

        response = self.client.post("/skills/updateSkill",
                                    content_type='application/json',
                                    data=json.dumps(formData))

        self.assertEqual(response.json, {
            "code": 201,
            "message": 'Updated successfully'
        })


''' Test Cases for Learning Journey '''


class TestLearningJourney(TestApp):

    """"Done By Aloysius"""

    def test_view_learning_journey(self):

        role1 = job_role(
            Job_Role_ID='1',
            Job_Role_Name="Software Developer",
            Job_Role_Description="Develop software applications",
            Department="Technology",
            Status="Active",
            Created_Date=datetime(2022, 10, 18, 0, 0, 0))

        job_role_skill1 = job_role_skills(
            Job_Role_ID=1,
            Skill_ID=1
        )

        skill1 = Skill(
            Skill_ID='1',
            Skill_Name='Sales',
            Skill_Description='Sell',
            Skill_Type='Active',
            Status='Active',
            Created_Date=datetime(2022, 10, 27, 0, 0, 0)
        )

        system_role1 = system_role(
            Role_ID='1',
            Role_Name="Anything"
        )

        staff1 = staff(
            Staff_ID='130001',
            Staff_FName='John',
            Staff_LName='Cena',
            Dept='WWE',
            Email='johncena@wwe.com',
            System_Role='1'

        )

        learning_journey1 = learning_journey(
            LJ_ID='1',
            Staff_ID='130001',
            Job_Role_ID='1'
        )

        db.session.add(role1)
        db.session.add(skill1)
        db.session.add(system_role1)
        db.session.commit()
        db.session.add(staff1)
        db.session.add(job_role_skill1)
        db.session.commit()
        db.session.add(learning_journey1)
        db.session.commit()

        response = self.client.get("/learningJourney/viewLearningJourney/1",
                                   content_type='application/json')

        self.assertEqual(response.json, {
            "code": 200,
            "data": {
                "Job_Role_ID": 1,
                "LJ_ID": 1,
                "Staff_ID": 130001
            }
        })

    """"Done By Aloysius"""

    def test_view_staff_learning_journeys(self):
        role1 = job_role(
            Job_Role_ID='1',
            Job_Role_Name="Software Developer",
            Job_Role_Description="Develop software applications",
            Department="Technology",
            Status="Active",
            Created_Date=datetime(2022, 10, 27, 0, 0, 0))

        job_role_skill1 = job_role_skills(
            Job_Role_ID=1,
            Skill_ID=1
        )

        skill1 = Skill(
            Skill_ID='1',
            Skill_Name='Sales',
            Skill_Description='Sell',
            Skill_Type='Active',
            Status='Active',
            Created_Date=datetime(2022, 10, 27, 0, 0, 0)
        )

        system_role1 = system_role(
            Role_ID='1',
            Role_Name="Anything"
        )

        staff1 = staff(
            Staff_ID='130001',
            Staff_FName='John',
            Staff_LName='Cena',
            Dept='WWE',
            Email='johncena@wwe.com',
            System_Role='1'

        )

        learning_journey1 = learning_journey(
            LJ_ID='1',
            Staff_ID='130001',
            Job_Role_ID='1'
        )

        db.session.add(role1)
        db.session.add(skill1)
        db.session.add(system_role1)
        db.session.commit()
        db.session.add(staff1)
        db.session.add(job_role_skill1)
        db.session.commit()
        db.session.add(learning_journey1)
        db.session.commit()

        response = self.client.get("/learningJourney/viewStaffLearningJourneys/130001",
                                   content_type='application/json')

        self.assertEqual(response.json, {
            "code": 200,
            "data": {
                "learning_journeys": [
                    {
                        "Created_Date": "Thu, 27 Oct 2022 00:00:00 GMT",
                        "Department": "Technology",
                        "Job_Role_Description": "Develop software applications",
                        "Job_Role_ID": 1,
                        "Job_Role_Name": "Software Developer",
                        "LJ_ID": 1,
                        "Staff_ID": 130001
                    }
                ]
            }
        })

    def test_create_learning_journey(self):
        self.maxDiff = None

        system_role1 = system_role(
            Role_ID='1',
            Role_Name="Anything"
        )

        staff1 = staff(
            Staff_ID='130001',
            Staff_FName='John',
            Staff_LName='Cena',
            Dept='WWE',
            Email='johncena@wwe.com',
            System_Role='1'

        )

        role1 = job_role(
            Job_Role_ID='1',
            Job_Role_Name="Software Developer",
            Job_Role_Description="Develop software applications",
            Department="Technology",
            Status="Active",
            Created_Date=datetime(2022, 10, 27, 0, 0, 0))

        formData = {
            'staff_id': '130001',
            'job_role_id': 1
        }

        db.session.add(system_role1)
        db.session.add(role1)
        db.session.commit()
        db.session.add(staff1)
        db.session.commit()

        created_learning_journey = db.session.query(learning_journey).filter(
            learning_journey.Job_Role_ID == 1,
            learning_journey.Staff_ID == '130001'
        ).with_entities(learning_journey.LJ_ID)

        response = self.client.post("/learningJourney/createLearningJourney",
                                    content_type='application/json',
                                    data=json.dumps(formData))

        self.assertEqual(response.json, {
            "code": 201,
            "data": [dict(row) for row in created_learning_journey]
        })

    """"Done By Aloysius"""

    def test_get_learning_journey_by_role_id(self):
        role1 = job_role(
            Job_Role_ID='1',
            Job_Role_Name="Software Developer",
            Job_Role_Description="Develop software applications",
            Department="Technology",
            Status="Active",
            Created_Date=datetime(2022, 10, 27, 0, 0, 0))

        job_role_skill1 = job_role_skills(
            Job_Role_ID=1,
            Skill_ID=1
        )

        skill1 = Skill(
            Skill_ID='1',
            Skill_Name='Sales',
            Skill_Description='Sell',
            Skill_Type='Active',
            Status='Active',
            Created_Date=datetime(2022, 10, 27, 0, 0, 0)
        )

        system_role1 = system_role(
            Role_ID='1',
            Role_Name="Anything"
        )

        staff1 = staff(
            Staff_ID='130001',
            Staff_FName='John',
            Staff_LName='Cena',
            Dept='WWE',
            Email='johncena@wwe.com',
            System_Role='1'

        )

        learning_journey1 = learning_journey(
            LJ_ID='1',
            Staff_ID='130001',
            Job_Role_ID='1'
        )

        db.session.add(role1)
        db.session.add(skill1)
        db.session.add(system_role1)
        db.session.commit()
        db.session.add(staff1)
        db.session.add(job_role_skill1)
        db.session.commit()
        db.session.add(learning_journey1)
        db.session.commit()

        response = self.client.get("/learningJourney/getLearningJourneyRole/1",
                                   content_type='application/json')

        self.assertEqual(response.json, {
            "code": 200,
            "data": {
                "LJ_ID": "1",
                "Role": [
                    {
                        "Department": "Technology",
                        "Job_Role_Description": "Develop software applications",
                        "Job_Role_ID": 1,
                        "Job_Role_Name": "Software Developer"
                    }
                ]
            }
        })

    def test_create_learning_journey_skill(self):
        self.maxDiff = None

        system_role1 = system_role(
            Role_ID='1',
            Role_Name="Anything"
        )

        staff1 = staff(
            Staff_ID='130001',
            Staff_FName='John',
            Staff_LName='Cena',
            Dept='WWE',
            Email='johncena@wwe.com',
            System_Role='1'

        )

        skill1 = Skill(
            Skill_ID='1',
            Skill_Name='Sales',
            Skill_Description='Sell',
            Skill_Type='Active',
            Status='Active',
            Created_Date=datetime(2022, 10, 27, 0, 0, 0)
        )

        role1 = job_role(
            Job_Role_ID='1',
            Job_Role_Name="Software Developer",
            Job_Role_Description="Develop software applications",
            Department="Technology",
            Status="Active",
            Created_Date=datetime(2022, 10, 27, 0, 0, 0))

        learning_journey1 = learning_journey(
            LJ_ID=1,
            Staff_ID='130001',
            Job_Role_ID=1
        )

        formData = {
            'lj_id': 1,
            'staff_id': '130001',
            'skill_id': 1
        }

        db.session.add(system_role1)
        db.session.add(role1)
        db.session.add(skill1)
        db.session.commit()
        db.session.add(staff1)
        db.session.commit()
        db.session.add(learning_journey1)
        db.session.commit()

        response = self.client.post("/learningJourney/createLearningJourneySkill",
                                    content_type='application/json',
                                    data=json.dumps(formData))

        self.assertEqual(response.json, {
            "code": 201,
            "message": 'Successfully added a new learning journey!'
        })

    """"Done By Aloysius"""

    def test_get_learning_journey_skills_by_LJ_ID(self):
        role1 = job_role(
            Job_Role_ID='1',
            Job_Role_Name="Software Developer",
            Job_Role_Description="Develop software applications",
            Department="Technology",
            Status="Active",
            Created_Date=datetime(2022, 10, 27, 0, 0, 0))

        job_role_skill1 = job_role_skills(
            Job_Role_ID=1,
            Skill_ID=1
        )

        skill1 = Skill(
            Skill_ID='1',
            Skill_Name='Sales',
            Skill_Description='Sell',
            Skill_Type='Active',
            Status='Active',
            Created_Date=datetime(2022, 10, 27, 0, 0, 0)
        )

        system_role1 = system_role(
            Role_ID='1',
            Role_Name="Anything"
        )

        staff1 = staff(
            Staff_ID='130001',
            Staff_FName='John',
            Staff_LName='Cena',
            Dept='WWE',
            Email='johncena@wwe.com',
            System_Role='1'

        )

        learning_journey1 = learning_journey(
            LJ_ID='1',
            Staff_ID='130001',
            Job_Role_ID='1'
        )

        learning_journey_skill1 = learning_journey_skill(
            LJ_ID='1',
            Staff_ID='130001',
            Skill_ID='1'
        )

        db.session.add(role1)
        db.session.add(skill1)
        db.session.add(system_role1)
        db.session.commit()
        db.session.add(staff1)
        db.session.add(job_role_skill1)
        db.session.commit()
        db.session.add(learning_journey1)
        db.session.commit()
        db.session.add(learning_journey_skill1)
        db.session.commit()

        response = self.client.get("/learningJourney/getLearningJourneySkills/1",
                                   content_type='application/json')

        self.assertEqual(response.json, {
            "code": 200,
            "data": {
                "LJ_ID": "1",
                "Skills": [
                    {
                        "Skill_Description": "Sell",
                        "Skill_ID": 1,
                        "Skill_Name": "Sales",
                        "Skill_Type": "Active"
                    }
                ]
            }
        })

    def test_create_learning_journey_course(self):
        self.maxDiff = None

        registration1 = registration(
            Reg_ID=1,
            Course_ID='COR001',
            Staff_ID='130001',
            Reg_Status='Test',
            Completion_Status='test'
        )

        system_role1 = system_role(
            Role_ID='1',
            Role_Name="Anything"
        )

        staff1 = staff(
            Staff_ID='130001',
            Staff_FName='John',
            Staff_LName='Cena',
            Dept='WWE',
            Email='johncena@wwe.com',
            System_Role='1'

        )

        skill1 = Skill(
            Skill_ID='1',
            Skill_Name='Sales',
            Skill_Description='Sell',
            Skill_Type='Active',
            Status='Active',
            Created_Date=datetime(2022, 10, 27, 0, 0, 0)
        )

        role1 = job_role(
            Job_Role_ID='1',
            Job_Role_Name="Software Developer",
            Job_Role_Description="Develop software applications",
            Department="Technology",
            Status="Active",
            Created_Date=datetime(2022, 10, 27, 0, 0, 0))

        learning_journey1 = learning_journey(
            LJ_ID=1,
            Staff_ID='130001',
            Job_Role_ID=1
        )

        learning_journey_skill1 = learning_journey_skill(
            LJ_ID=1,
            Staff_ID='130001',
            Skill_ID=1
        )

        course1 = Courses_Catalog(
            Course_ID="COR001",
            Course_Name="Systems Thinking and Design",
            Course_Description="This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking",
            Course_Status="Active",
            Course_Type="Internal",
            Course_Category="Core"
        )

        db.session.add(system_role1)
        db.session.add(role1)
        db.session.add(skill1)
        db.session.add(course1)
        db.session.commit()
        db.session.add(staff1)
        db.session.commit()
        db.session.add(registration1)
        db.session.add(learning_journey1)
        db.session.commit()
        db.session.add(learning_journey_skill1)
        db.session.commit()

        formData = {
            'lj_id': 1,
            'staff_id': '130001',
            'skill_id': 1,
            'course_id': 'COR001',
            'reg_id': 1
        }

        response = self.client.post("/learningJourney/createLearningJourneyCourse",
                                    content_type='application/json',
                                    data=json.dumps(formData))

        self.assertEqual(response.json, {
            "code": 201,
            "message": 'Successfully added a new learning journey!'
        })

    def test_add_learning_journey_course(self):

        registration1 = registration(
            Reg_ID=1,
            Course_ID='COR001',
            Staff_ID='130001',
            Reg_Status='Test',
            Completion_Status='test'
        )

        system_role1 = system_role(
            Role_ID='1',
            Role_Name="Anything"
        )

        staff1 = staff(
            Staff_ID='130001',
            Staff_FName='John',
            Staff_LName='Cena',
            Dept='WWE',
            Email='johncena@wwe.com',
            System_Role='1'

        )

        skill1 = Skill(
            Skill_ID='1',
            Skill_Name='Sales',
            Skill_Description='Sell',
            Skill_Type='Active',
            Status='Active',
            Created_Date=datetime(2022, 10, 27, 0, 0, 0)
        )

        role1 = job_role(
            Job_Role_ID='1',
            Job_Role_Name="Software Developer",
            Job_Role_Description="Develop software applications",
            Department="Technology",
            Status="Active",
            Created_Date=datetime(2022, 10, 27, 0, 0, 0))

        learning_journey1 = learning_journey(
            LJ_ID=1,
            Staff_ID='130001',
            Job_Role_ID=1
        )

        learning_journey_skill1 = learning_journey_skill(
            LJ_ID=1,
            Staff_ID='130001',
            Skill_ID=1
        )

        course1 = Courses_Catalog(
            Course_ID="COR001",
            Course_Name="Systems Thinking and Design",
            Course_Description="This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking",
            Course_Status="Active",
            Course_Type="Internal",
            Course_Category="Core"
        )

        db.session.add(system_role1)
        db.session.add(role1)
        db.session.add(skill1)
        db.session.add(course1)
        db.session.commit()
        db.session.add(staff1)
        db.session.commit()
        db.session.add(registration1)
        db.session.add(learning_journey1)
        db.session.commit()
        db.session.add(learning_journey_skill1)
        db.session.commit()

        formData = {
            'lj_id': 1,
            'staff_id': '130001',
            'skill_id': 1,
            'course_id': 'COR002',
            'reg_id': 1
        }

        response = self.client.post("/learningJourney/createLearningJourneyCourse",
                                    content_type='application/json',
                                    data=json.dumps(formData))

        self.assertEqual(response.json, {
            "code": 201,
            "message": 'Successfully added a new learning journey!'
        })

    def test_delete_existing_learning_journey_course(self):
        registration1 = registration(
            Reg_ID=1,
            Course_ID='COR001',
            Staff_ID='130001',
            Reg_Status='Test',
            Completion_Status='test'
        )

        system_role1 = system_role(
            Role_ID='1',
            Role_Name="Anything"
        )

        staff1 = staff(
            Staff_ID='130001',
            Staff_FName='John',
            Staff_LName='Cena',
            Dept='WWE',
            Email='johncena@wwe.com',
            System_Role='1'

        )

        skill1 = Skill(
            Skill_ID='1',
            Skill_Name='Sales',
            Skill_Description='Sell',
            Skill_Type='Active',
            Status='Active',
            Created_Date=datetime(2022, 10, 27, 0, 0, 0)
        )

        role1 = job_role(
            Job_Role_ID='1',
            Job_Role_Name="Software Developer",
            Job_Role_Description="Develop software applications",
            Department="Technology",
            Status="Active",
            Created_Date=datetime(2022, 10, 27, 0, 0, 0))

        learning_journey1 = learning_journey(
            LJ_ID=1,
            Staff_ID='130001',
            Job_Role_ID=1
        )

        learning_journey_skill1 = learning_journey_skill(
            LJ_ID=1,
            Staff_ID='130001',
            Skill_ID=1
        )

        course1 = Courses_Catalog(
            Course_ID="COR001",
            Course_Name="Systems Thinking and Design",
            Course_Description="This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking",
            Course_Status="Active",
            Course_Type="Internal",
            Course_Category="Core"
        )

        learning_journey_course1 = learning_journey_course(
            LJ_ID=1,
            Staff_ID='130001',
            Skill_ID=1,
            Course_ID='COR001',
            Reg_ID=1
        )

        db.session.add(system_role1)
        db.session.add(role1)
        db.session.add(skill1)
        db.session.add(course1)
        db.session.commit()
        db.session.add(staff1)
        db.session.commit()
        db.session.add(registration1)
        db.session.add(learning_journey1)
        db.session.commit()
        db.session.add(learning_journey_skill1)
        db.session.commit()
        db.session.add(learning_journey_course1)
        db.session.commit()

        formData = {
            'deleteInfo': {
                'LJ_id': 1,
                'staff_id': '130001',
                'course_id': 'COR001'
            }
        }

        response = self.client.post("/deleteLearningJourneyCourse",
                                    content_type='application/json',
                                    data=json.dumps(formData))

        self.assertEqual(response.json, {
            "code": 201,
            "message": 'Successfully delete courses.'
        })


if __name__ == "__main__":
    unittest.main()
