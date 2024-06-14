-- dags/sql/birth_date.sql
SELECT * FROM pet
WHERE birth_date BETWEEN SYMMETRIC '2020-01-01' AND '2020-12-31';