-- BASES
-- Se pueden abrir tantas conexiones como sea pero solo 1 escribe.
-- Transactions: pasan todas o ninguna
-- commiting: hace los cambio reales en la DB, Rollingback. Deshace los cambios de 1 transacción
CREATE TABLE IF NOT EXISTS users (first_name TEXT, surname TEXT);

-- CURSORES
-- una estructura que nos permite recorrer un conjunto de resultados
-- los cursores de la base de datos permiten que la base de datos solo cargue los resultados cuando se solicite
-- El cursor trae toda la data pero podemos acceder a ella 1 a 1 por ejemplo con for loop

INSERT INTO entries VALUES ('Today I learned about SQLite', '2020-06-01');
INSERT INTO entries VALUES ('I''ve continued to learn about SQLite!', '2020-06-02');

-- Clause WHERE
... WHERE (age <= 18 OR age >= 65) AND salary > 0;

SELECT first_name, surname, age, salary FROM users WHERE (age <= 18 OR age >= 65) AND salary > 0;
SELECT first_name, surname, age, salary
FROM users
WHERE (age <= 18 OR age >= 65) AND salary > 0;

-- CLause DROP
DROP TABLE IF EXISTS users;

-- SQL more secure on Python
GET_USER = "SELECT * FROM users WHERE first_name = ?;"
cursor.execute(GET_USER, (username, ))