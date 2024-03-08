CREATE DATABASE book_review;

USE book_review;

CREATE TABLE user (
    id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(191) NOT NULL, email VARCHAR(191) NOT NULL, password VARCHAR(191) NOT NULL, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE book (
    id INT PRIMARY KEY AUTO_INCREMENT, title VARCHAR(191) NOT NULL, price INTEGER NOT NULL, description TEXT(191), created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE book_review (
    id INTEGER PRIMARY KEY auto_increment, book_id INTEGER NOT NULL, email VARCHAR(100) NOT NULL, rating INTEGER NOT NULL, review_content TEXT NOT NULL, created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO
    book_review (
        book_id, email, rating, review_content
    )
VALUES (
        1, 'test@gmail.com', 4, 'Good'
    );

INSERT INTO
    book_review (
        book_id, email, rating, review_content
    )
VALUES (1, 'test@gmail.com', 2, 'Bad');

INSERT INTO
    book_review (
        book_id, email, rating, review_content
    )
VALUES (
        1, 'test@gmail.com', 5, 'Oustanding'
    );

DESCRIBE user;

DESCRIBE book;

SHOW TABLES;

SELECT * FROM user;

SELECT * FROM book;

SELECT * FROM book_review;