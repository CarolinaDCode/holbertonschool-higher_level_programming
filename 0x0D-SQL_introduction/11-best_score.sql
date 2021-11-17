-- Escriba un script que enumere todos los registros con una puntuación > = 10
-- en la tabla second_table de la base de datos hbtn_0c_0 en su servidor MySQL.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;