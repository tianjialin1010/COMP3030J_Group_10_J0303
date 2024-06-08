/*
Navicat MySQL Data Transfer

Source Server         : localhost_3316
Source Server Version : 80033
Source Host           : localhost:3306
Source Database       : refresh_comp3030j

Target Server Type    : MYSQL
Target Server Version : 80033
File Encoding         : 65001

Date: 2024-06-08 11:24:24
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `drivers`
-- ----------------------------
DROP TABLE IF EXISTS `drivers`;
CREATE TABLE `drivers` (
  `driver_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `total_mileage` decimal(10,2) NOT NULL DEFAULT '0.00',
  `total_emission` decimal(10,2) NOT NULL DEFAULT '0.00',
  `orders_count` int NOT NULL DEFAULT '0',
  `status` enum('AVAILABLE','UNAVAILABLE') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`driver_id`),
  UNIQUE KEY `user_id` (`user_id`) USING BTREE,
  CONSTRAINT `drivers_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of drivers
-- ----------------------------
INSERT INTO `drivers` VALUES ('1', '5', '0.00', '0.00', '0', 'AVAILABLE');
INSERT INTO `drivers` VALUES ('2', '6', '0.00', '0.00', '0', 'AVAILABLE');
INSERT INTO `drivers` VALUES ('3', '7', '0.00', '0.00', '0', 'AVAILABLE');
INSERT INTO `drivers` VALUES ('4', '8', '0.00', '0.00', '0', 'AVAILABLE');
INSERT INTO `drivers` VALUES ('5', '9', '0.00', '0.00', '0', 'AVAILABLE');
INSERT INTO `drivers` VALUES ('6', '20', '0.00', '0.00', '0', 'AVAILABLE');
INSERT INTO `drivers` VALUES ('7', '21', '0.00', '0.00', '0', 'AVAILABLE');
INSERT INTO `drivers` VALUES ('8', '22', '0.00', '0.00', '0', 'AVAILABLE');

-- ----------------------------
-- Table structure for `orders`
-- ----------------------------
DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `assigned_driver_id` int DEFAULT NULL,
  `status` enum('CREATED','ACCEPTED','IN_PROGRESS','COMPLETED') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'CREATED',
  `origin` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `destination` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `license_plate` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `completed_at` timestamp NULL DEFAULT NULL,
  `mileage` decimal(10,2) DEFAULT '0.00',
  `estimate_time` decimal(10,2) DEFAULT NULL,
  `carbon_emission` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`order_id`),
  KEY `assigned_driver_id` (`assigned_driver_id`) USING BTREE,
  KEY `license_plate` (`license_plate`) USING BTREE,
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`assigned_driver_id`) REFERENCES `drivers` (`driver_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`license_plate`) REFERENCES `vehicles` (`license_plate`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of orders
-- ----------------------------
INSERT INTO `orders` VALUES ('1', null, 'CREATED', 'Dublin', 'Galway', null, '2024-05-15 01:25:37', null, '207.00', '8465.00', null);
INSERT INTO `orders` VALUES ('2', null, 'CREATED', 'Dublin', 'Cork', null, '2024-05-15 01:54:41', null, '260.00', '10331.00', null);
INSERT INTO `orders` VALUES ('3', null, 'CREATED', 'Dublin', 'Cork', null, '2024-05-15 16:17:05', null, '260.00', '10331.00', null);
INSERT INTO `orders` VALUES ('4', null, 'CREATED', 'Cork', 'Galway', null, '2024-05-15 16:17:19', null, '205.00', '9121.00', null);
INSERT INTO `orders` VALUES ('5', null, 'CREATED', 'Limerick', 'Dublin', null, '2024-05-15 16:17:30', null, '203.00', '8353.00', null);
INSERT INTO `orders` VALUES ('6', null, 'CREATED', 'Dublin', 'Cork', null, '2024-05-15 16:17:42', null, '260.00', '10331.00', null);
INSERT INTO `orders` VALUES ('7', null, 'CREATED', 'Limerick', 'Dublin', null, '2024-05-15 16:17:54', null, '203.00', '8353.00', null);
INSERT INTO `orders` VALUES ('8', null, 'CREATED', 'Galway', 'Dublin', null, '2024-05-15 16:33:32', null, '207.00', '8465.00', null);
INSERT INTO `orders` VALUES ('9', null, 'CREATED', 'Galway', 'Dublin', null, '2024-05-15 16:34:14', null, '207.00', '8465.00', null);
INSERT INTO `orders` VALUES ('10', null, 'CREATED', 'Limerick', 'Cork', null, '2024-05-15 16:34:20', null, '99.00', '5461.00', null);
INSERT INTO `orders` VALUES ('11', null, 'CREATED', 'Limerick', 'Cork', null, '2024-05-15 16:34:29', null, '99.00', '5461.00', null);

-- ----------------------------
-- Table structure for `users`
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password_hash` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `role` enum('DRIVER','WAREHOUSE','ADMIN') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `avatar_url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `username` (`username`) USING BTREE,
  UNIQUE KEY `email` (`email`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES ('5', 'd1', 'd@1.com', 'scrypt:32768:8:1$rwHT6OCm2TFMZA8y$f38795e6c058927a56ee669f207af901a3e082d5f96e7774c1fa45b876d65ac3d30325021ba6e66f689902ee81718c1005f6dae38bb886689bb20079ff377f4e', 'DRIVER', null, '2024-05-14 14:48:19');
INSERT INTO `users` VALUES ('6', 'd2', 'd@2.com', 'scrypt:32768:8:1$Ai0qP8fatdj95kfq$673c0fb29fe5550b0fd399d07e2b993770d85941cd4324cdff88b1ebd754f9a6e5c378b80d4678e3e6bfceb43fbcbb575bb1b4035ba541f4722bb55d68191390', 'DRIVER', null, '2024-05-14 14:49:56');
INSERT INTO `users` VALUES ('7', 'd3', 'd@3.com', 'scrypt:32768:8:1$OPtyi3gbHe7LKgXI$c3509c0ab08bff6b0f701a78e70a861b6fbf86563a10894879d0740a93911dbf9bf84da05216666f6596249e20ebe843fe7596e774e7085c8af2e37dfb025006', 'DRIVER', null, '2024-05-14 14:50:10');
INSERT INTO `users` VALUES ('8', 'd4', 'd@4.com', 'scrypt:32768:8:1$awwWZpElcn5oJmtV$47396d5c43be867905a4452d0ae43a2ef56232bea50dcc343ffe1f96b3366f97549e30945646c531020fddbc34b426d4c90d616adea74b39f0a90d0ca593c4dc', 'DRIVER', null, '2024-05-14 14:50:24');
INSERT INTO `users` VALUES ('9', 'd5', 'd@5.com', 'scrypt:32768:8:1$SHSC8qKwW06sqdTc$c1e22f762125b8ce72a807207b3f9251d77070869d1e0e6de7094fd64013ac5b393a38b67ae9bd044a0c6d5e1e805101d5bea10dc44fce048a4f63a684fddef7', 'DRIVER', null, '2024-05-14 14:50:42');
INSERT INTO `users` VALUES ('10', 'w1', 'w@1.com', 'scrypt:32768:8:1$wUghCIFRI30rBm0m$bb6d17ff0b6705b474dee85f0a32047b6477e1af2be6bfa5496e1b749e93e5a91f94a01883a8acc8b6a0f3f70a6c0737f33a108f78d3e8d64e48872cd1b4941c', 'WAREHOUSE', null, '2024-05-14 15:01:14');
INSERT INTO `users` VALUES ('11', 'w2', 'w@2.com', 'scrypt:32768:8:1$ECcCxR8t6hms88UQ$05a967ddad8f1a0f1ac880d307ccf416f1bd47cecfa9e56635bac63a0f0854b7c9f719353e8e06ed7e03fbaf162328e411fdd792fbd7eaf3b7f472b5227a4a97', 'WAREHOUSE', null, '2024-05-14 15:01:30');
INSERT INTO `users` VALUES ('12', 'w3', 'w@3.com', 'scrypt:32768:8:1$pMJMCJrmTF9MFoI8$aa326942e47e6dc3542eb9e574de5d7da435a4f87629595418ac4a40377e2dc1af3d6a3a515f6a8aaa537318fc94f8111d16dedc31c3347b84239706bdf6fb57', 'WAREHOUSE', null, '2024-05-14 15:01:42');
INSERT INTO `users` VALUES ('13', 'w4', 'w@4.com', 'scrypt:32768:8:1$GgNqQO4EpspH6URF$ce9796d3583679feca98cb6cf776b9c447a12bc538b95884348b96c991b79cb29e69b29c996b0dd39fbcfca5e7138c6d497a0628e71000e0b15fef6599f107f8', 'WAREHOUSE', null, '2024-05-14 15:01:53');
INSERT INTO `users` VALUES ('14', 'w5', 'w@5.com', 'scrypt:32768:8:1$10Fba3Vj9Nk2xh5G$cdb2894a3ff3e7bd03434e534530c93ab06a1110fc9b6d441fc959ddfcf728e9a69c88d06e5288d991bac91ecb126da1bd92b064bdb8f1c54b1516dd3c7cfd93', 'WAREHOUSE', null, '2024-05-14 15:02:23');
INSERT INTO `users` VALUES ('15', 'a1', 'a@1.com', 'scrypt:32768:8:1$Ipv20Tm1JK9VYqcg$124c3dee2b5a4770978a0db9ddc6b9778395980ed00913930af4081edc4f85f721cc3b2c93114b2cd19e38006f7d6b980b8478239203dcbef88df8b18cd0355c', 'ADMIN', null, '2024-05-14 15:03:07');
INSERT INTO `users` VALUES ('16', 'a2', 'a@2.com', 'scrypt:32768:8:1$AcckuVjRzdL28h5L$3052267a93e1d33dc7a8a81ca306175f2e237a0e7380470079c66b2b2b040d325aaf4f29fdac2d59f672ef18018c7a5de66c13c440d40881c8df86c02b173897', 'ADMIN', null, '2024-05-14 15:03:18');
INSERT INTO `users` VALUES ('17', 'a3', 'a@3.com', 'scrypt:32768:8:1$OQqLNORAQ429HGa0$479452f139c11f3d88c418e6063459a90947b054d33af6da00b3a6369f83d6af79ee4ed3ad9d67466f6dd7efc2d64c32583084cfcf9f7d70925eeb30afd95d50', 'ADMIN', null, '2024-05-14 15:03:29');
INSERT INTO `users` VALUES ('18', 'a4', 'a@4.com', 'scrypt:32768:8:1$H1R4Fiu2JE3J1L1x$b054e50a14182bae917f7627d17a8b3883081c851f7fc0dd3eabfb93087cf10df65c4cd20177c2d6effb30cf34a41cbe3500a955449fe12d9ed1c7f4860410d4', 'ADMIN', null, '2024-05-14 15:04:05');
INSERT INTO `users` VALUES ('19', 'a5', 'a@5.com', 'scrypt:32768:8:1$9erMm524kZn1R9sa$2f08790553aa93fae9afdf386ebfe08a10663ccb04728604e6088abc7f4fc9dfce8e01600653ed21193caa84ae93115bf269c74bd9b51752be45f5da8b69b3db', 'ADMIN', null, '2024-05-14 15:04:30');
INSERT INTO `users` VALUES ('20', 'del1', 'del@1.com', 'scrypt:32768:8:1$kgeiei5XYwwml86C$6819893f60d1a8527a11740a4db3140f012a90ccb708041ecbd248f344de981d5fa730f71c011401c0fa79a41093967e76a06adcb3fc72149f10c04ff11d08df', 'DRIVER', null, '2024-05-14 15:04:51');
INSERT INTO `users` VALUES ('21', 'del2', 'del@2.com', 'scrypt:32768:8:1$K9T5LOi6xBxhE1V8$33e87cd3d0cf93bf312178f1df963a3d8f5d9b3a895561204cffca2ecd8259f67e6adad233e6f0282392a97001d617e25539b14e4eb386d63e231bd9299ca8f4', 'DRIVER', null, '2024-05-14 15:05:03');
INSERT INTO `users` VALUES ('22', 'del3', 'del@3.com', 'scrypt:32768:8:1$D0svwItF8vWMBDKF$1aba065d867b03b32bd2f4bfe277b878d627b641035577b9e8bdf704d26dc0d9cd4527ce018bb0e4eccdcb0ff10b36347c29f8bf360a17187b7a85f113971506', 'DRIVER', null, '2024-05-14 15:05:22');
INSERT INTO `users` VALUES ('23', 'del4', 'del@4.com', 'scrypt:32768:8:1$ltzDTlqicFoKUjhV$a827ad9877ed4279150f9eceaa9f9ed0d7230bc4d336bc235a8e02cd193958657a91f143b787dc56ef3ea5294a2df5694af64b98310df935d1b1403a127a8505', 'WAREHOUSE', null, '2024-05-14 15:05:37');
INSERT INTO `users` VALUES ('24', 'del5', 'del@5.com', 'scrypt:32768:8:1$btWAPsSj5spGS5Gp$5c1d08a6b8a027b40295c2c63240bcdef5b03c2051efa38f5af54d8c672118c5602664d666d4b505a66ec3f2799a44ab309be14086f11f453ba549e121523848', 'WAREHOUSE', null, '2024-05-14 15:05:46');
INSERT INTO `users` VALUES ('25', 'del6', 'del@6.com', 'scrypt:32768:8:1$KURg5lCGoUAWwYMY$f4b04f53db2103c216b548238da01e16cbe5a36a880a78673797be5d0facbf01f0b3c420c89204542e624efa23edcbcadb027b7d7ad97651847a765c8a9dda50', 'WAREHOUSE', null, '2024-05-14 15:05:59');
INSERT INTO `users` VALUES ('26', 'del7', 'del@7.com', 'scrypt:32768:8:1$6jmgkXRZOtxKlNbu$95626699f3e858bd71087707f6306c60479abeeadd3375e471c1129721ec6860aea17529bbe1cea132ddc462591c1a691857ba1024b6f8c61601321b3ac394a9', 'ADMIN', null, '2024-05-14 15:06:12');
INSERT INTO `users` VALUES ('27', 'del8', 'del@8.com', 'scrypt:32768:8:1$xA3fWRcgGvrlZJHz$433c82d021cccd60929c29bd38c42748fdc278e0c57e2a3f72927b406bff06a0a49f0f56d2ac03d4e2ad894283e6f0980eb65f30c6c33f906964a2778bea69cc', 'ADMIN', null, '2024-05-14 15:06:25');
INSERT INTO `users` VALUES ('28', 'del9', 'del@9.com', 'scrypt:32768:8:1$B122sJ3fbo4AtaYE$50107e3384c07ea9a46c483becd9ec8032ded2206124028cdf1e9c4229a86388998c1b0bb2b791d6c481aecf9b991290e2a66d6973f98fb64faeeb3e6f832a23', 'ADMIN', null, '2024-05-14 15:06:35');
INSERT INTO `users` VALUES ('29', 'jialin', 'tianjialingogogo@163.com', 'scrypt:32768:8:1$fgtVYaGXgSPydk6W$80801dbf63d13b1d094c03e766a45c959ed9cf4d6d40cb13494ead677d1f6675dfb890f7285881b4774e62451ca5e5d307f4f9cc05ddeb6743c7e7145f6c1549', 'ADMIN', null, '2024-05-14 17:58:57');

-- ----------------------------
-- Table structure for `vehicles`
-- ----------------------------
DROP TABLE IF EXISTS `vehicles`;
CREATE TABLE `vehicles` (
  `license_plate` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `type` enum('TRUCK','VAN','ELECTRIC') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `emission_rate` decimal(10,2) NOT NULL,
  `owner_id` int DEFAULT NULL,
  PRIMARY KEY (`license_plate`),
  KEY `vehicles_ibfk_1` (`owner_id`),
  CONSTRAINT `vehicles_ibfk_1` FOREIGN KEY (`owner_id`) REFERENCES `drivers` (`driver_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of vehicles
-- ----------------------------
INSERT INTO `vehicles` VALUES ('01D67696', 'ELECTRIC', '0.05', '1');
INSERT INTO `vehicles` VALUES ('02D41166', 'TRUCK', '0.30', '1');
INSERT INTO `vehicles` VALUES ('06C12552', 'VAN', '0.20', '1');
INSERT INTO `vehicles` VALUES ('06D32798', 'TRUCK', '0.30', null);
INSERT INTO `vehicles` VALUES ('07C27321', 'ELECTRIC', '0.05', null);
INSERT INTO `vehicles` VALUES ('07C27518', 'TRUCK', '0.30', null);
INSERT INTO `vehicles` VALUES ('07D26282', 'ELECTRIC', '0.05', null);
INSERT INTO `vehicles` VALUES ('07D54685', 'ELECTRIC', '0.05', null);
INSERT INTO `vehicles` VALUES ('08D67820', 'TRUCK', '0.30', null);
INSERT INTO `vehicles` VALUES ('08D67822', 'ELECTRIC', '0.05', null);
INSERT INTO `vehicles` VALUES ('08TS8198', 'ELECTRIC', '0.05', null);
INSERT INTO `vehicles` VALUES ('09D14573', 'TRUCK', '0.30', null);
INSERT INTO `vehicles` VALUES ('09D14863', 'VAN', '0.20', null);
INSERT INTO `vehicles` VALUES ('09D14888', 'ELECTRIC', '0.05', null);
INSERT INTO `vehicles` VALUES ('09D14925', 'TRUCK', '0.30', null);
INSERT INTO `vehicles` VALUES ('09D14963', 'TRUCK', '0.30', null);
INSERT INTO `vehicles` VALUES ('09D14977', 'ELECTRIC', '0.05', null);
INSERT INTO `vehicles` VALUES ('09D14983', 'VAN', '0.20', null);
INSERT INTO `vehicles` VALUES ('09D16185', 'TRUCK', '0.30', null);
INSERT INTO `vehicles` VALUES ('09D557', 'VAN', '0.20', null);
INSERT INTO `vehicles` VALUES ('09D989', 'ELECTRIC', '0.05', null);
INSERT INTO `vehicles` VALUES ('10D30871', 'VAN', '0.20', null);
INSERT INTO `vehicles` VALUES ('10WH473', 'ELECTRIC', '0.05', null);
INSERT INTO `vehicles` VALUES ('10WH787', 'VAN', '0.20', null);
INSERT INTO `vehicles` VALUES ('10WH801', 'ELECTRIC', '0.05', null);
INSERT INTO `vehicles` VALUES ('11D1237', 'TRUCK', '0.30', null);
INSERT INTO `vehicles` VALUES ('11D1253', 'TRUCK', '0.30', null);
INSERT INTO `vehicles` VALUES ('11D9934', 'VAN', '0.20', null);
INSERT INTO `vehicles` VALUES ('12D13709', 'VAN', '0.20', null);
INSERT INTO `vehicles` VALUES ('131C1722', 'VAN', '0.20', null);
INSERT INTO `vehicles` VALUES ('131C1724', 'TRUCK', '0.30', null);
INSERT INTO `vehicles` VALUES ('131D7170', 'TRUCK', '0.30', null);
INSERT INTO `vehicles` VALUES ('131D7173', 'VAN', '0.20', null);
INSERT INTO `vehicles` VALUES ('131D7199', 'VAN', '0.20', null);
INSERT INTO `vehicles` VALUES ('132D9091', 'ELECTRIC', '0.05', null);
INSERT INTO `vehicles` VALUES ('141D1454', 'VAN', '0.20', null);
INSERT INTO `vehicles` VALUES ('142D10523', 'TRUCK', '0.30', null);
INSERT INTO `vehicles` VALUES ('161WH1088', 'VAN', '0.20', null);
INSERT INTO `vehicles` VALUES ('161WH1112', 'VAN', '0.20', null);
INSERT INTO `vehicles` VALUES ('162D22319', 'TRUCK', '0.30', null);
INSERT INTO `vehicles` VALUES ('181D13047', 'VAN', '0.20', null);
INSERT INTO `vehicles` VALUES ('181D5468', 'VAN', '0.20', null);
INSERT INTO `vehicles` VALUES ('182D15751', 'VAN', '0.20', null);
INSERT INTO `vehicles` VALUES ('191D10766', 'TRUCK', '0.30', null);
INSERT INTO `vehicles` VALUES ('191D45114', 'ELECTRIC', '0.05', null);
INSERT INTO `vehicles` VALUES ('191WX66', 'VAN', '0.20', null);
INSERT INTO `vehicles` VALUES ('192C4667', 'TRUCK', '0.30', null);
INSERT INTO `vehicles` VALUES ('192D12336', 'ELECTRIC', '0.05', null);
INSERT INTO `vehicles` VALUES ('192D23336', 'ELECTRIC', '0.05', null);
INSERT INTO `vehicles` VALUES ('201D19122', 'ELECTRIC', '0.05', null);
INSERT INTO `vehicles` VALUES ('202D12417', 'TRUCK', '0.30', null);
INSERT INTO `vehicles` VALUES ('202D12958', 'VAN', '0.20', null);
INSERT INTO `vehicles` VALUES ('202D16089', 'TRUCK', '0.30', null);
INSERT INTO `vehicles` VALUES ('202D16538', 'VAN', '0.20', null);
INSERT INTO `vehicles` VALUES ('202D19711', 'ELECTRIC', '0.05', null);
INSERT INTO `vehicles` VALUES ('231D31798', 'TRUCK', '0.30', null);
INSERT INTO `vehicles` VALUES ('231D33337', 'TRUCK', '0.30', null);
INSERT INTO `vehicles` VALUES ('232D4068', 'ELECTRIC', '0.05', null);
INSERT INTO `vehicles` VALUES ('95D12221', 'ELECTRIC', '0.05', null);
INSERT INTO `vehicles` VALUES ('97D51632', 'ELECTRIC', '0.05', null);

-- ----------------------------
-- Table structure for `warehouses`
-- ----------------------------
DROP TABLE IF EXISTS `warehouses`;
CREATE TABLE `warehouses` (
  `warehouse_id` int NOT NULL AUTO_INCREMENT,
  `city` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `capacity` decimal(10,2) NOT NULL,
  `manager_user_id` int DEFAULT NULL,
  PRIMARY KEY (`warehouse_id`),
  KEY `manager_user_id` (`manager_user_id`) USING BTREE,
  CONSTRAINT `warehouses_ibfk_1` FOREIGN KEY (`manager_user_id`) REFERENCES `users` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of warehouses
-- ----------------------------
INSERT INTO `warehouses` VALUES ('1', 'Dublin', '10000.00', '10');
INSERT INTO `warehouses` VALUES ('2', 'Cork', '10000.00', '11');
INSERT INTO `warehouses` VALUES ('3', 'Galway', '10000.00', '12');
INSERT INTO `warehouses` VALUES ('4', 'Limerick', '10000.00', '13');
