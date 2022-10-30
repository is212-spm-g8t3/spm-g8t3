import unittest
import flask_testing
from ljps import *
# from unittest.mock import MagicMock

class TestApp(flask_testing.TestCase):

    # Setting a in-memory temporary database
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
        'dbURL') or 'mysql+mysqlconnector://' + db_creds.username + ':' + db_creds.password + '@' + db_creds.hostname + ':3306/ljps_test'
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
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

    # # Setting a in-memory temporary database
    # def create_app(self):
    #     return create_test_app()

    # def setUp(self):
    #     db.create_all()

    # def tearDown(self):
    #     db.session.remove()
    #     db.drop_all()
    
class TestGetAllCourses(TestApp):
    ''' 
    Test Cases for Courses
    '''
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
            Course_ID= 'COR002',
            Course_Name= 'Lean Six Sigma Green Belt Certification',
            Course_Description='Apply Lean Six Sigma methodology and statistical tools such as Minitab to be used in process analytics',
            Course_Status= 'Active',
            Course_Type= 'Internal',
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
            Course_Category= 'Sales'
                    )

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

if __name__ == "__main__":
    unittest.main()