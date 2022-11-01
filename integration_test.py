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
            Course_ID= 'SAL003',
            Course_Name= 'Optimising Your Brand For The Digital Spaces',
            Course_Description= 'Digital has fundamentally shifted communication between brands and their consumers from a one-way broadcast to a two-way dialogue. In a hastened bid to transform their businesses to be digital market-ready,',
            Course_Status= 'Active',
            Course_Type= 'External',
            Course_Category= 'Sales')

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
            Created_Date= datetime(2012, 3, 3, 10, 10, 10)
        )

        skill2 = Skill(
            Skill_ID='2',
            Skill_Name='HR',
            Skill_Description='Human Resources',
            Skill_Type='Active',
            Status='Active',
            Created_Date= datetime(2012, 3, 3, 10, 10, 10)
        )

        skill3 = Skill(
            Skill_ID='3',
            Skill_Name='Hacking',
            Skill_Description='Hacking',
            Skill_Type='Active',
            Status='Active',
            Created_Date= datetime(2012, 3, 3, 10, 10, 10)
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
            Course_ID= 'COR002',
            Course_Name= 'Lean Six Sigma Green Belt Certification',
            Course_Description='Apply Lean Six Sigma methodology and statistical tools such as Minitab to be used in process analytics',
            Course_Status= 'Active',
            Course_Type= 'Internal',
            Course_Category='Core')

        skill1 = Skill(
            Skill_ID='1',
            Skill_Name='Sales',
            Skill_Description='Sell',
            Skill_Type='Active',
            Status='Active',
            Created_Date= datetime(2012, 3, 3, 10, 10, 10)
        )

        skill2 = Skill(
            Skill_ID='2',
            Skill_Name='HR',
            Skill_Description='Human Resources',
            Skill_Type='Active',
            Status='Active',
            Created_Date= datetime(2012, 3, 3, 10, 10, 10)
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
            Course_ID= 'COR002',
            Course_Name= 'Lean Six Sigma Green Belt Certification',
            Course_Description='Apply Lean Six Sigma methodology and statistical tools such as Minitab to be used in process analytics',
            Course_Status= 'Active',
            Course_Type= 'Internal',
            Course_Category='Core')

        course3 = Courses_Catalog(
            Course_ID= 'SAL003',
            Course_Name= 'Optimising Your Brand For The Digital Spaces',
            Course_Description= 'Digital has fundamentally shifted communication between brands and their consumers from a one-way broadcast to a two-way dialogue. In a hastened bid to transform their businesses to be digital market-ready,',
            Course_Status= 'Active',
            Course_Type= 'External',
            Course_Category= 'Sales')

        skill1 = Skill(
            Skill_ID='1',
            Skill_Name='Sales',
            Skill_Description='Sell',
            Skill_Type='Active',
            Status='Active',
            Created_Date= datetime(2012, 3, 3, 10, 10, 10)
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

    def test_update_course_skills(self):
        course1 = Courses_Catalog(
            Course_ID="COR001",
            Course_Name="Systems Thinking and Design",
            Course_Description="This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking",
            Course_Status="Active",
            Course_Type="Internal",
            Course_Category="Core")

        course_skill1 = course_skills(
            Course_ID='COR001',
            Skill_ID='1'
        )

        course_skill2 = course_skills(
            Course_ID='COR001',
            Skill_ID='2'
        )

        skill1 = Skill(
            Skill_ID='1',
            Skill_Name='Sales',
            Skill_Description='Sell',
            Skill_Type='Active',
            Status='Active',
            Created_Date= datetime(2012, 3, 3, 10, 10, 10)
        )

        skill2 = Skill(
            Skill_ID='2',
            Skill_Name='HR',
            Skill_Description='Human Resource',
            Skill_Type='Active',
            Status='Active',
            Created_Date= datetime(2012, 3, 3, 10, 10, 10)
        )

        db.session.add(course1)
        db.session.add(skill1)
        db.session.add(skill2)
        # db.session.add(course_skill1)
        # db.session.add(course_skill2)
        db.session.commit()

        data = str({"updateInfo":{"skillsForUpdate":["Sales","HR"],"courseId":"COR001"}})
        datajson = json.dumps(data)
    
        # print(dict(updateInfo=dict(skillsForUpdate=['Sales', 'HR'],courseId="COR001")))

        response = self.client.post("/updateCourseSkills",
                                    data=data,
                                    content_type='application/json')
        
        self.assertEqual(response.json, {
            "code": 201,
            "message": 'Successfully updated courses.'
        })

''' Test Cases for Roles '''
class TestRoles(TestApp):
    def test_get_all_roles(self):
        role1 = job_role(
            Job_Role_ID=2,
            Job_Role_Name="Engineer",
            Job_Role_Description="Engineers, as practitioners of engineering, are professionals who invent, design, analyze, build and test machines, complex systems, structures, gadgets and materials to fulfill functional objectives and requirements while considering the limitations impo",
            Department="Engineering",
            Status="Active",
            Created_Date= datetime(2022, 10, 27, 0, 0, 0))

        role2 = job_role(
            Job_Role_ID=17,
            Job_Role_Name="Software Developer",
            Job_Role_Description="Develop software applications",
            Department="Technology",
            Status="Active",
            Created_Date= datetime(2022, 10, 18, 0, 0, 0))

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

    def test_get_roles_with_skills(self):
        pass

    def test_create_role(self):
        pass


''' Test Cases for Skills '''
class TestSkills(TestApp):
    def test_get_all_skills(self):
        pass

    def test_get_skills_by_role(self):
        pass

    # '/skills/AddNewSkill
    def test_create_skill(self):
        pass

    def test_update_skill(self):
        pass


''' Test Cases for Learning Journey '''
class TestLearningJourney(TestApp):
    def test_view_learning_journey(self):
        pass

    def test_view_staff_learning_journeys(self):
        pass

    def test_create_learning_journey(self):
        pass

    def test_get_learning_journey_by_role_id(self):
        pass

    def test_create_learning_journey_skill(self):
        pass

    def test_get_learning_journey_skills_by_LJ_ID(self):
        pass

    def test_create_learning_journey_course(self):
        pass


if __name__ == "__main__":
    unittest.main()

