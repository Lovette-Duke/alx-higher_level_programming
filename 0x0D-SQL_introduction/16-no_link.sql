-- lists all record where name is not NULL and ordered by score in decending order

SELECT score, name 
FROM second_table
WHERE name IS NOT NULL 
ORDER BY score DESC;
