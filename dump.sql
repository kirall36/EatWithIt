CREATE DATABASE  IF NOT EXISTS `eatwithit2` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `eatwithit2`;
-- MySQL dump 10.13  Distrib 8.0.16, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: eatwithit2
-- ------------------------------------------------------
-- Server version	8.0.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `incompatibleproducts`
--

DROP TABLE IF EXISTS `incompatibleproducts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `incompatibleproducts` (
  `id_product1` int(11) NOT NULL,
  `id_product2` int(11) NOT NULL,
  PRIMARY KEY (`id_product1`,`id_product2`),
  KEY `product2_key_idx` (`id_product2`),
  CONSTRAINT `product1_key` FOREIGN KEY (`id_product1`) REFERENCES `products` (`idproducts`),
  CONSTRAINT `product2_key` FOREIGN KEY (`id_product2`) REFERENCES `products` (`idproducts`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `incompatibleproducts`
--

LOCK TABLES `incompatibleproducts` WRITE;
/*!40000 ALTER TABLE `incompatibleproducts` DISABLE KEYS */;
INSERT INTO `incompatibleproducts` VALUES (8,1),(8,2),(7,11),(16,11),(17,11),(18,11),(19,11),(20,11),(21,11),(22,11),(3,19),(28,23),(31,23),(28,24),(31,24),(28,25),(31,25),(28,26),(31,26),(8,28),(8,31),(6,37),(7,41),(16,41),(17,41),(18,41),(19,41),(20,41),(21,41),(22,41),(42,45),(43,45),(8,46),(8,47),(46,47),(8,48),(46,48),(8,49);
/*!40000 ALTER TABLE `incompatibleproducts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `meal`
--

