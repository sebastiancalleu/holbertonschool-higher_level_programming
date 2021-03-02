-- script to list max value of tmp of each state.

SELECT state, max(value) AS max_tmp FROM temperatures GROUP BY state ORDER BY state;