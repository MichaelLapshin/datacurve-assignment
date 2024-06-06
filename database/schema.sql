DROP DATABASE IF EXISTS datacurve;
CREATE DATABASE datacurve;

USE datacurve;

CREATE TABLE submissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    code TEXT
);

CREATE TABLE runs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    code_id INT,

    -- code interface
    std_in TEXT,
    std_out TEXT,
    std_err TEXT,
    status_code INT,

    FOREIGN KEY (code_id) REFERENCES submissions(id)
)
