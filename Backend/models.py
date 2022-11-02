from Backend import db
from dataclasses import dataclass
from datetime import datetime

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
    
    def json(self):
        return {"Skill_ID": self.Skill_ID, "Course_ID": self.Course_ID}

class job_role(db.Model):
    __tablename__ = 'job_role'

    Job_Role_ID = db.Column(db.Integer, primary_key=True)
    Job_Role_Name = db.Column(db.String(50), nullable=False)
    Job_Role_Description = db.Column(db.String(255), nullable=False)
    Department = db.Column(db.String(50))
    Status = db.Column(db.String(20))
    Created_Date  = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


    def __init__(self, Job_Role_ID, Job_Role_Name, Job_Role_Description, Department, Status, Created_Date):
        self.Job_Role_ID = Job_Role_ID
        self.Job_Role_Name = Job_Role_Name
        self.Job_Role_Description = Job_Role_Description
        self.Department = Department
        self.Status = Status
        self.Created_Date = Created_Date

    def json(self):
        # return {"Role_ID": self.Job_Role_ID, "Role_Name": self.Job_Role_Name, "Role_Description": self.Job_Role_Description}

        return {"Job_Role_ID": self.Job_Role_ID, "Job_Role_Name": self.Job_Role_Name, "Job_Role_Description": self.Job_Role_Description, "Department": self.Department, 'Status': self.Status, "Created_Date": self.Created_Date}

class job_role_skills(db.Model):
    __tablename__ = 'job_role_skills'

    Job_Role_ID = db.Column(db.Integer, db.ForeignKey(job_role.Job_Role_ID), primary_key=True)
    Skill_ID = db.Column(db.Integer, db.ForeignKey(Skill.Skill_ID), primary_key=True)

    def __init__(self, Job_Role_ID, Skill_ID):
        self.Job_Role_ID = Job_Role_ID
        self.Skill_ID = Skill_ID
    
    def json(self):
        return {"Role_ID": self.Job_Role_ID, "Skill_ID": self.Skill_ID}

class system_role(db.Model):
    __tablename__ = 'system_role'

    Role_ID = db.Column(db.Integer, primary_key=True)
    Role_Name = db.Column(db.String(50))

    def __init__(self, Role_ID, Role_Name):
        self.Role_ID = Role_ID
        self.Role_Name = Role_Name
    
    def json(self):
        return {"Role_ID": self.Role_ID, "Role_Name": self.Role_Name}

class staff(db.Model):
    __tablename__ = 'staff'

    Staff_ID = db.Column(db.Integer, primary_key=True)
    Staff_FName = db.Column(db.String(50))
    Staff_LName = db.Column(db.String(50)) 
    Dept = db.Column(db.String(50)) 
    Email = db.Column(db.String(50)) 
    System_Role = db.Column(db.Integer, db.ForeignKey(system_role.Role_ID))

    def __init__(self, Staff_ID, Staff_FName, Staff_LName, Dept, Email, System_Role):
        self.Staff_ID = Staff_ID
        self.Staff_FName = Staff_FName
        self.Staff_LName = Staff_LName
        self.Dept = Dept
        self.Email = Email
        self.System_Role = System_Role
    
    def json(self):
        return {"Staff_ID": self.Staff_ID, "Staff_FName": self.Staff_FName, "Staff_LName": self.Staff_LName, "Dept": self.Dept, "Email": self.Email, "System_Role": self.System_Role}

class registration(db.Model):
    __tablename__ = 'registration'

    Reg_ID = db.Column(db.Integer, primary_key=True)
    Course_ID = db.Column(db.String(20), db.ForeignKey(Courses_Catalog.Course_ID))
    Staff_ID = db.Column(db.Integer, db.ForeignKey(staff.Staff_ID))
    Reg_Status = db.Column(db.String(20))
    Completion_Status = db.Column(db.String(20))

    def __init__(self, Reg_ID, Course_ID, Staff_ID, Reg_Status, Completion_Status):
        self.Reg_ID = Reg_ID
        self.Course_ID = Course_ID
        self.Staff_ID = Staff_ID
        self.Reg_Status = Reg_Status
        self.Completion_Status = Completion_Status
    
    def json(self):
        return {"Reg_ID": self.Reg_ID, "Course_ID": self.Course_ID, "Staff_ID": self.Staff_ID, "Reg_Status": self.Reg_Status, "Completion_Status": self.Completion_Status}

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
    Course_ID = db.Column(db.String(20), db.ForeignKey(Courses_Catalog.Course_ID), primary_key=True)
    Reg_ID = db.Column(db.Integer, db.ForeignKey(registration.Reg_ID), nullable=True)

    def __init__(self, LJ_ID, Staff_ID, Skill_ID, Course_ID, Reg_ID):
        self.LJ_ID = LJ_ID
        self.Staff_ID = Staff_ID
        self.Skill_ID = Skill_ID
        self.Course_ID = Course_ID
        self.Reg_ID = Reg_ID

    def json(self):
        return {"LJ_ID": self.LJ_ID, "Staff_ID": self.Staff_ID, "Skill_ID": self.Skill_ID, "Course_ID": self.Course_ID, "Reg_ID": self.Reg_ID}






