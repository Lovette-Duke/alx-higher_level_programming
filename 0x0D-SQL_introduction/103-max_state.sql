-- lists the max temperature foreach state ordered by the state name

SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
