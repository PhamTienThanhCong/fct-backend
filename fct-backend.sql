-- phpMyAdmin SQL Dump
-- version 5.2.0-rc1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 03, 2023 at 05:24 PM
-- Server version: 5.7.33
-- PHP Version: 8.1.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fct-backend`
--

-- --------------------------------------------------------

--
-- Table structure for table `car_infos`
--

CREATE TABLE `car_infos` (
  `id` int(11) NOT NULL,
  `car_type_id` varchar(50) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `name_car` varchar(255) NOT NULL,
  `license_plate` varchar(50) NOT NULL,
  `vehicle_condition` varchar(255) DEFAULT NULL,
  `battery_status` varchar(100) DEFAULT NULL,
  `year_of_manufacture` int(11) DEFAULT NULL,
  `created_at` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `car_types`
--

CREATE TABLE `car_types` (
  `id` varchar(50) NOT NULL,
  `name` varchar(255) NOT NULL,
  `country` varchar(255) NOT NULL,
  `description` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `car_types`
--

INSERT INTO `car_types` (`id`, `name`, `country`, `description`) VALUES
('bmw', 'BMW', 'Vietnam', 'BMW Vietnam is a subsidiary of Bayerische Motoren Werke AG, a German luxury automobile and motorcycle manufacturer.'),
('chevrolet', 'Chevrolet', 'Vietnam', 'Chevrolet Vietnam is a subsidiary of Chevrolet, an American automobile brand.'),
('ford', 'Ford', 'Vietnam', 'Ford Vietnam is a subsidiary of Ford Motor Company, an American automaker.'),
('hino', 'Hino', 'Vietnam', 'Hino Motors Vietnam is a subsidiary of Hino Motors, a Japanese manufacturer of trucks and buses.'),
('honda', 'Honda', 'Vietnam', 'Honda Vietnam is a subsidiary of Honda Motor Co., Ltd., a Japanese automaker.'),
('hyundai', 'Hyundai', 'Vietnam', 'Hyundai Thành Công Vietnam is a joint venture between Hyundai Motor Company and Thành Công Corporation in Vietnam.'),
('isuzu', 'Isuzu', 'Vietnam', 'Isuzu Vietnam is a subsidiary of Isuzu Motors Limited, a Japanese manufacturer of commercial vehicles.'),
('kia', 'Kia', 'Vietnam', 'Kia Motors Vietnam is a subsidiary of Kia Corporation, a South Korean automobile manufacturer.'),
('mazda', 'Mazda', 'Vietnam', 'Mazda Vietnam is a subsidiary of Mazda Motor Corporation, a Japanese automaker.'),
('mercedes', 'Mercedes-Benz', 'Vietnam', 'Mercedes-Benz Vietnam is a subsidiary of Mercedes-Benz, a German luxury automobile manufacturer.'),
('mitsubishi', 'Mitsubishi', 'Vietnam', 'Mitsubishi Motors Vietnam is a subsidiary of Mitsubishi Motors, a Japanese automaker.'),
('peugeot', 'Peugeot', 'Vietnam', 'Peugeot Vietnam is a subsidiary of Stellantis, a French multinational automotive manufacturer.'),
('samco', 'SAMCO', 'Vietnam', 'Sài Gòn Mechanical Engineering Corporation (SAMCO) is a leading manufacturer of buses and special-purpose vehicles in Vietnam.'),
('samsung', 'Samsung', 'Vietnam', 'Samsung Vietnam is a subsidiary of Samsung C&T Corporation, a South Korean company that manufactures commercial vehicles.'),
('subaru', 'Subaru', 'Vietnam', 'Subaru Vietnam is a subsidiary of Subaru Corporation, a Japanese automobile manufacturer.'),
('suzuki', 'Suzuki', 'Vietnam', 'Suzuki Vietnam is a subsidiary of Suzuki Motor Corporation, a Japanese automaker.'),
('thaco', 'Thaco', 'Vietnam', 'Trường Hải Auto Corporation (Thaco) is a major Vietnamese automobile manufacturer.'),
('vinfast', 'VinFast', 'Vietnam', 'VinFast is a Vietnamese automotive manufacturer based in Hanoi, Vietnam.'),
('yamaha', 'Yamaha', 'Vietnam', 'Yamaha Motor Vietnam is a subsidiary of Yamaha Motor Co., Ltd., a Japanese motorcycle manufacturer.');

-- --------------------------------------------------------

--
-- Table structure for table `charging_ports`
--

CREATE TABLE `charging_ports` (
  `id` int(11) NOT NULL,
  `station_id` int(11) DEFAULT NULL,
  `port_code` varchar(50) NOT NULL,
  `price` float NOT NULL,
  `power` float NOT NULL,
  `status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `comments`