DROP TABLE IF EXISTS `meal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `meal` (
  `id_meal` int(11) NOT NULL AUTO_INCREMENT,
  `meal_type` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `product_id` int(11) NOT NULL,
  `weight` double NOT NULL,
  `carbs` double DEFAULT NULL,
  `fats` double DEFAULT NULL,
  `proteins` double DEFAULT NULL,
  `calories` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_meal`),
  KEY `product_key_idx` (`product_id`),
  CONSTRAINT `product_key` FOREIGN KEY (`product_id`) REFERENCES `products` (`idproducts`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meal`
--

LOCK TABLES `meal` WRITE;
/*!40000 ALTER TABLE `meal` DISABLE KEYS */;
INSERT INTO `meal` VALUES (5,'breakfast',1,200,21,0,1.8,92),(7,'dinner',19,240,1.92,20.64,48.96,386),(9,'breakfast',42,50,24.75,0.3,2.35,105),(11,'breakfast',11,120,12.24,73.56,16.56,777);
/*!40000 ALTER TABLE `meal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `meals_in_ration`
--

DROP TABLE IF EXISTS `meals_in_ration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `meals_in_ration` (
  `id_meal` int(11) NOT NULL,
  `id_ration` int(11) NOT NULL,
  PRIMARY KEY (`id_meal`,`id_ration`),
  KEY `ration_key_idx` (`id_ration`),
  CONSTRAINT `meal_key` FOREIGN KEY (`id_meal`) REFERENCES `meal` (`id_meal`),
  CONSTRAINT `ration_key` FOREIGN KEY (`id_ration`) REFERENCES `ration` (`id_ration`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meals_in_ration`
--

LOCK TABLES `meals_in_ration` WRITE;
/*!40000 ALTER TABLE `meals_in_ration` DISABLE KEYS */;
INSERT INTO `meals_in_ration` VALUES (5,1),(7,1),(9,3),(11,3);
/*!40000 ALTER TABLE `meals_in_ration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `products` (
  `idproducts` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `calories` int(11) NOT NULL,
  `proteins` double NOT NULL,
  `fats` double NOT NULL,
  `carbs` double NOT NULL,
  PRIMARY KEY (`idproducts`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'Абрикосы',46,0.9,0,10.5),(2,'Авокадо',223,1.9,23.5,6.7),(3,'Картофель',83,2,0.1,19.7),(4,'Кабачки',27,0.6,0.3,5.7),(5,'Банан',91,1.5,0,22.4),(6,'Яйцо куриное',157,12.7,11.5,0.7),(7,'Говядина',187,18.9,12.4,0),(8,'Молоко',58,2.8,3.2,4.7),(9,'Геркулес',355,13.1,6.2,55.7),(10,'Сахар',399,0,0,99.8),(11,'Грецкий орех',648,13.8,61.3,10.2),(12,'Зефир',299,0.8,0,78.3),(13,'Сыр',371,23.4,30,0),(14,'Докторская колбаса',260,13.7,22.8,0),(15,'Сардельки говяжьи',215,11.1,18.2,1.6),(16,'Баранина',201,16.2,15.3,0),(17,'Индейка',192,21.1,12.3,0.6),(18,'Кролик',197,20.6,12.8,0),(19,'Курица',161,20.4,8.6,0.8),(20,'Свинина',484,11.6,49.1,0),(21,'Сосиски молочные',260,11.3,23.9,1.1),(22,'Сосиски куриные',242,10.6,22.1,3.3),(23,'Майонез',624,3.3,67,2.4),(24,'Масло оливковое',898,0,99.8,0),(25,'Масло сливочное',747,0.5,82.5,1),(26,'Масло подсолнечное',899,0,99.9,0),(27,'Кальмары',100,18,2.2,2),(28,'Карась',84,17.5,1.6,0),(29,'Креветки',98,20.5,1.6,0.3),(30,'Крабовые палочки',73,17.9,2.1,0),(31,'Сельдь',248,17.7,19.5,0),(32,'Пломбир',232,3.7,15,24),(33,'Творог',169,18,9,3),(34,'Йогурт',87,5,3.2,8.5),(35,'Кефир',53,2.9,2.5,4),(36,'Огурец',14,0.8,0.1,0.5),(37,'Помидор',24,1.1,0.2,3.8),(38,'Сельдерей',34,1.3,0.3,6.5),(39,'Тыква',22,1,0.1,4.4),(40,'Свекла',42,1.5,0.1,8.8),(41,'Фасоль',298,21,2,47),(42,'Хлеб',210,4.7,0.6,49.5),(43,'Батон',261,9.4,2.7,50.7),(44,'Мед',312,0.6,0,80.5),(45,'Варенье',278,0.4,0.1,69),(46,'Вино ',83,0.1,0,2.7),(47,'Апельсин',43,0.9,0.2,8.1),(48,'Мандарин',38,0.8,0.2,7.5),(49,'Яблоко',47,0.4,0.4,9.8),(50,'Шоколад',552,6.7,35.6,52.4);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ration`
--

DROP TABLE IF EXISTS `ration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `ration` (
  `id_ration` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `carbs` double DEFAULT NULL,
  `proteins` double DEFAULT NULL,
  `fats` double DEFAULT NULL,
  `calories` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_ration`),
  KEY `user_key_idx` (`user_id`),
  CONSTRAINT `user_key` FOREIGN KEY (`user_id`) REFERENCES `user` (`id_user`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ration`
--

LOCK TABLES `ration` WRITE;
/*!40000 ALTER TABLE `ration` DISABLE KEYS */;
INSERT INTO `ration` VALUES (1,17,'2019-06-04',22.92,50.76,20.64,478),(3,20,'2019-06-04',36.99,18.91,73.86,882);
/*!40000 ALTER TABLE `ration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `user` (
  `id_user` int(11) NOT NULL AUTO_INCREMENT,
  `role` varchar(20) NOT NULL,
  `name` varchar(200) NOT NULL,
  `login` varchar(50) NOT NULL,
  `password` varchar(200) NOT NULL,
  `weight` double NOT NULL,
  `hight` double NOT NULL,
  `activityLevel` varchar(80) NOT NULL,
  `diet` varchar(50) NOT NULL DEFAULT 'wl',
  `caloriesRecomendation` double NOT NULL DEFAULT '2000',
  `sex` varchar(4) NOT NULL,
  `birth_date` date NOT NULL,
  PRIMARY KEY (`id_user`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (10,'User','Kroshka Du','kate3','$5$rounds=535000$CZQbjTPb50psbhqD$AyjY9WIOBd6DzzmaJFrEqojyL2LsdYGwU/Ldv0jFqf1',52,165,'high','wl',1300,'f','1998-03-30'),(16,'Vip','Kirill','kirall36','$5$rounds=535000$inQHLJ26z2etW/ed$MWw37gXY3BBECHHEfye9WhA9balcyiZZ.TTMrWYS/C3',65,172,'high','wl',2249,'m','1998-06-15'),(17,'Vip','kir','kir2','$5$rounds=535000$CUQx8y9sNCAJy/AX$3L046jkmu1HBXkj7bEFXT9LunKi2ZFUzAvbrQ2M0gsA',62,173,'medium','wm',2490,'m','1998-06-15'),(18,'User','test','tesrt','$5$rounds=535000$Dh.Oau8D8fdewVqr$MOSHVVZAdgDyhHu0lx66Sf8T3mBohXMyQqWu1ofW188',77,172,'medium','wm',2728,'m','2000-07-18'),(20,'User','Test User','user','$5$rounds=535000$BDBxJG2.f1Hgrp35$c7wF5zl1O/ESSvOeXdWIFHFi.envINgE3OP7vvEUxq8',65,172,'medium','wm',2526,'m','1998-06-14');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-04  7:58:39
