-- MySQL dump 10.13  Distrib 8.0.17, for macos10.14 (x86_64)
--
-- Host: localhost    Database: imdbnew
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
-- Table structure for table `name_basics`
--

DROP TABLE IF EXISTS `name_basics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `name_basics` (
  `nconst` varchar(128) DEFAULT NULL,
  `primary_name` varchar(128) DEFAULT NULL,
  `birth_year` varchar(45) DEFAULT NULL,
  `death_year` varchar(45) DEFAULT NULL,
  `primary_profession` varchar(128) DEFAULT NULL,
  `known_for_titles` varchar(128) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `title_akas`
--

DROP TABLE IF EXISTS `title_akas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `title_akas` (
  `titleid` varchar(128) DEFAULT NULL,
  `ordering` varchar(128) DEFAULT NULL,
  `title` text,
  `region` varchar(128) DEFAULT NULL,
  `language` varchar(128) DEFAULT NULL,
  `types` varchar(512) DEFAULT NULL,
  `attributes` varchar(512) DEFAULT NULL,
  `is_original` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `title_basics`
--

DROP TABLE IF EXISTS `title_basics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `title_basics` (
  `tconst` varchar(64) NOT NULL,
  `ttype` varchar(64) DEFAULT NULL,
  `primary_title` varchar(512) DEFAULT NULL,
  `original_title` varchar(512) DEFAULT NULL,
  `is_adult` varchar(32) DEFAULT NULL,
  `start_year` varchar(45) DEFAULT NULL,
  `end_year` varchar(45) DEFAULT NULL,
  `runtime` varchar(45) DEFAULT NULL,
  `genres` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`tconst`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `title_crew`
--

DROP TABLE IF EXISTS `title_crew`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `title_crew` (
  `tconst` varchar(128) DEFAULT NULL,
  `directors` text,
  `writer` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `title_episode`
--

DROP TABLE IF EXISTS `title_episode`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `title_episode` (
  `tconst` varchar(128) NOT NULL,
  `parent` varchar(128) DEFAULT NULL,
  `season_number` text,
  `episode_number` text,
  PRIMARY KEY (`tconst`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `title_principals`
--

DROP TABLE IF EXISTS `title_principals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `title_principals` (
  `tconst` varchar(128) DEFAULT NULL,
  `ordering` varchar(45) DEFAULT NULL,
  `nconst` varchar(128) DEFAULT NULL,
  `category` text,
  `job` text,
  `characters` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `title_ratings`
--

DROP TABLE IF EXISTS `title_ratings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `title_ratings` (
  `tconst` varchar(128) NOT NULL,
  `rating` varchar(45) DEFAULT NULL,
  `votes` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`tconst`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping routines for database 'imdbnew'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-29 10:25:16