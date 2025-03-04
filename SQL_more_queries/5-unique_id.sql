-- Create the table unique_id with id INT default value to 1 and must be unique, name VARCHAR(256)
CREATE TABLE IF NOT EXISTS `unique_id` (
	`id` INT DEFAULT 1 UNIQUE,
	`name` VARCHAR(256)
)