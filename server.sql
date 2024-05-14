/*
Navicat MySQL Data Transfer

Source Server         : localhost_3316
Source Server Version : 80033
Source Host           : localhost:3306
Source Database       : comp3030j

Target Server Type    : MYSQL
Target Server Version : 80033
File Encoding         : 65001

Date: 2024-05-14 14:34:52
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `drivers`
-- ----------------------------
DROP TABLE IF EXISTS `drivers`;
CREATE TABLE `drivers` (
  `driver_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `total_mileage` decimal(10,2) NOT NULL DEFAULT '0.00',
  `total_emission` decimal(10,2) NOT NULL DEFAULT '0.00',
  `orders_count` int NOT NULL DEFAULT '0',
  `status` enum('AVAILABLE','UNAVAILABLE') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`driver_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of drivers
-- ----------------------------
INSERT INTO `drivers` VALUES ('1', 'hou', '0.00', '0.00', '0', 'AVAILABLE');

-- ----------------------------
-- Table structure for `orders`
-- ----------------------------
DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `initiator_user_id` int NOT NULL,
  `assigned_driver_id` int DEFAULT NULL,
  `status` enum('CREATED','ACCEPTED','IN_PROGRESS','COMPLETED','CANCELED') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'CREATED',
  `destination` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `mileage` decimal(10,2) DEFAULT '0.00',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `completed_at` timestamp NULL DEFAULT NULL,
  `vehicle_type` enum('large','small') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `carbon_emission` decimal(10,2) DEFAULT '0.00',
  `driver_id` int DEFAULT NULL,
  `vehicle_id` int DEFAULT NULL,
  `startlocation` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`order_id`) USING BTREE,
  KEY `initiator_user_id` (`initiator_user_id`) USING BTREE,
  KEY `assigned_driver_id` (`assigned_driver_id`) USING BTREE,
  KEY `fk_driver` (`driver_id`) USING BTREE,
  KEY `fk_vehicle` (`vehicle_id`) USING BTREE,
  CONSTRAINT `fk_driver` FOREIGN KEY (`driver_id`) REFERENCES `drivers` (`driver_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_vehicle` FOREIGN KEY (`vehicle_id`) REFERENCES `vehicles` (`vehicle_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`initiator_user_id`) REFERENCES `users` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`assigned_driver_id`) REFERENCES `users` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of orders
-- ----------------------------
INSERT INTO `orders` VALUES ('1', '123', '123', 'COMPLETED', '11', '11.00', '2024-05-16 19:57:40', '2024-05-08 19:57:43', 'large', '11.00', '1', '889', 'shanghai');
INSERT INTO `orders` VALUES ('6', '125', null, 'CREATED', 'shanghai', '10.00', '2024-05-09 12:02:55', null, 'small', '10.00', null, null, 'beijing');
INSERT INTO `orders` VALUES ('8', '123', null, 'CREATED', 'beijing', '0.00', '2024-05-09 12:44:01', null, 'small', '0.00', null, null, 'shanghai');
INSERT INTO `orders` VALUES ('9', '123', null, 'CREATED', 'shanghai', '0.00', '2024-05-09 13:11:54', null, 'large', '0.00', null, '241166', 'shanghai');

-- ----------------------------
-- Table structure for `sustainabilitydata`
-- ----------------------------
DROP TABLE IF EXISTS `sustainabilitydata`;
CREATE TABLE `sustainabilitydata` (
  `data_id` int NOT NULL AUTO_INCREMENT,
  `order_id` int NOT NULL,
  `carbon_emission` decimal(10,2) NOT NULL,
  `fuel_consumption` decimal(10,2) NOT NULL,
  `efficiency_score` decimal(5,2) NOT NULL,
  PRIMARY KEY (`data_id`) USING BTREE,
  KEY `order_id` (`order_id`) USING BTREE,
  CONSTRAINT `sustainabilitydata_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of sustainabilitydata
-- ----------------------------

-- ----------------------------
-- Table structure for `users`
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password_hash` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `role` enum('DRIVER','WAREHOUSE','ADMIN') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `avatar_url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`) USING BTREE,
  UNIQUE KEY `username` (`username`) USING BTREE,
  UNIQUE KEY `email` (`email`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=129 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES ('1', 'jialin', 'scrypt:32768:8:1$E13QPRa6nwDLL2mW$48b5b53f3fe0f0317749787264984e346f50b0aa925e96de58a772c5475fcd516f8d12ca4d004c0ebe25956fb7be5f959c17bc3cb93fe695368e08405f72fb60', 'ADMIN', null, 'tianjialingogogo@163.com', '2024-05-09 09:28:05');
INSERT INTO `users` VALUES ('123', 'username', '123', 'DRIVER', '123', 'email', '2024-04-16 15:01:07');
INSERT INTO `users` VALUES ('125', 'Tony', 'scrypt:32768:8:1$UJnMDvQDme2sKRP3$bea95d810a794c8fd7207cd1796ca8a110c68f38b363096d24d43b3d46ea36ddaa2c6fb818c496636e8ea18b413d5a10285275ae08ff85415e204a1baef6cc58', 'ADMIN', null, 'hsz0828@163.com', '2024-05-08 14:50:37');
INSERT INTO `users` VALUES ('128', 'fuck', 'scrypt:32768:8:1$onjuhD7cRVss1kiy$dcb635e93c0241ccfcb0b6216f93b1b7416793b2325dd53a481eeb94976816752077597dd755fce886ea9ebf04ef66767ad9b683dc23c80032b672a734fab430', 'ADMIN', null, 'fuck@you.com', '2024-05-11 07:47:59');

-- ----------------------------
-- Table structure for `vehicles`
-- ----------------------------
DROP TABLE IF EXISTS `vehicles`;
CREATE TABLE `vehicles` (
  `vehicle_id` int NOT NULL AUTO_INCREMENT,
  `type` enum('LARGE','SMALL') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `load_capacity` decimal(10,2) NOT NULL,
  `emission_rate` decimal(10,2) NOT NULL,
  PRIMARY KEY (`vehicle_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=241167 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of vehicles
-- ----------------------------
INSERT INTO `vehicles` VALUES ('889', 'SMALL', '111.00', '111.00');
INSERT INTO `vehicles` VALUES ('241166', 'SMALL', '123456.00', '12212.00');

-- ----------------------------
-- Table structure for `warehouses`
-- ----------------------------
DROP TABLE IF EXISTS `warehouses`;
CREATE TABLE `warehouses` (
  `warehouse_id` int NOT NULL AUTO_INCREMENT,
  `longitude` decimal(9,6) NOT NULL,
  `latitude` decimal(9,6) NOT NULL,
  `city` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `capacity` decimal(10,2) NOT NULL,
  PRIMARY KEY (`warehouse_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of warehouses
-- ----------------------------
