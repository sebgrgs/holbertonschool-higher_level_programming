-- Create the database hbtn_0d_usa and the table cities
-- Cities has id INT UNIQUE auto generated cant be null and is a primary key
-- state_id INT, cant be null and must be a foreign KEY that references to id of the states table
-- name VARCHAR(256) cant be null
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `cities` (
	`id` INT UNIQUE AUTO_INCREMENT NOT NULL,
	`state_id` INT NOT NULL,
	`name` VARCHAR(256) NOT NULL,
	PRIMARY KEY (`id`),
	FOREIGN KEY (`state_id`) REFERENCES `states`(`id`)
)