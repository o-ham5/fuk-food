use api-db;

CREATE TABLE tests (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    user VARCHAR(50),
    mail VARCHAR(50),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

INSERT INTO tests (user, mail) VALUES ("test01", "test01@example.com");
INSERT INTO tests (user, mail) VALUES ("test02", "test02@example.com");