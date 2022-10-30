import unittest
from datetime import datetime
from ljps import *

'''
Test Done By: Quentin Quek 
'''
class TestCoursesCatalog(unittest.TestCase):

    def setUp(self):
        self.course1 = Courses_Catalog(
            Course_ID="COR001",
            Course_Name="Systems Thinking and Design",
            Course_Description="This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking",
            Course_Status="Active",
            Course_Type="Internal",
            Course_Category="Core")

    def tearDown(self):
        self.course1 = None

    def test_json(self):
        self.assertEqual(self.course1.json(), {
            'Course_ID': 'COR001',
            'Course_Name': 'Systems Thinking and Design',
            'Course_Description': 'This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking',
            'Course_Status': 'Active',
            'Course_Type': 'Internal',
            'Course_Category': 'Core'
        })

class TestSkill(unittest.TestCase):

    def setUp(self):
        self.skill1 = Skill(
            Skill_ID='1',
            Skill_Name='Sales',
            Skill_Description='Sell',
            Skill_Type='Soft Skill',
            Status='Active',
            Created_Date= '2022-10-25'
        )

    def tearDown(self):
        self.skill1 = None

    def test_json(self):
        self.assertEqual(self.skill1.json(), {
            'Skill_ID': '1',
            'Skill_Name': 'Sales',
            'Skill_Description': 'Sell',
            'Skill_Type': 'Soft Skill',
            'Status': 'Active',
            'Created_Date': '2022-10-25'
        })

class TestSkill(unittest.TestCase):

    def setUp(self):
        self.skill1 = Skill(
            Skill_ID='1',
            Skill_Name='Sales',
            Skill_Description='Sell',
            Skill_Type='Soft Skill',
            Status='Active',
            Created_Date= '2022-10-25'
        )

        self.course1 = Courses_Catalog(
            Course_ID="COR001",
            Course_Name="Systems Thinking and Design",
            Course_Description="This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking",
            Course_Status="Active",
            Course_Type="Internal",
            Course_Category="Core")

        self.course_skill1 = course_skills(
            Skill_ID = self.skill1.Skill_ID,
            Course_ID = self.course1.Course_ID
        )

    def tearDown(self):
        self.skill1 = None
        self.course1 = None
        self.course_skill1 = None

    def test_json(self):
        self.assertEqual(self.course_skill1.json(), {
            'Skill_ID': '1',
            'Course_ID': 'COR001'
        })

class TestJobRole(unittest.TestCase):

    def setUp(self):
        self.job_role1 = job_role(
            Job_Role_ID=1,
            Job_Role_Name='Engineer',
            Job_Role_Description='Engineers, as practitioners of engineering, are professionals who invent, design, analyze, build and test machines, complex systems, structures, gadgets and materials to fulfill functional objectives and requirements.',
            Department='Engineering',
            Status='Active',
            Created_Date='2022-10-25'
        )

    def tearDown(self):
        self.job_role1 = None

    def test_json(self):
        self.assertEqual(self.job_role1.json(), {
            'Job_Role_ID': 1,
            'Job_Role_Name': 'Engineer',
            'Job_Role_Description': 'Engineers, as practitioners of engineering, are professionals who invent, design, analyze, build and test machines, complex systems, structures, gadgets and materials to fulfill functional objectives and requirements.',
            'Department': 'Engineering',
            'Status': 'Active',
            'Created_Date': '2022-10-25'
        })

class TestJobRoleSkills(unittest.TestCase):

    def setUp(self):
        self.job_role_skill1 = job_role_skills(
            Job_Role_ID=2,
            Skill_ID=1
        )

    def tearDown(self):
        self.job_role_skill1 = None

    def test_json(self):
        self.assertEqual(self.job_role_skill1.json(), {
            'Role_ID': 2, 
            'Skill_ID': 1
        })

class TestSystemRole(unittest.TestCase):

    def setUp(self):
        self.system_role1 = system_role(
            Role_ID=1,
            Role_Name='Admin'
        )

    def tearDown(self):
        self.system_role1 = None

    def test_json(self):
        self.assertEqual(self.system_role1.json(), {
            'Role_ID': 1,
            'Role_Name': 'Admin'
        })

class TestStaff(unittest.TestCase):

    def setUp(self):
        self.staff1 = staff(
            Staff_ID='130002',
            Staff_FName='Jack',
            Staff_LName='Sim',
            Dept='CEO',
            Email='jack.sim@allinone.com.sg',
            System_Role='1'
        )

    def tearDown(self):
        self.staff1 = None

    def test_json(self):
        self.assertEqual(self.staff1.json(), {
            'Staff_ID': '130002',
            'Staff_FName': 'Jack',
            'Staff_LName': 'Sim',
            'Dept': 'CEO',
            'Email': 'jack.sim@allinone.com.sg',
            'System_Role': '1'
        })

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.registration1 = registration(
            Reg_ID='6',
            Course_ID='COR002',
            Staff_ID='140008',
            Reg_Status='Registered',
            Completion_Status='OnGoing'
        )

    def tearDown(self):
        self.registration1 = None

    def test_json(self):
        self.assertEqual(self.registration1.json(), {
            'Reg_ID': '6',
            'Course_ID': 'COR002',
            'Staff_ID': '140008',
            'Reg_Status': 'Registered',
            'Completion_Status': 'OnGoing',
        })

class TestLearningJourney(unittest.TestCase):

    def setUp(self):
        self.learning_journey1 = learning_journey(
            LJ_ID=1,
            Staff_ID=130002,
            Job_Role_ID=2
        )

    def tearDown(self):
        self.learning_journey1 = None

    def test_json(self):
        self.assertEqual(self.learning_journey1.json(), {
            'LJ_ID': 1,
            'Staff_ID': 130002,
            'Job_Role_ID': 2,
        })

class TestLearningJourneySkill(unittest.TestCase):

    def setUp(self):
        self.learning_journey_skill1 = learning_journey_skill(
            LJ_ID=1,
            Staff_ID=130001,
            Skill_ID=2
        )

    def tearDown(self):
        self.learning_journey_skill1 = None

    def test_json(self):
        self.assertEqual(self.learning_journey_skill1.json(), {
            'LJ_ID': 1,
            'Staff_ID': 130001,
            'Skill_ID': 2,
        })

class TestLearningJourneyCourse(unittest.TestCase):

    def setUp(self):
        self.learning_journey_course1 = learning_journey_course(
            LJ_ID=1,
            Staff_ID=130001,
            Skill_ID=1,
            Course_ID="COR001",
            Reg_ID=6
        )

    def tearDown(self):
        self.learning_journey_course1 = None

    def test_json(self):
        self.assertEqual(self.learning_journey_course1.json(), {
            'LJ_ID': 1,
            'Staff_ID': 130001,
            'Skill_ID': 1,
            'Course_ID': 'COR001',
            'Reg_ID': 6,
        })

