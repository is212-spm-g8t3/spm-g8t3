-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: ljps-db.cztujttsewgv.ap-southeast-1.rds.amazonaws.com    Database: ljps
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
-- SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

-- SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '';

--
-- Table structure for table `course_skills`
--

DROP TABLE IF EXISTS `course_skills`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course_skills` (
  `Course_ID` varchar(20) NOT NULL,
  `Skill_ID` int NOT NULL,
  PRIMARY KEY (`Course_ID`,`Skill_ID`),
  KEY `skill_fk2_idx` (`Skill_ID`),
  CONSTRAINT `course_fk2` FOREIGN KEY (`Course_ID`) REFERENCES `courses_catalog` (`Course_ID`),
  CONSTRAINT `skill_fk2` FOREIGN KEY (`Skill_ID`) REFERENCES `skill` (`Skill_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course_skills`
--

LOCK TABLES `course_skills` WRITE;
/*!40000 ALTER TABLE `course_skills` DISABLE KEYS */;
INSERT INTO `course_skills` VALUES ('COR001',1),('MGT002',2),('MGT001',3),('MGT007',3),('COR002',22),('COR002',23);
/*!40000 ALTER TABLE `course_skills` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `courses_catalog`
--

DROP TABLE IF EXISTS `courses_catalog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `courses_catalog` (
  `Course_ID` varchar(20) NOT NULL,
  `Course_Name` varchar(50) NOT NULL,
  `Course_Description` varchar(255) NOT NULL,
  `Course_Status` varchar(20) NOT NULL,
  `Course_Type` varchar(20) NOT NULL,
  `Course_Category` varchar(20) NOT NULL,
  PRIMARY KEY (`Course_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `courses_catalog`
--

LOCK TABLES `courses_catalog` WRITE;
/*!40000 ALTER TABLE `courses_catalog` DISABLE KEYS */;
INSERT INTO `courses_catalog` VALUES ('AGR001','Planting Rice','Agriculture or farming is the practice of cultivating plants and livestock. This course is focused on planting rice','Active','External','Farming'),('COR001','Systems Thinking and Design','This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking','Active','Internal','Core'),('COR002','Lean Six Sigma Green Belt Certification','Apply Lean Six Sigma methodology and statistical tools such as Minitab to be used in process analytics','Active','Internal','Core'),('COR004','Service Excellence','The programme provides the learner with the key foundations of what builds customer confidence in the service industr','Pending','Internal','Core'),('COR006','Manage Change','Identify risks associated with change and develop risk mitigation plans.','Retired','External','Core'),('FIN001','Data Collection and Analysis','Data is meaningless unless insights and analysis can be drawn to provide useful information for business decision-making. It is imperative that data quality, integrity and security ','Active','External','Finance'),('FIN002','Risk and Compliance Reporting','Regulatory reporting is a requirement for businesses from highly regulated sectors to demonstrate compliance with the necessary regulatory provisions.','Active','External','Finance'),('FIN003','Business Continuity Planning','Business continuity planning is essential in any business to minimise loss when faced with potential threats and disruptions.','Retired','External','Finance'),('HRD001','Leading and Shaping a Culture in Learning','This training programme, delivered by the National Centre of Excellence (Workplace Learning), aims to equip participants with the skills and knowledge of the National workplace learning certification framework,','Active','External','HR'),('MGT001','People Management','enable learners to manage team performance and development through effective communication, conflict resolution and negotiation skills.','Active','Internal','Management'),('MGT002','Workplace Conflict Management for Professionals','This course will address the gaps to build consensus and utilise knowledge of conflict management techniques to diffuse tensions and achieve resolutions effectively in the best interests of the organisation.','Active','External','Management'),('MGT003','Enhance Team Performance Through Coaching','The course aims to upskill real estate team leaders in the area of service coaching for performance.','Pending','Internal','Management'),('MGT004','Personal Effectiveness for Leaders','Learners will be able to acquire the skills and knowledge to undertake self-assessment in relation to one','Active','External','Management'),('MGT007','Supervisory Management Skills','Supervisors lead teams, manage tasks, solve problems, report up and down the hierarchy, and much more. ','Retired','External','Management'),('SAL001','Risk Management for Smart Business','Apply risk management concepts to digital business','Retired','Internal','Sales'),('SAL002','CoC in Smart Living Solutions','Participants will acquire the knowledge and skills in setting up a smart living solution','Pending','External','Sales'),('SAL003','Optimising Your Brand For The Digital Spaces','Digital has fundamentally shifted communication between brands and their consumers from a one-way broadcast to a two-way dialogue. In a hastened bid to transform their businesses to be digital market-ready,','Active','External','Sales'),('SAL004','Stakeholder Management','Develop a stakeholder engagement plan and negotiate with stakeholders to arrive at mutually-beneficial arrangements.','Active','Internal','Sales'),('tch001','Print Server Setup','Setting up print server in enterprise environment','Retired','Internal','Technical'),('tch002','Canon MFC Setup','Setting up Canon ImageRUNNER series of products','Retired','Internal','Technical'),('tch003','Canon MFC Mainteance and Troubleshooting','Troubleshoot and fixing L2,3 issues of Canon ImageRUNNER series of products','Active','Internal','Technical'),('tch004','Introduction to Open Platform Communications','This course provides the participants with a good in-depth understanding of the SS IEC 62541 standard','Pending','Internal','Technical'),('tch005','An Introduction to Sustainability','The course provides learners with the multi-faceted basic knowledge of sustainability.','Active','External','Technical'),('tch006','Machine Learning DevOps Engineer','The Machine Learning DevOps Engineer Nanodegree program focuses on the software engineering fundamentals needed to successfully streamline the deployment of data and machine-learning models','Pending','Internal','Technical'),('tch008','Technology Intelligence and Strategy','Participants will be able to gain knowledge and skills on: - establishing technology strategy with technology intelligence framework and tools','Active','External','Technical'),('tch009','Smart Sensing Technology','This course introduces sensors and sensing systems. The 5G infrastructure enables the many fast-growing IoT applications equipped with sensors ','Pending','External','Technical'),('tch012','Internet of Things','The Internet of Things (IoT) is integrating our digital and physical world, opening up new and exciting opportunities to deploy, automate, optimize and secure diverse use cases and applications. ','Active','Internal','Technical'),('tch013','Managing Cybersecurity and Risks','Digital security is the core of our daily lives considering that our dependence on the digital world','Active','Internal','Technical'),('tch014','Certified Information Privacy Professional','The Certified Information Privacy Professional/ Asia (CIPP/A) is the first publicly available privacy certification','Active','External','Technical'),('tch015','Network Security','Understanding of the fundamental knowledge of network security including cryptography, authentication and key distribution. The security techniques at various layers of computer networks are examined.','Active','External','Technical'),('tch018','Professional Project Management','solid foundation in the project management processes from initiating a project, through planning, execution, control,','Active','Internal','Technical'),('tch019','Innovation and Change Management','the organization that constantly reinvents itself to be relevant has a better chance of making progress','Active','External','Technical');
/*!40000 ALTER TABLE `courses_catalog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_role`
--

DROP TABLE IF EXISTS `job_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job_role` (
  `Job_Role_ID` int NOT NULL AUTO_INCREMENT,
  `Job_Role_Name` varchar(50) NOT NULL,
  `Job_Role_Description` varchar(255) NOT NULL,
  `Department` varchar(50) DEFAULT NULL,
  `Status` varchar(45) NOT NULL DEFAULT 'Active',
  `Created_Date` date DEFAULT NULL,
  PRIMARY KEY (`Job_Role_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_role`
--

LOCK TABLES `job_role` WRITE;
/*!40000 ALTER TABLE `job_role` DISABLE KEYS */;
INSERT INTO `job_role` VALUES (1,'Sales Representative','Serves customers by selling products and meeting customer needs','Sales','Active','2022-10-27'),(2,'Engineer','Engineers, as practitioners of engineering, are professionals who invent, design, analyze, build and test machines, complex systems, structures, gadgets and materials to fulfill functional objectives and requirements while considering the limitations impo','Engineering','Active','2022-10-27'),(17,'Software Developer','Develop software applications','Technology','Active','2022-10-18'),(18,'Data Scientist','Extracting data from multiple sources, using machine learning tools to organize data, process, clean, and validate the data etc.','Technology','Active','2022-10-21'),(19,'Talent Recruiter','Scout for amazing talent ','Human Resources','Active','2022-10-27'),(20,'UI/UX Designer','Design interfaces for various applications','Design','Inactive','2022-11-05'),(21,'Penetration Tester','A penetration test, also known as a pen test, is a simulated cyber attack against your computer system to check for exploitable vulnerabilities.','Cybersecurity','Active','2022-11-05'),(22,'System Administrator','Administrator of systems','Operations','Active','2022-11-05'),(23,'Cloud Architect','Design cloud architecture','Technology','Inactive','2022-11-05'),(24,'Human Resource Manager','Manage HR','HR','Active','2022-11-05');
/*!40000 ALTER TABLE `job_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_role_skills`
--

DROP TABLE IF EXISTS `job_role_skills`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job_role_skills` (
  `Job_Role_ID` int NOT NULL,
  `Skill_ID` int NOT NULL,
  PRIMARY KEY (`Job_Role_ID`,`Skill_ID`),
  KEY `Skill_fk_idx` (`Skill_ID`),
  CONSTRAINT `Role_fk` FOREIGN KEY (`Job_Role_ID`) REFERENCES `job_role` (`Job_Role_ID`),
  CONSTRAINT `Skill_fk` FOREIGN KEY (`Skill_ID`) REFERENCES `skill` (`Skill_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_role_skills`
--

LOCK TABLES `job_role_skills` WRITE;
/*!40000 ALTER TABLE `job_role_skills` DISABLE KEYS */;
INSERT INTO `job_role_skills` VALUES (17,1),(19,3),(24,3),(21,7),(1,21),(22,22),(22,23),(23,24);
/*!40000 ALTER TABLE `job_role_skills` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `learning_journey`
--

DROP TABLE IF EXISTS `learning_journey`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `learning_journey` (
  `LJ_ID` int NOT NULL AUTO_INCREMENT,
  `Staff_ID` int NOT NULL,
  `Job_Role_ID` int DEFAULT NULL,
  PRIMARY KEY (`LJ_ID`,`Staff_ID`),
  KEY `role_fk2_idx` (`Job_Role_ID`),
  KEY `lj_staff_fk` (`Staff_ID`),
  CONSTRAINT `lj_staff_fk` FOREIGN KEY (`Staff_ID`) REFERENCES `staff` (`Staff_ID`),
  CONSTRAINT `role_fk2` FOREIGN KEY (`Job_Role_ID`) REFERENCES `job_role` (`Job_Role_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `learning_journey`
--

LOCK TABLES `learning_journey` WRITE;
/*!40000 ALTER TABLE `learning_journey` DISABLE KEYS */;
INSERT INTO `learning_journey` VALUES (7,140002,17);
/*!40000 ALTER TABLE `learning_journey` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `learning_journey_course`
--

DROP TABLE IF EXISTS `learning_journey_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `learning_journey_course` (
  `LJ_ID` int NOT NULL,
  `Staff_ID` int NOT NULL,
  `Skill_ID` int NOT NULL,
  `Course_ID` varchar(20) NOT NULL,
  `Reg_ID` int DEFAULT NULL,
  PRIMARY KEY (`LJ_ID`,`Staff_ID`,`Skill_ID`,`Course_ID`),
  KEY `ljc_course_fk` (`Course_ID`),
  KEY `ljc_reg_fk` (`Reg_ID`),
  CONSTRAINT `ljc_course_fk` FOREIGN KEY (`Course_ID`) REFERENCES `courses_catalog` (`Course_ID`),
  CONSTRAINT `ljc_fk` FOREIGN KEY (`LJ_ID`, `Staff_ID`, `Skill_ID`) REFERENCES `learning_journey_skill` (`LJ_ID`, `Staff_ID`, `Skill_ID`),
  CONSTRAINT `ljc_reg_fk` FOREIGN KEY (`Reg_ID`) REFERENCES `registration` (`Reg_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `learning_journey_course`
--

LOCK TABLES `learning_journey_course` WRITE;
/*!40000 ALTER TABLE `learning_journey_course` DISABLE KEYS */;
INSERT INTO `learning_journey_course` VALUES (7,140002,1,'COR001',1);
/*!40000 ALTER TABLE `learning_journey_course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `learning_journey_skill`
--

DROP TABLE IF EXISTS `learning_journey_skill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `learning_journey_skill` (
  `LJ_ID` int NOT NULL,
  `Staff_ID` int NOT NULL,
  `Skill_ID` int NOT NULL,
  PRIMARY KEY (`LJ_ID`,`Staff_ID`,`Skill_ID`),
  KEY `ljs_skill_fk_idx` (`Skill_ID`),
  CONSTRAINT `ljs_fk` FOREIGN KEY (`LJ_ID`, `Staff_ID`) REFERENCES `learning_journey` (`LJ_ID`, `Staff_ID`),
  CONSTRAINT `ljs_skill_fk` FOREIGN KEY (`Skill_ID`) REFERENCES `skill` (`Skill_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `learning_journey_skill`
--

LOCK TABLES `learning_journey_skill` WRITE;
/*!40000 ALTER TABLE `learning_journey_skill` DISABLE KEYS */;
INSERT INTO `learning_journey_skill` VALUES (7,140002,1);
/*!40000 ALTER TABLE `learning_journey_skill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registration`
--

DROP TABLE IF EXISTS `registration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registration` (
  `Reg_ID` int NOT NULL,
  `Course_ID` varchar(20) NOT NULL,
  `Staff_ID` int NOT NULL,
  `Reg_Status` varchar(20) NOT NULL,
  `Completion_Status` varchar(20) NOT NULL,
  PRIMARY KEY (`Reg_ID`),
  KEY `course_fk` (`Course_ID`),
  KEY `staff_fk` (`Staff_ID`),
  CONSTRAINT `course_fk` FOREIGN KEY (`Course_ID`) REFERENCES `courses_catalog` (`Course_ID`),
  CONSTRAINT `staff_fk` FOREIGN KEY (`Staff_ID`) REFERENCES `staff` (`Staff_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registration`
--

LOCK TABLES `registration` WRITE;
/*!40000 ALTER TABLE `registration` DISABLE KEYS */;
INSERT INTO `registration` VALUES (1,'COR002',130001,'Registered','Completed'),(2,'COR002',130002,'Registered','Completed'),(3,'COR002',140001,'Registered','Completed'),(4,'COR002',140002,'Registered','Completed'),(5,'COR002',140003,'Rejected',''),(6,'COR002',140008,'Registered','OnGoing'),(7,'COR002',140025,'Registered','OnGoing'),(8,'COR002',140036,'Waitlist',''),(9,'COR002',140078,'Waitlist',''),(10,'COR002',140102,'Registered',''),(11,'COR002',140103,'Registered',''),(12,'COR002',140108,'Registered',''),(13,'COR002',140115,'Registered','Completed'),(14,'COR002',140525,'Rejected',''),(15,'COR002',140878,'Registered','Completed'),(16,'COR002',150075,'Registered','Completed'),(17,'COR002',150065,'Waitlist',''),(18,'COR002',150076,'Waitlist',''),(19,'COR002',150118,'Registered','Completed'),(20,'COR002',150142,'Registered','OnGoing'),(21,'COR002',150143,'Registered','OnGoing'),(22,'COR002',150148,'Registered',''),(23,'COR002',150155,'Rejected',''),(24,'COR002',150776,'Registered',''),(25,'COR002',150095,'Registered',''),(26,'COR002',150085,'Waitlist',''),(27,'COR002',150096,'Waitlist',''),(28,'COR002',150138,'Registered','Completed'),(29,'COR002',150162,'Registered','Completed'),(30,'COR002',150163,'Registered','Completed'),(31,'COR002',150168,'Registered','Completed'),(32,'COR002',150175,'Rejected',''),(33,'COR002',150796,'Registered','OnGoing'),(34,'COR002',150125,'Registered','OnGoing'),(35,'COR002',150115,'Waitlist',''),(36,'COR002',150126,'Waitlist',''),(37,'COR002',150192,'Registered',''),(38,'COR002',150193,'Registered',''),(39,'COR002',150198,'Registered',''),(40,'COR002',150205,'Registered','Completed'),(41,'COR002',150615,'Rejected',''),(42,'COR002',150968,'Registered','Completed'),(43,'COR002',150166,'Registered','Completed'),(44,'COR002',150208,'Waitlist',''),(45,'COR002',150232,'Waitlist',''),(46,'COR002',150233,'Registered','Completed'),(47,'COR002',150238,'Registered','OnGoing'),(48,'COR002',150245,'Registered','OnGoing'),(49,'COR002',150655,'Registered',''),(50,'COR002',150866,'Rejected',''),(51,'COR002',150215,'Registered',''),(52,'COR002',150258,'Registered',''),(53,'COR002',150282,'Waitlist',''),(54,'COR002',150283,'Waitlist',''),(55,'COR002',150288,'Registered','Completed'),(56,'COR002',150295,'Registered','Completed'),(57,'COR002',150705,'Registered','Completed'),(58,'COR002',150916,'Registered','Completed'),(59,'COR002',151058,'Rejected',''),(60,'COR002',150265,'Registered','OnGoing'),(61,'COR002',150318,'Registered','OnGoing'),(62,'COR002',150342,'Waitlist',''),(63,'COR002',150343,'Waitlist',''),(64,'COR002',150348,'Registered',''),(65,'COR002',150355,'Registered',''),(66,'COR002',150765,'Registered',''),(67,'COR002',150976,'Registered','Completed'),(68,'COR002',151118,'Rejected',''),(69,'COR002',150356,'Registered','Completed'),(70,'COR002',150422,'Registered','Completed'),(71,'COR002',150423,'Waitlist',''),(72,'COR002',150428,'Waitlist',''),(73,'COR002',150435,'Registered','Completed'),(74,'COR002',150845,'Registered','OnGoing'),(75,'COR002',151056,'Registered','OnGoing'),(76,'COR002',151198,'Registered',''),(77,'COR002',150445,'Rejected',''),(78,'COR002',150488,'Registered',''),(79,'COR002',150513,'Registered','Completed'),(80,'COR002',150518,'Waitlist',''),(81,'COR002',150525,'Waitlist',''),(82,'COR002',150935,'Registered','Completed'),(83,'COR002',151146,'Registered','Completed'),(84,'COR002',151288,'Registered','Completed'),(85,'COR002',150555,'Registered','OnGoing'),(86,'COR002',150566,'Rejected',''),(87,'COR002',150632,'Registered','OnGoing'),(88,'COR002',150638,'Registered',''),(89,'COR002',150645,'Waitlist',''),(90,'COR002',151055,'Waitlist',''),(91,'COR002',151266,'Registered',''),(92,'COR002',151408,'Registered',''),(93,'COR002',150695,'Registered','Completed'),(94,'COR002',160008,'Registered','Completed'),(95,'COR002',160075,'Rejected',''),(96,'COR002',160076,'Registered','Completed'),(97,'COR002',160142,'Registered','Completed'),(98,'COR002',160143,'Waitlist',''),(99,'COR002',160148,'Waitlist',''),(100,'COR002',160155,'Registered','OnGoing'),(101,'COR002',160145,'Registered','OnGoing'),(102,'COR002',160135,'Registered',''),(103,'COR002',160146,'Registered',''),(104,'COR002',160188,'Rejected',''),(105,'COR002',160213,'Registered',''),(106,'COR002',160225,'Registered','Completed'),(107,'COR002',160258,'Waitlist',''),(108,'COR002',160282,'Waitlist',''),(109,'COR002',151008,'Registered',''),(110,'COR002',150216,'Waitlist',''),(111,'SAL004',140001,'Registered','Completed'),(112,'SAL004',140002,'Registered','Completed'),(113,'SAL003',140003,'Registered','Completed'),(114,'SAL003',140004,'Registered','OnGoing'),(115,'SAL004',140008,'Rejected',''),(116,'SAL003',140025,'Registered','OnGoing'),(117,'SAL004',140078,'Registered',''),(118,'SAL004',140102,'Waitlist',''),(119,'SAL003',140103,'Waitlist',''),(120,'SAL003',140108,'Registered','Completed'),(121,'SAL004',140115,'Registered','Completed'),(122,'SAL004',140525,'Registered','Completed'),(123,'SAL003',140736,'Registered','OnGoing'),(124,'SAL003',140878,'Rejected',''),(125,'tch002',150075,'Registered',''),(126,'tch003',150065,'Waitlist',''),(127,'tch005',150118,'Registered','Completed'),(128,'tch001',150143,'Registered','Completed'),(129,'tch002',150148,'Registered','OnGoing'),(130,'tch003',150155,'Rejected',''),(131,'tch001',150095,'Waitlist',''),(132,'tch002',150085,'Waitlist',''),(133,'tch003',150096,'Registered','Completed'),(134,'tch005',150162,'Registered','Completed'),(135,'tch001',150168,'Rejected',''),(136,'tch005',150938,'Waitlist',''),(137,'tch001',150115,'Registered','Completed'),(138,'tch002',150126,'Registered','Completed'),(139,'tch003',150192,'Registered','Completed'),(140,'tch005',150198,'Rejected',''),(141,'tch002',150826,'Registered',''),(142,'tch003',150968,'Waitlist',''),(143,'tch005',150166,'Registered','Completed'),(144,'tch001',150232,'Registered','Completed'),(145,'tch002',150233,'Registered','OnGoing'),(146,'tch003',150238,'Rejected',''),(147,'tch001',151008,'Waitlist',''),(148,'tch002',150215,'Waitlist',''),(149,'tch003',150216,'Registered','Completed'),(150,'tch005',150282,'Registered','Completed'),(151,'tch001',150288,'Rejected',''),(152,'tch005',151058,'Waitlist',''),(153,'tch001',150265,'Registered','Completed'),(154,'tch002',150276,'Registered','Completed'),(155,'tch003',150318,'Registered','Completed'),(156,'tch005',150343,'Rejected',''),(157,'tch002',150765,'Registered',''),(158,'tch003',150976,'Waitlist',''),(159,'tch005',150345,'Registered','Completed'),(160,'tch001',150398,'Registered','Completed'),(161,'tch002',150422,'Registered','OnGoing'),(162,'tch003',150423,'Rejected',''),(163,'tch001',151056,'Waitlist',''),(164,'tch002',151198,'Waitlist',''),(165,'tch003',150445,'Registered','Completed'),(166,'tch005',150488,'Registered','Completed'),(167,'tch001',150513,'Rejected',''),(168,'tch005',151146,'Waitlist',''),(169,'tch001',150555,'Registered','Completed'),(170,'tch002',150566,'Registered','Completed'),(171,'tch003',150608,'Registered','Completed'),(172,'tch005',150633,'Rejected',''),(173,'tch002',151055,'Registered',''),(174,'tch003',151266,'Waitlist',''),(175,'tch005',150695,'Registered','Completed'),(176,'HRD001',160008,'Registered','Completed'),(177,'MGT001',160075,'Registered','Completed'),(178,'MGT002',160065,'Registered','Completed'),(179,'MGT004',160118,'Rejected',''),(180,'MGT001',160148,'Registered',''),(181,'MGT002',160155,'Waitlist',''),(182,'MGT004',160135,'Registered','Completed'),(183,'MGT007',160146,'Registered','Completed'),(184,'HRD001',160188,'Registered','Completed'),(185,'MGT001',160212,'Registered','OnGoing'),(186,'MGT002',160213,'Rejected',''),(187,'MGT007',160258,'Registered',''),(188,'MGT001',160282,'Waitlist',''),(189,'FIN001',150166,'Waitlist',''),(190,'FIN002',150208,'Registered','Completed'),(191,'FIN001',150232,'Registered','Completed'),(192,'FIN002',150233,'Registered','Completed'),(193,'FIN001',150238,'Registered','OnGoing'),(194,'FIN002',150245,'Rejected',''),(195,'FIN001',150655,'Waitlist',''),(196,'FIN002',150866,'Registered','Completed'),(197,'FIN001',151008,'Registered','Completed'),(198,'FIN002',150215,'Registered','Completed'),(199,'FIN001',150216,'Registered','OnGoing'),(200,'MGT001',140001,'Registered','Completed'),(201,'MGT001',150008,'Registered','Completed'),(202,'MGT001',150166,'Registered','Completed'),(203,'COR002',140004,'Registered','Completed'),(204,'COR002',140015,'Waitlist',''),(205,'COR002',140736,'Waitlist',''),(206,'COR002',150008,'Registered','Completed'),(207,'COR002',150565,'Registered',''),(208,'COR002',150918,'Registered',''),(209,'COR002',150585,'Registered','OnGoing'),(210,'COR002',150938,'Rejected',''),(211,'COR002',150826,'Rejected',''),(212,'COR002',150165,'Registered','OnGoing'),(213,'COR002',150275,'Waitlist',''),(214,'COR002',150276,'Registered','Completed'),(215,'COR002',150345,'Registered',''),(216,'COR002',150398,'Registered','Completed'),(217,'COR002',150446,'Registered',''),(218,'COR002',150512,'Registered',''),(219,'COR002',150608,'Registered','OnGoing'),(220,'COR002',150633,'Waitlist',''),(221,'COR002',160065,'Waitlist',''),(222,'SAL004',160118,'Registered','Completed'),(223,'SAL004',160142,'Registered','Completed'),(224,'SAL003',160143,'Registered','Completed'),(225,'SAL003',160148,'Registered','OnGoing'),(226,'SAL004',160155,'Rejected',''),(227,'SAL003',160145,'Registered',''),(228,'SAL004',160135,'Waitlist',''),(229,'SAL004',160146,'Registered','Completed'),(230,'SAL003',160188,'Registered','Completed'),(231,'SAL003',160212,'Registered','OnGoing'),(232,'SAL004',160213,'Rejected',''),(233,'SAL004',160218,'Waitlist',''),(234,'SAL003',160225,'Waitlist',''),(235,'SAL003',160258,'Registered','Completed'),(236,'tch002',160282,'Registered','Completed'),(237,'tch003',150166,'Rejected',''),(238,'tch005',150208,'Waitlist',''),(239,'tch001',150245,'Rejected',''),(240,'tch002',150655,'Registered',''),(241,'tch003',150866,'Waitlist',''),(242,'tch005',151008,'Registered','Completed'),(243,'tch001',150215,'Registered','Completed'),(244,'tch005',150216,'Registered','OnGoing'),(245,'COR001',130001,'Registered','Completed'),(246,'COR006',140001,'Waitlist',''),(247,'FIN001',140002,'Waitlist',''),(248,'FIN002',140003,'Registered','Completed'),(249,'FIN003',140004,'Registered','OnGoing'),(250,'HRD001',140008,'Registered','OnGoing'),(251,'MGT001',140015,'Registered',''),(252,'MGT002',140025,'Rejected',''),(253,'MGT004',140036,'Registered',''),(254,'MGT007',140078,'Registered','Completed'),(255,'SAL001',140102,'Waitlist',''),(256,'SAL004',140108,'Registered','Completed'),(257,'tch001',140115,'Registered','Completed'),(258,'tch002',140525,'Registered','Completed'),(259,'tch003',140736,'Registered','OnGoing'),(260,'tch005',140878,'Rejected',''),(261,'tch008',150008,'Registered','OnGoing'),(262,'tch012',150075,'Registered',''),(263,'tch013',150065,'Waitlist',''),(264,'tch014',150076,'Waitlist',''),(265,'tch015',150118,'Registered',''),(266,'tch018',150142,'Registered',''),(267,'tch019',150143,'Registered','Completed'),(268,'COR001',150148,'Registered','Completed'),(269,'COR006',150565,'Registered','Completed'),(270,'FIN001',150776,'Registered','Completed'),(271,'FIN002',150918,'Waitlist',''),(272,'FIN003',150095,'Waitlist',''),(273,'HRD001',150085,'Registered','OnGoing'),(274,'MGT001',150096,'Registered','OnGoing'),(275,'MGT002',150138,'Registered',''),(276,'MGT004',150162,'Registered',''),(277,'MGT007',150163,'Rejected',''),(278,'SAL001',150168,'Registered',''),(279,'SAL003',150175,'Registered','Completed'),(280,'SAL004',150585,'Waitlist',''),(281,'tch001',150796,'Waitlist',''),(282,'tch002',150938,'Registered','Completed'),(283,'tch003',150125,'Registered','Completed'),(284,'tch005',150115,'Registered','Completed'),(285,'tch008',150126,'Registered','OnGoing'),(286,'tch012',150192,'Rejected',''),(287,'tch013',150193,'Registered','OnGoing'),(288,'tch014',150198,'Registered',''),(289,'tch015',150205,'Waitlist',''),(290,'tch018',150615,'Waitlist',''),(291,'tch019',150826,'Registered','Completed'),(292,'COR001',150968,'Registered','Completed'),(293,'COR006',150166,'Registered','OnGoing'),(294,'FIN001',150208,'Rejected',''),(295,'FIN002',150232,'Registered','OnGoing'),(296,'FIN003',150233,'Registered',''),(297,'HRD001',150238,'Waitlist',''),(298,'MGT001',150245,'Waitlist',''),(299,'MGT002',150655,'Registered','Completed'),(300,'MGT004',150866,'Registered','Completed'),(301,'MGT007',151008,'Registered','Completed'),(302,'SAL001',150215,'Registered','OnGoing'),(303,'SAL003',150216,'Rejected',''),(304,'SAL004',150258,'Registered',''),(305,'tch001',150282,'Waitlist',''),(306,'tch002',150283,'Registered','Completed'),(307,'tch003',150288,'Registered','Completed'),(308,'tch005',150295,'Registered','OnGoing'),(309,'tch008',150705,'Rejected',''),(310,'tch012',150916,'Waitlist',''),(311,'tch013',151058,'Waitlist',''),(312,'tch014',150275,'Registered','Completed'),(313,'tch015',150265,'Registered','Completed'),(314,'tch018',150276,'Rejected',''),(315,'tch019',150318,'Waitlist',''),(316,'COR001',150342,'Registered','Completed'),(317,'COR006',150348,'Registered','Completed'),(318,'FIN001',150355,'Rejected',''),(319,'FIN002',150765,'Registered',''),(320,'FIN003',150976,'Waitlist',''),(321,'HRD001',151118,'Registered','Completed'),(322,'MGT001',150345,'Registered','Completed'),(323,'MGT002',150356,'Registered','OnGoing'),(324,'MGT004',150398,'Registered','Completed'),(325,'MGT007',150422,'Registered','Completed'),(326,'SAL001',150423,'Waitlist',''),(327,'SAL003',150428,'Waitlist',''),(328,'SAL004',150435,'Registered','Completed'),(329,'tch001',150845,'Registered','OnGoing'),(330,'tch002',151056,'Registered','OnGoing'),(331,'tch003',151198,'Registered',''),(332,'tch005',150445,'Rejected',''),(333,'tch008',150446,'Registered',''),(334,'tch012',150488,'Registered','Completed'),(335,'tch013',150512,'Waitlist',''),(336,'tch014',150513,'Waitlist',''),(337,'tch015',150518,'Registered','Completed'),(338,'tch018',150525,'Registered','Completed'),(339,'tch019',150935,'Registered','Completed'),(340,'COR001',151146,'Registered','OnGoing'),(341,'COR006',150555,'Registered','OnGoing'),(342,'FIN001',150566,'Registered',''),(343,'FIN002',150608,'Waitlist',''),(344,'FIN003',150632,'Waitlist',''),(345,'HRD001',150633,'Registered',''),(346,'MGT001',150638,'Registered',''),(347,'MGT002',150645,'Registered','Completed'),(348,'MGT004',151055,'Registered','Completed'),(349,'MGT007',151266,'Rejected',''),(350,'SAL001',151408,'Registered','Completed'),(351,'SAL003',150695,'Registered','Completed'),(352,'SAL004',160008,'Waitlist',''),(353,'tch001',160075,'Waitlist',''),(354,'tch002',160065,'Registered','OnGoing'),(355,'tch003',160076,'Registered','OnGoing'),(356,'tch005',160118,'Registered',''),(357,'tch008',160142,'Registered',''),(358,'tch012',160143,'Rejected',''),(359,'tch013',160148,'Registered',''),(360,'tch014',160155,'Registered','Completed'),(361,'tch015',160145,'Waitlist',''),(362,'tch018',160135,'Waitlist',''),(363,'tch019',160146,'Registered','Completed'),(364,'COR001',160188,'Registered','Completed'),(365,'COR002',160212,'Registered','Completed'),(366,'COR006',160213,'Registered','OnGoing'),(367,'FIN001',160218,'Rejected',''),(368,'FIN002',160225,'Registered','OnGoing'),(369,'FIN003',160258,'Registered',''),(370,'HRD001',160282,'Waitlist',''),(371,'MGT002',150208,'Registered','Completed'),(372,'MGT004',150232,'Registered','Completed'),(373,'MGT007',150233,'Registered','Completed'),(374,'SAL001',150238,'Registered','OnGoing'),(375,'SAL003',150245,'Rejected',''),(376,'SAL004',150655,'Registered','OnGoing'),(377,'tch001',150866,'Registered',''),(378,'tch002',151008,'Waitlist',''),(379,'tch003',150215,'Waitlist','');
/*!40000 ALTER TABLE `registration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `skill`
--

DROP TABLE IF EXISTS `skill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `skill` (
  `Skill_ID` int NOT NULL AUTO_INCREMENT,
  `Skill_Name` varchar(50) NOT NULL,
  `Skill_Description` varchar(255) NOT NULL,
  `Skill_type` varchar(20) DEFAULT NULL,
  `Status` varchar(20) DEFAULT NULL,
  `Created_Date` date DEFAULT NULL,
  PRIMARY KEY (`Skill_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skill`
--

LOCK TABLES `skill` WRITE;
/*!40000 ALTER TABLE `skill` DISABLE KEYS */;
INSERT INTO `skill` VALUES (1,'Software Development','Develop Software','Hard Skill','Active','2022-10-27'),(2,'Scrum','Master of Scrum','Soft Skill','Inactive','2022-11-05'),(3,'Human Resources','Human resources is the set of people who make up the workforce of an organization, business sector, industry, or economy.','Soft Skill','Active','2022-11-05'),(7,'Ethical Hacking','Ethical hacking is a process of detecting vulnerabilities in an application, system, or organization’s infrastructure that an attacker can use to exploit an individual or organization.','Hard Skill','Active','2022-11-05'),(21,'Sales','Ability to sell','Soft Skill','Active','2022-11-05'),(22,'Incident Response','Respond to incidents','Hard Skill','Active','2022-11-05'),(23,'Root Cause Analysis','Find the root cause of the incident/problem','Hard Skill','Active','2022-11-05'),(24,'Cloud Engineering','Engineer Cloud solutions','Hard Skill','Active','2022-11-05');
/*!40000 ALTER TABLE `skill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff` (
  `Staff_ID` int NOT NULL,
  `Staff_FName` varchar(50) NOT NULL,
  `Staff_LName` varchar(50) NOT NULL,
  `Dept` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `System_Role` int NOT NULL,
  PRIMARY KEY (`Staff_ID`),
  KEY `system_role_fk` (`System_Role`),
  CONSTRAINT `system_role_fk` FOREIGN KEY (`System_Role`) REFERENCES `system_role` (`Role_ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
INSERT INTO `staff` VALUES (130001,'John','Sim','Chariman','jack.sim@allinone.com.sg',1),(130002,'Jack','Sim','CEO','jack.sim@allinone.com.sg',1),(140001,'Derek','Tan','Sales','Derek.Tan@allinone.com.sg',3),(140002,'Susan','Goh','Sales','Susan.Goh@allinone.com.sg',2),(140003,'Janice','Chan','Sales','Janice.Chan@allinone.com.sg',2),(140004,'Mary','Teo','Sales','Mary.Teo@allinone.com.sg',2),(140008,'Jaclyn','Lee','Sales','Jaclyn.Lee@allinone.com.sg',2),(140015,'Oliva','Lim','Sales','Oliva.Lim@allinone.com.sg',2),(140025,'Emma','Heng','Sales','Emma.Heng@allinone.com.sg',2),(140036,'Charlotte','Wong','Sales','Charlotte.Wong@allinone.com.sg',2),(140078,'Amelia','Ong','Sales','Amelia.Ong@allinone.com.sg',2),(140102,'Eva','Yong','Sales','Eva.Yong@allinone.com.sg',2),(140103,'Sophia','Toh','Sales','Sophia.Toh@allinone.com.sg',2),(140108,'Liam','The','Sales','Liam.The@allinone.com.sg',2),(140115,'Noah','Ng','Sales','Noah.Ng@allinone.com.sg',2),(140525,'Oliver','Tan','Sales','Oliver.Tan@allinone.com.sg',2),(140736,'William','Fu','Sales','William.Fu@allinone.com.sg',2),(140878,'James','Tong','Sales','James.Tong@allinone.com.sg',2),(150008,'Eric','Loh','Ops','Eric.Loh@allinone.com.sg',3),(150065,'Noah','Goh','Ops','Noah.Goh@allinone.com.sg',4),(150075,'Liam','Tan','Ops','Liam.Tan@allinone.com.sg',4),(150076,'Oliver','Chan','Ops','Oliver.Chan@allinone.com.sg',4),(150085,'Michael','Ng','Ops','Michael.Ng@allinone.com.sg',4),(150095,'Alexander','The','Ops','Alexander.The@allinone.com.sg',4),(150096,'Ethan','Tan','Ops','Ethan.Tan@allinone.com.sg',4),(150115,'Jaclyn','Lee','Ops','Jaclyn.Lee@allinone.com.sg',4),(150118,'William','Teo','Ops','William.Teo@allinone.com.sg',4),(150125,'Mary','Teo','Ops','Mary.Teo@allinone.com.sg',4),(150126,'Oliva','Lim','Ops','Oliva.Lim@allinone.com.sg',2),(150138,'Daniel','Fu','Ops','Daniel.Fu@allinone.com.sg',4),(150142,'James','Lee','Ops','James.Lee@allinone.com.sg',4),(150143,'John','Lim','Ops','John.Lim@allinone.com.sg',4),(150148,'Jack','Heng','Ops','Jack.Heng@allinone.com.sg',4),(150155,'Derek','Wong','Ops','Derek.Wong@allinone.com.sg',4),(150162,'Jacob','Tong','Ops','Jacob.Tong@allinone.com.sg',4),(150163,'Logan','Loh','Ops','Logan.Loh@allinone.com.sg',4),(150165,'Oliver','Tan','Ops','Oliver.Tan@allinone.com.sg',2),(150166,'William','Fu','Ops','William.Fu@allinone.com.sg',2),(150168,'Jackson','Tan','Ops','Jackson.Tan@allinone.com.sg',4),(150175,'Aiden','Tan','Ops','Aiden.Tan@allinone.com.sg',4),(150192,'Emma','Heng','Ops','Emma.Heng@allinone.com.sg',2),(150193,'Charlotte','Wong','Ops','Charlotte.Wong@allinone.com.sg',2),(150198,'Amelia','Ong','Ops','Amelia.Ong@allinone.com.sg',2),(150205,'Eva','Yong','Ops','Eva.Yong@allinone.com.sg',2),(150208,'James','Tong','Ops','James.Tong@allinone.com.sg',2),(150215,'Michael','Lee','Ops','Michael.Lee@allinone.com.sg',2),(150216,'Ethan','Lim','Ops','Ethan.Lim@allinone.com.sg',2),(150232,'John','Loh','Ops','John.Loh@allinone.com.sg',2),(150233,'Jack','Tan','Ops','Jack.Tan@allinone.com.sg',2),(150238,'Derek','Tan','Ops','Derek.Tan@allinone.com.sg',2),(150245,'Benjamin','Tan','Ops','Benjamin.Tan@allinone.com.sg',2),(150258,'Daniel','Heng','Ops','Daniel.Heng@allinone.com.sg',2),(150265,'Jaclyn','Tong','Ops','Jaclyn.Tong@allinone.com.sg',2),(150275,'Mary','Fu','Ops','Mary.Fu@allinone.com.sg',2),(150276,'Oliva','Loh','Ops','Oliva.Loh@allinone.com.sg',2),(150282,'Jacob','Wong','Ops','Jacob.Wong@allinone.com.sg',2),(150283,'Logan','Ong','Ops','Logan.Ong@allinone.com.sg',2),(150288,'Jackson','Yong','Ops','Jackson.Yong@allinone.com.sg',2),(150295,'Aiden','Toh','Ops','Aiden.Toh@allinone.com.sg',2),(150318,'Emma','Tan','Ops','Emma.Tan@allinone.com.sg',2),(150342,'Charlotte','Tan','Ops','Charlotte.Tan@allinone.com.sg',2),(150343,'Amelia','Tan','Ops','Amelia.Tan@allinone.com.sg',2),(150345,'William','Heng','Ops','William.Heng@allinone.com.sg',2),(150348,'Eva','Goh','Ops','Eva.Goh@allinone.com.sg',2),(150355,'Sophia','Chan','Ops','Sophia.Chan@allinone.com.sg',2),(150356,'James','Wong','Ops','James.Wong@allinone.com.sg',2),(150398,'John','Ong','Ops','John.Ong@allinone.com.sg',2),(150422,'Jack','Yong','Ops','Jack.Yong@allinone.com.sg',2),(150423,'Derek','Toh','Ops','Derek.Toh@allinone.com.sg',2),(150428,'Benjamin','The','Ops','Benjamin.The@allinone.com.sg',2),(150435,'Lucas','Ng','Ops','Lucas.Ng@allinone.com.sg',2),(150445,'Ethan','Loh','Ops','Ethan.Loh@allinone.com.sg',2),(150446,'Daniel','Tan','Ops','Daniel.Tan@allinone.com.sg',2),(150488,'Jacob','Tan','Ops','Jacob.Tan@allinone.com.sg',2),(150512,'Logan','Tan','Ops','Logan.Tan@allinone.com.sg',2),(150513,'Jackson','Goh','Ops','Jackson.Goh@allinone.com.sg',2),(150518,'Aiden','Chan','Ops','Aiden.Chan@allinone.com.sg',2),(150525,'Samuel','Teo','Ops','Samuel.Teo@allinone.com.sg',2),(150555,'Jaclyn','Wong','Ops','Jaclyn.Wong@allinone.com.sg',2),(150565,'Benjamin','Ong','Ops','Benjamin.Ong@allinone.com.sg',4),(150566,'Oliva','Ong','Ops','Oliva.Ong@allinone.com.sg',2),(150585,'Samuel','Tan','Ops','Samuel.Tan@allinone.com.sg',4),(150608,'Emma','Yong','Ops','Emma.Yong@allinone.com.sg',2),(150615,'Sophia','Toh','Ops','Sophia.Toh@allinone.com.sg',2),(150632,'Charlotte','Toh','Ops','Charlotte.Toh@allinone.com.sg',2),(150633,'Amelia','The','Ops','Amelia.The@allinone.com.sg',2),(150638,'Eva','Ng','Ops','Eva.Ng@allinone.com.sg',2),(150645,'Sophia','Tan','Ops','Sophia.Tan@allinone.com.sg',2),(150655,'Lucas','Goh','Ops','Lucas.Goh@allinone.com.sg',2),(150695,'William','Tan','Ops','William.Tan@allinone.com.sg',2),(150705,'Samuel','The','Ops','Samuel.The@allinone.com.sg',2),(150765,'Liam','Teo','Ops','Liam.Teo@allinone.com.sg',2),(150776,'Lucas','Yong','Ops','Lucas.Yong@allinone.com.sg',4),(150796,'Susan','Goh','Ops','Susan.Goh@allinone.com.sg',4),(150826,'Liam','The','Ops','Liam.The@allinone.com.sg',2),(150845,'Henry','Tan','Ops','Henry.Tan@allinone.com.sg',2),(150866,'Henry','Chan','Ops','Henry.Chan@allinone.com.sg',2),(150916,'Susan','Ng','Ops','Susan.Ng@allinone.com.sg',2),(150918,'Henry','Toh','Ops','Henry.Toh@allinone.com.sg',4),(150935,'Susan','Lee','Ops','Susan.Lee@allinone.com.sg',2),(150938,'Janice','Chan','Ops','Janice.Chan@allinone.com.sg',4),(150968,'Noah','Ng','Ops','Noah.Ng@allinone.com.sg',2),(150976,'Noah','Lee','Ops','Noah.Lee@allinone.com.sg',2),(151008,'Alexander','Teo','Ops','Alexander.Teo@allinone.com.sg',2),(151055,'Liam','Fu','Ops','Liam.Fu@allinone.com.sg',2),(151056,'Alexander','Fu','Ops','Alexander.Fu@allinone.com.sg',2),(151058,'Janice','Tan','Ops','Janice.Tan@allinone.com.sg',2),(151118,'Oliver','Lim','Ops','Oliver.Lim@allinone.com.sg',2),(151146,'Janice','Lim','Ops','Janice.Lim@allinone.com.sg',2),(151198,'Michael','Tong','Ops','Michael.Tong@allinone.com.sg',2),(151266,'Noah','Tong','Ops','Noah.Tong@allinone.com.sg',2),(151288,'Mary','Heng','Ops','Mary.Heng@allinone.com.sg',2),(151408,'Oliver','Loh','Ops','Oliver.Loh@allinone.com.sg',2),(160008,'Sally','Loh','HR','Sally.Loh@allinone.com.sg',1),(160065,'John','Tan','HR','John.Tan@allinone.com.sg',1),(160075,'James','Tan','HR','James.Tan@allinone.com.sg',1),(160076,'Jack','Goh','HR','Jack.Goh@allinone.com.sg',1),(160118,'Derek','Chan','HR','Derek.Chan@allinone.com.sg',1),(160135,'Jaclyn','Ong','HR','Jaclyn.Ong@allinone.com.sg',2),(160142,'Benjamin','Teo','HR','Benjamin.Teo@allinone.com.sg',1),(160143,'Lucas','Lee','HR','Lucas.Lee@allinone.com.sg',1),(160145,'Mary','Wong','HR','Mary.Wong@allinone.com.sg',2),(160146,'Oliva','Yong','HR','Oliva.Yong@allinone.com.sg',2),(160148,'Henry','Lim','HR','Henry.Lim@allinone.com.sg',1),(160155,'Alexander','Heng','HR','Alexander.Heng@allinone.com.sg',1),(160188,'Emma','Toh','HR','Emma.Toh@allinone.com.sg',2),(160212,'Charlotte','The','HR','Charlotte.The@allinone.com.sg',2),(160213,'Amelia','Ng','HR','Amelia.Ng@allinone.com.sg',2),(160218,'Eva','Tan','HR','Eva.Tan@allinone.com.sg',2),(160225,'Sophia','Fu','HR','Sophia.Fu@allinone.com.sg',2),(160258,'Michael','Tong','HR','Michael.Tong@allinone.com.sg',2),(160282,'Ethan','Loh','HR','Ethan.Loh@allinone.com.sg',2),(170166,'David','Yap','Finance','David.Yap@allinone.com.sg',3),(170208,'Daniel','Tan','Finance','Daniel.Tan@allinone.com.sg',2),(170215,'Mary','Wong','Finance','Mary.Wong@allinone.com.sg',2),(170216,'Jaclyn','Ong','Finance','Jaclyn.Ong@allinone.com.sg',2),(170232,'Jacob','Tan','Finance','Jacob.Tan@allinone.com.sg',2),(170233,'Logan','Goh','Finance','Logan.Goh@allinone.com.sg',2),(170238,'Jackson','Chan','Finance','Jackson.Chan@allinone.com.sg',2),(170245,'Aiden','Teo','Finance','Aiden.Teo@allinone.com.sg',2),(170655,'Samuel','Lee','Finance','Samuel.Lee@allinone.com.sg',2),(170866,'Susan','Lim','Finance','Susan.Lim@allinone.com.sg',2),(171008,'Janice','Heng','Finance','Janice.Heng@allinone.com.sg',2);
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_role`
--

DROP TABLE IF EXISTS `system_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_role` (
  `Role_ID` int NOT NULL,
  `Role_Name` varchar(50) NOT NULL,
  PRIMARY KEY (`Role_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_role`
--

LOCK TABLES `system_role` WRITE;
/*!40000 ALTER TABLE `system_role` DISABLE KEYS */;
INSERT INTO `system_role` VALUES (1,'Admin'),(2,'User'),(3,'Manager'),(4,'Trainer');
/*!40000 ALTER TABLE `system_role` ENABLE KEYS */;
UNLOCK TABLES;
-- SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
-- /*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-06  0:01:39
