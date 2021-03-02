-- script that list city with their average temperature.

SELECT city, AVG(value) FROM temperatures GROUP BY city ORDER BY AVG(value) DESC;