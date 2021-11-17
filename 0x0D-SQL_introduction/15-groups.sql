-- Escriba un script que enumere el número de registros con la misma puntuación
-- en la tabla second_table de la base de datos hbtn_0c_0 en su servidor MySQL.
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;