CREATE DATABASE IF NOT EXISTS inari_restaurant_db;

USE inari_restaurant_db;

CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    state ENUM('available', 'out of stock') NOT NULL,
    date_added DATE NOT NULL,
    amount INT NOT NULL,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    company VARCHAR(255),
    email VARCHAR(255) NOT NULL,
    address VARCHAR(255),
    notes TEXT,
    product_id INT,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);
