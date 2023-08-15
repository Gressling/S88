CREATE TABLE `unitoperations` (
  `UOName` varchar(255) NOT NULL,
  `UOCost` decimal(10,2) DEFAULT NULL,
  `WorkCost` decimal(10,2) DEFAULT NULL,
  `PrepTime` int(11) DEFAULT NULL,
  PRIMARY KEY (`UOName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8