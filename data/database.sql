CREATE DATABASE usuarios;

USE usuarios;

CREATE TABLE usuarios (
  id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
  usuario VARCHAR(25),
  nombre VARCHAR(30),
  contrasenia VARCHAR(20)
);

