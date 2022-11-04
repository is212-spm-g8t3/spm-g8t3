# IS212 SPM G8T3 - Learning Journey Planning System (LJPS)
LJPS is a Web Application designed to enhance the learning experience of employees aiming to upskill themselves and progress their career. 

LJPS provides a user friendly interface for employees to the track courses they wish to complete based on the roles they are working towards in the form of Learning Journeys. Employees can explore the various roles avaliable to them, the skills required for those roles and the courses they need to accquire those skills, making it a breeze to plan their Learning Journey goals.

## Members
- Chia Yu-En Aloysius (yechia.2020@scis.smu.edu.sg)
- Darren Thyng Chuan Sik (darrenthyng.2020@scis.smu.edu.sg)
- Ho Zhi Ying (zhiying.ho.2020@scis.smu.edu.sg)
- Maximilian Tan Yong Xun (yxtan.2020@scis.smu.edu.sg)
- Quentin Quek Zhen Ming (quentinquek.2020@scis.smu.edu.sg)
- Tan ZhongLi Aaron (aaron.tan.2020@scis.smu.edu.sg)

## Github
https://github.com/is212-spm-g8t3/spm-g8t3

## LJPS Set Up
### Frontend Web Application - Node JS
1. Make sure Nodejs is downloaded, install here -> "https://nodejs.org/en/"
2. Open integrated terminal G8T3-LJPS/src
3. npm install
4. npm run serve (once install is done)

### Flask Backend & MySQL Database
1. Open MySQL Workbench
2. Run the database.sql to import the database schema
3. Run app.py to start the Flask server

### System Info
- Web App runs on port 8080
- Backend for API calls runs on port 5000

## Learning Journey Planning System
LJPS can be browsed to locally at localhost:8080
### Core Function 1 - View Skills Required By Selected role
1. Upon loading the system webpage, click login located on the top right in the navigation bar.
2. Sign in with the email: "Susan.Goh@allinone.com.sg" and password: "staffstaff".
3. Upon loading the system webpage, click on "Roles" located in the navigation bar on the left.
4. Click on the "+" icon to display the list of skills required for the selected role
### Core Function 2 - View/Add/Remove Courses on Learning Journey
1. Upon loading the system webpage, click login located on the top right in the navigation bar.
2. Sign in with the email: "Susan.Goh@allinone.com.sg" and password: "staffstaff".
3. Navigate to attainable Roles by clicking on "Browse" located in the navigation bar on the left.
4. Select a Role to start a learning journey for.
5. You will be able to view the Skills necessary for the selected Role.
6. Click on the "Select" button next to the Skill to view the Courses to attain the skill.
7. Click on "Add" to add the courses you want to take to attain the selected Skill.
    1. Click on "Remove" to remove courses
8. Click "Confirm" to confirm your selection
9. Click "Save" to save the Learning Journey.
### Core Function 3 - CRUD For Roles
1. Upon loading the system webpage, click login located on the top right in the navigation bar.
2. Sign in with the email: "Sally.Loh@allinone.com.sg" and password: "adminadmin".
3. Navigate to Role Management by clicking on "Roles" located in the navigation bar on the left
4. From the Role Management page, you can create a new role with the Create button on the top right or, edit the Role's details or delete it using the respective action buttons.
5. Create
    1. Click on the "Create" button
    2. Fill in the Role Name, Department, Role Description, Skills (optional) and Status.
    3. Click "Create"
6. Edit
    1. Click on the "Edit" button of the Role you intend to modify
    2. Modify the desired fields
    3. Click "Update" to save the changes
7. Delete
    1. Click on the "Delete" button of the Role you intend to modify
    2. The Role is now deleted

### Core Function 4 - CRUD For Skills
1. Upon loading the system webpage, click login located on the top right in the navigation bar.
2. Sign in with the email: "Sally.Loh@allinone.com.sg" and password: "adminadmin".
3. Navigate to Skill Management by clicking on "Skill" located in the navigation bar on the left.
4. From the Skill Management page, you can create a new Skill with the Create button on the top right or, edit the Skill's details the respective action button.
5. Create
    1. Click on the "Create" button
    2. Fill in the Skill Name, Type, Skill Description and Status.
    3. Click "Create"
6. Edit
    1. Click on the "Edit" button of the Skill you intend to modify
    2. Modify the desired fields
    3. Click "Update" to save the changes
### Core Function 5 - Assigning Skills to Roles and Courses
1. Upon loading the system webpage, click login located on the top right in the navigation bar.
2. Sign in with the email: "Sally.Loh@allinone.com.sg" and password: "adminadmin".
3. Navigate to either Role Management or Course Management by clicking on "Roles" or "Courses" located in the navigation bar on the left.
4. Assigning Skills to Roles
    1. Click on the "Edit" button of the Role you intend to assign skills to
    2. Under the "Skills" field, select the Skill(s) to assign to the role
    3. Click "Update" to save the changes
5. Assigning Skills to Courses
    1. Click on the "Edit" button of the Course you intend to assign skills to
    2. Under the "Skills" field, select the Skill(s) to assign to the role
    3. Click "Update" to save the changes

## Other Links
Please contact Ho Zhi Ying (zhiying.ho.2020@scis.smu.edu.sg) with your email for access to Jira and Confluence
### Confluence
https://spm-g8t3.atlassian.net/wiki/spaces/IS212SPMG8/overview
### Jira
https://spm-g8t3.atlassian.net/jira/software/c/projects/IS212G8T3/boards/2
