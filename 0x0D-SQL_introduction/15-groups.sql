-- script to list the number of records of each score.

SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;