import unittest
import flask_testing
from ljps import *
# from unittest.mock import MagicMock

class TestApp(flask_testing.TestCase):

    # Setting a in-memory temporary database
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
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
        
        db.session.add(course1)
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
                    }
                ]
            }   
        })

    # Insert another test case here   


if __name__ == "__main__":
    unittest.main()