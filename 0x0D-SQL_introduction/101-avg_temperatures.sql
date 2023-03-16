-- Script displays the average temperature (F) by city ordered by temps (descending)
SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY city ORDER BY AVG(value) DESC;
