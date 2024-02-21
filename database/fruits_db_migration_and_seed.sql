DROP DATABASE IF EXISTS fruits_db;
CREATE DATABASE fruits_db;
USE fruits_db;

CREATE TABLE fruits(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    quantity INT UNSIGNED NOT NUlL
);

INSERT INTO fruits(name, quantity) VALUES
  ('apple', 3),
  ('banana', 4),
  ('cantelope', 16),
  ('dragonfruit', 1),
  ('elderberry', 2);