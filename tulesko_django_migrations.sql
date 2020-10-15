-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: tulesko
-- ------------------------------------------------------
-- Server version	8.0.19

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

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-05-19 18:26:34.460899'),(2,'auth','0001_initial','2020-05-19 18:28:17.635800'),(3,'admin','0001_initial','2020-05-19 18:33:13.264709'),(4,'admin','0002_logentry_remove_auto_add','2020-05-19 18:34:36.950496'),(5,'admin','0003_logentry_add_action_flag_choices','2020-05-19 18:34:38.058559'),(6,'contenttypes','0002_remove_content_type_name','2020-05-19 18:35:35.452842'),(7,'auth','0002_alter_permission_name_max_length','2020-05-19 18:36:24.514648'),(8,'auth','0003_alter_user_email_max_length','2020-05-19 18:36:36.497334'),(9,'auth','0004_alter_user_username_opts','2020-05-19 18:36:38.725461'),(10,'auth','0005_alter_user_last_login_null','2020-05-19 18:37:05.224977'),(11,'auth','0006_require_contenttypes_0002','2020-05-19 18:37:06.728063'),(12,'auth','0007_alter_validators_add_error_messages','2020-05-19 18:37:08.260150'),(13,'auth','0008_alter_user_username_max_length','2020-05-19 18:37:44.900246'),(14,'auth','0009_alter_user_last_name_max_length','2020-05-19 18:38:19.069200'),(15,'auth','0010_alter_group_name_max_length','2020-05-19 18:38:25.188550'),(16,'auth','0011_update_proxy_permissions','2020-05-19 18:38:26.663635'),(17,'sessions','0001_initial','2020-05-19 18:38:39.833388'),(18,'travel','0001_initial','2020-05-19 18:39:09.309074'),(19,'travel','0002_destination_price','2020-05-19 22:14:53.980153'),(20,'library','0001_initial','2020-06-10 20:27:43.528766'),(21,'library','0002_auto_20200610_2119','2020-06-10 20:28:11.821384'),(22,'library','0003_auto_20200611_2207','2020-06-11 21:14:57.268305'),(23,'library','0004_auto_20200612_1556','2020-06-12 15:00:16.016661');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-30 22:57:22
