CREATE DATABASE IF NOT EXISTS my_database;
USE my_database;
CREATE TABLE роли (
    id SERIAL PRIMARY KEY,
    название VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE сотрудники (
    id SERIAL PRIMARY KEY,
    имя_пользователя VARCHAR(50) NOT NULL UNIQUE,
    пароль VARCHAR(128) NOT NULL,
    роль_id INT REFERENCES роли(id),
    создано TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE категории (
    id SERIAL PRIMARY KEY,
    название VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE статусы (
    id SERIAL PRIMARY KEY,
    название VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE задачи (
    id SERIAL PRIMARY KEY,
    заголовок VARCHAR(200) NOT NULL,
    описание TEXT,
    создано TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    дата_окончания TIMESTAMP,
    статус_id INT REFERENCES статусы(id),
    категория_id INT REFERENCES категории(id),
    сотрудник_id INT REFERENCES сотрудники(id),
    создатель_id INT REFERENCES сотрудники(id)
);
INSERT INTO роли (название) VALUES ('Руководитель'), ('Сотрудник');

INSERT INTO сотрудники (имя_пользователя, пароль, роль_id) 
VALUES ('ivan', 'password123', 1), 
       ('anna', 'mypassword', 2);

INSERT INTO категории (название) VALUES ('Разработка'), ('Тестирование');

INSERT INTO статусы (название) VALUES ('Новая'), ('В процессе'), ('Завершена');

INSERT INTO задачи (заголовок, описание, дата_окончания, статус_id, категория_id, сотрудник_id, создатель_id) 
VALUES ('Создать API', 'Создание REST API', '2023-11-01', 1, 1, 1, 1),
       ('Тестирование функционала', 'Тестирование нового функционала', '2023-11-10', 1, 2, 2, 1);
       