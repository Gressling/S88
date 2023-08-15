CREATE TABLE `chemicals_inventory` (
  `synonym` varchar(150) DEFAULT NULL,
  `name` varchar(150) DEFAULT NULL,
  `density` varchar(20) NOT NULL,
  `molecular_weight` double DEFAULT NULL,
  `SF` text,
  `CAS` varchar(20) NOT NULL,
  `comment` varchar(30) DEFAULT NULL,
  `price_per_kg` decimal(10,2) DEFAULT '10.00'
) ENGINE=InnoDB DEFAULT CHARSET=utf8