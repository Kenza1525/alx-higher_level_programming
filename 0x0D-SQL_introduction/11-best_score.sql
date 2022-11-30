-- lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0
SELECT score, `name` FROM second_table
WHERE score BETWEEN 10 AND 14
ORDER BY score DESC;
