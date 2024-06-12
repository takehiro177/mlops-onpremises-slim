-- dags/sql/birth_date.sql
SELECT * FROM pet WHERE birth_date BETWEEN SYMMETRIC {{ params.begin_date }} AND {{ params.end_date }};