--

CREATE TABLE `comments` (
  `id` int(11) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `station_id` int(11) DEFAULT NULL,
  `title` varchar(255) NOT NULL,
  `content` varchar(255) NOT NULL,
  `rating` int(11) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `id` int(11) NOT NULL,
  `email` varchar(250) DEFAULT NULL,
  `password` varchar(255) NOT NULL,
  `full_name` varchar(100) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `card_id` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `id` int(11) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `charging_port_id` int(11) DEFAULT NULL,
  `status` int(11) NOT NULL DEFAULT '1',
  `start_time` datetime NOT NULL,
  `end_time` datetime NOT NULL,
  `total_price` float NOT NULL,
  `total_time` float NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `rescue_services`
--

CREATE TABLE `rescue_services` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `address` varchar(255) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `local_x` float NOT NULL,
  `local_y` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `rescue_services`
--

INSERT INTO `rescue_services` (`id`, `name`, `phone`, `address`, `email`, `local_x`, `local_y`) VALUES
(1, 'Repair Shop 1', '0993474655', '123 Street 1, Hanoi, Vietnam', 'zhgxzovq@yahoo.com', 21.068, 105.718),
(2, 'Repair Shop 2', '0030410026', '123 Street 2, Hanoi, Vietnam', 'dyvcfrdy@gmail.com', 21.0803, 105.666),
(3, 'Repair Shop 3', '0377953733', '123 Street 3, Hanoi, Vietnam', 'iunqbkpi@yahoo.com', 20.9775, 105.817),
(4, 'Repair Shop 4', '0194103278', '123 Street 4, Hanoi, Vietnam', 'yngaezvw@gmail.com', 20.9852, 105.845),
(5, 'Repair Shop 5', '0876643776', '123 Street 5, Hanoi, Vietnam', 'cerjgtoe@viettel.com', 21.0818, 105.794),
(6, 'Repair Shop 6', '0393903094', '123 Street 6, Hanoi, Vietnam', 'uluijvba@outlook.com', 20.9184, 105.843),
(7, 'Repair Shop 7', '0502108518', '123 Street 7, Hanoi, Vietnam', 'drvcmuyc@viettel.com', 20.9578, 105.676),
(8, 'Repair Shop 8', '0998863900', '123 Street 8, Hanoi, Vietnam', 'mqxqqlhd@viettel.com', 20.9633, 105.899),
(9, 'Repair Shop 9', '0971121817', '123 Street 9, Hanoi, Vietnam', 'mtlqvdyn@outlook.com', 21.0644, 105.705),
(10, 'Repair Shop 10', '0738344587', '123 Street 10, Hanoi, Vietnam', 'jvvsyvss@yahoo.com', 21.0273, 105.622),
(11, 'Repair Shop 11', '0721561015', '123 Street 11, Hanoi, Vietnam', 'dirjsshm@outlook.com', 20.9063, 105.821),
(12, 'Repair Shop 12', '0702962573', '123 Street 12, Hanoi, Vietnam', 'tssiqizn@viettel.com', 20.9355, 105.814),
(13, 'Repair Shop 13', '0604363517', '123 Street 13, Hanoi, Vietnam', 'ddqxsnmz@outlook.com', 21.0002, 105.653),
(14, 'Repair Shop 14', '0523294563', '123 Street 14, Hanoi, Vietnam', 'cfizfkbw@viettel.com', 20.952, 105.632),
(15, 'Repair Shop 15', '0217799503', '123 Street 15, Hanoi, Vietnam', 'iiotphrq@gmail.com', 21.0721, 105.605),
(16, 'Repair Shop 16', '0982868896', '123 Street 16, Hanoi, Vietnam', 'jbpimbcr@hotmail.com', 21.0693, 105.717),
(17, 'Repair Shop 17', '0849991324', '123 Street 17, Hanoi, Vietnam', 'qtgykaku@fpt.com', 21.0138, 105.785),
(18, 'Repair Shop 18', '0542603018', '123 Street 18, Hanoi, Vietnam', 'rsseehet@gmail.com', 20.9358, 105.689),
(19, 'Repair Shop 19', '0918442797', '123 Street 19, Hanoi, Vietnam', 'dazbfuwt@viettel.com', 20.9967, 105.785),
(20, 'Repair Shop 20', '0587973045', '123 Street 20, Hanoi, Vietnam', 'ivbkcajo@fpt.com', 21.0142, 105.667),
(21, 'Repair Shop 21', '0351830133', '123 Street 21, Hanoi, Vietnam', 'eclnwovi@yahoo.com', 20.9574, 105.675),
(22, 'Repair Shop 22', '0453751007', '123 Street 22, Hanoi, Vietnam', 'cqcuaxtj@fpt.com', 21.0593, 105.81),
(23, 'Repair Shop 23', '0425064248', '123 Street 23, Hanoi, Vietnam', 'hjvvkjje@viettel.com', 20.9834, 105.788),
(24, 'Repair Shop 24', '0306683670', '123 Street 24, Hanoi, Vietnam', 'wrprjgcb@viettel.com', 21.0344, 105.728),
(25, 'Repair Shop 25', '0089203824', '123 Street 25, Hanoi, Vietnam', 'vuztzvgs@fpt.com', 21.0406, 105.649),
(26, 'Repair Shop 26', '0801629513', '123 Street 26, Hanoi, Vietnam', 'lflovpbj@yahoo.com', 20.9088, 105.765),
(27, 'Repair Shop 27', '0962761818', '123 Street 27, Hanoi, Vietnam', 'aasybpqt@fpt.com', 21.036, 105.631),
(28, 'Repair Shop 28', '0365882179', '123 Street 28, Hanoi, Vietnam', 'lisuiisv@outlook.com', 21.0732, 105.643),
(29, 'Repair Shop 29', '0292944807', '123 Street 29, Hanoi, Vietnam', 'gqkbxfln@hotmail.com', 20.9685, 105.61),
(30, 'Repair Shop 30', '0364024660', '123 Street 30, Hanoi, Vietnam', 'ptrogwas@hotmail.com', 21.0503, 105.842),
(31, 'Repair Shop 31', '0866109514', '123 Street 31, Hanoi, Vietnam', 'pvnqrdnn@viettel.com', 21.0835, 105.779),
(32, 'Repair Shop 32', '0775865388', '123 Street 32, Hanoi, Vietnam', 'xyfizbby@viettel.com', 20.9205, 105.601),
(33, 'Repair Shop 33', '0728353985', '123 Street 33, Hanoi, Vietnam', 'fgejjvtq@gmail.com', 20.9062, 105.628),
(34, 'Repair Shop 34', '0952660618', '123 Street 34, Hanoi, Vietnam', 'xmspvnht@fpt.com', 21.0262, 105.677),
(35, 'Repair Shop 35', '0522124697', '123 Street 35, Hanoi, Vietnam', 'itfjnwfh@viettel.com', 20.9681, 105.77),
(36, 'Repair Shop 36', '0941955803', '123 Street 36, Hanoi, Vietnam', 'enwineat@viettel.com', 20.9008, 105.712),
(37, 'Repair Shop 37', '0187104804', '123 Street 37, Hanoi, Vietnam', 'cnloatpf@yahoo.com', 21.0107, 105.725),
(38, 'Repair Shop 38', '0059252236', '123 Street 38, Hanoi, Vietnam', 'uyyifzdl@outlook.com', 21.025, 105.755),
(39, 'Repair Shop 39', '0760054584', '123 Street 39, Hanoi, Vietnam', 'tcfrajdu@yahoo.com', 21.0531, 105.656),
(40, 'Repair Shop 40', '0833403587', '123 Street 40, Hanoi, Vietnam', 'rbvzbywx@yahoo.com', 21.0297, 105.866),
(41, 'Repair Shop 41', '0530050581', '123 Street 41, Hanoi, Vietnam', 'eriwfhux@hotmail.com', 20.9733, 105.707),
(42, 'Repair Shop 42', '0478632730', '123 Street 42, Hanoi, Vietnam', 'mmoxsahp@outlook.com', 20.9086, 105.671),
(43, 'Repair Shop 43', '0542537695', '123 Street 43, Hanoi, Vietnam', 'zwrasjzt@hotmail.com', 20.9809, 105.883),
(44, 'Repair Shop 44', '0865472206', '123 Street 44, Hanoi, Vietnam', 'ghmwvjuu@fpt.com', 21.0561, 105.813),
(45, 'Repair Shop 45', '0127225021', '123 Street 45, Hanoi, Vietnam', 'bpgxjjir@hotmail.com', 20.913, 105.814),
(46, 'Repair Shop 46', '0531172063', '123 Street 46, Hanoi, Vietnam', 'rwmhnggn@hotmail.com', 21.0133, 105.765),
(47, 'Repair Shop 47', '0887263591', '123 Street 47, Hanoi, Vietnam', 'xktlojks@viettel.com', 21.0069, 105.74),
(48, 'Repair Shop 48', '0478485169', '123 Street 48, Hanoi, Vietnam', 'oafjdwcp@gmail.com', 21.0993, 105.682),
(49, 'Repair Shop 49', '0439080594', '123 Street 49, Hanoi, Vietnam', 'rcalysst@hotmail.com', 20.968, 105.789),
(50, 'Repair Shop 50', '0671428417', '123 Street 50, Hanoi, Vietnam', 'avgrdjjj@yahoo.com', 21.0615, 105.776);

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

CREATE TABLE `roles` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `roles`
--

INSERT INTO `roles` (`id`, `name`, `description`) VALUES
(1, 'admin', 'Administrator'),
(2, 'user', 'Regular User');

-- --------------------------------------------------------

--
-- Table structure for table `stations`
--

CREATE TABLE `stations` (
  `id` int(11) NOT NULL,
  `owner_id` int(11) DEFAULT NULL,
  `name` varchar(100) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `address` varchar(255) NOT NULL,
  `local_x` float NOT NULL,
  `local_y` float NOT NULL,
  `phone` varchar(20) NOT NULL,
  `email` varchar(250) NOT NULL,
  `image` varchar(255) DEFAULT NULL,
  `open_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `close_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `is_order` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `role_id` int(11) DEFAULT NULL,
  `email` varchar(250) NOT NULL,
  `password` varchar(255) NOT NULL,
  `full_name` varchar(100) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `address` varchar(255) NOT NULL,
  `card_id` varchar(25) NOT NULL,
  `title` varchar(100) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `role_id`, `email`, `password`, `full_name`, `phone`, `address`, `card_id`, `title`, `description`) VALUES
(1, 1, 'admin@gmail.com', '$2b$12$yGPL8HdQVKq5Sse2.u2ouuYEUcg/0a6nmoHV8e6fYV4EHcyXupIUa', 'Phạm Tiến Thành Công', '0396396396', 'Hoàn Kiếm, Hà Nội', '021551225400', 'Admin', 'admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `car_infos`
--
ALTER TABLE `car_infos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `car_type_id` (`car_type_id`),
  ADD KEY `customer_id` (`customer_id`);

--
-- Indexes for table `car_types`
--
ALTER TABLE `car_types`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `charging_ports`
--
ALTER TABLE `charging_ports`
  ADD PRIMARY KEY (`id`),
  ADD KEY `station_id` (`station_id`);

--
-- Indexes for table `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `customer_id` (`customer_id`),
  ADD KEY `station_id` (`station_id`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`),
  ADD KEY `customer_id` (`customer_id`),
  ADD KEY `charging_port_id` (`charging_port_id`);

--
-- Indexes for table `rescue_services`
--
ALTER TABLE `rescue_services`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `stations`
--
ALTER TABLE `stations`
  ADD PRIMARY KEY (`id`),
  ADD KEY `owner_id` (`owner_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD KEY `role_id` (`role_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `car_infos`
--
ALTER TABLE `car_infos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `charging_ports`
--
ALTER TABLE `charging_ports`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `comments`
--
ALTER TABLE `comments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `rescue_services`
--
ALTER TABLE `rescue_services`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT for table `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `stations`
--
ALTER TABLE `stations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `car_infos`
--
ALTER TABLE `car_infos`
  ADD CONSTRAINT `car_infos_ibfk_1` FOREIGN KEY (`car_type_id`) REFERENCES `car_types` (`id`),
  ADD CONSTRAINT `car_infos_ibfk_2` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`);

--
-- Constraints for table `charging_ports`
--
ALTER TABLE `charging_ports`
  ADD CONSTRAINT `charging_ports_ibfk_1` FOREIGN KEY (`station_id`) REFERENCES `stations` (`id`);

--
-- Constraints for table `comments`
--
ALTER TABLE `comments`
  ADD CONSTRAINT `comments_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`),
  ADD CONSTRAINT `comments_ibfk_2` FOREIGN KEY (`station_id`) REFERENCES `stations` (`id`);

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`),
  ADD CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`charging_port_id`) REFERENCES `charging_ports` (`id`);

--
-- Constraints for table `stations`
--
ALTER TABLE `stations`
  ADD CONSTRAINT `stations_ibfk_1` FOREIGN KEY (`owner_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
