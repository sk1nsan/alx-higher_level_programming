-- lists all records of the table second_table of the database hbtn_0c_0
SELECT city, AVG(value) as avg_temp from temperatures WHERE month in (7, 8) group by city ORDER BY avg_temp DESC LIMIT 3;
