-- Crear la base de datos VoteStamp

CREATE DATABASE IF NOT EXISTS VoteStamp;

-- Usar la base de datos VoteStamp

USE VoteStamp;

-- Crear la tabla Votos

CREATE TABLE
    IF NOT EXISTS Votos (
        voto_id INT AUTO_INCREMENT PRIMARY KEY,
        timestamp DATETIME,
        lista VARCHAR(255),
        partido VARCHAR(255)
    );