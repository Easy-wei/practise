# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.32)
# Database: global_data
# Generation Time: 2021-09-11 15:36:31 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table distros
# ------------------------------------------------------------

DROP TABLE IF EXISTS `distros`;

CREATE TABLE `distros` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `school_id` varchar(32) DEFAULT NULL,
  `mail_domains` varchar(128) DEFAULT '[]',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `distros` WRITE;
/*!40000 ALTER TABLE `distros` DISABLE KEYS */;

INSERT INTO `distros` (`id`, `school_id`, `mail_domains`)
VALUES
	(1,'ningbo','[]'),
	(2,'ningbo_sfv','[]'),
	(3,'qidi','[]'),
	(4,'so1','[]'),
	(5,'wuxi','[]'),
	(6,'uk','[]');

/*!40000 ALTER TABLE `distros` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

SELECT 

table_name 

FROM

information_schema.tables 

WHERE table_schema = 'env_qidi' 

AND table_type = 'base table' 

 
+---------------------------------+
| table_name                      |
+---------------------------------+
| academic_plans                  |
| campuses                        |
| class_assignment_request        |
| classes                         |
| classrooms                      |
| dormitories                     |
| dormitory_students              |
| exam_price_changes              |
| exams                           |
| file_structures                 |
| file_student_uploads            |
| file_uploads                    |
| group_rights                    |
| interactive_test_answers        |
| interactive_test_assigned       |
| interactive_test_data           |
| interactive_tests               |
| lessons                         |
| log                             |
| news_links                      |
| notifications                   |
| pages                           |
| parent_students                 |
| parents                         |
| pay_models                      |
| profiles                        |
| public_exam_account             |
| public_exam_signups             |
| self_signup_classes             |
| settings                        |
| settings_design                 |
| settings_editable               |
| staff                           |
| staff_groups                    |
| student_attendance              |
| student_classes                 |
| student_complaints              |
| student_credit                  |
| student_exams                   |
| student_feedback_form           |
| student_feedback_form_topics    |
| student_feedback_lesson_comment |
| student_signup_form             |
| student_signups                 |
| students                        |
| students_sales                  |
| subject_books                   |
| subjects                        |
| survey_answers                  |
| survey_assigned                 |
| survey_data                     |
| surveys                         |
| teacher_default_schedule        |
| teacher_feedback                |
| teacher_schedule                |
| test_groups                     |
| tests                           |
| textbook_purchases              |
| textbooks                       |
| topic_content                   |
| topics                          |
+------------------