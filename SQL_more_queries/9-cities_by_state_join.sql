-- lists cities.id, cities.name, and states.name for all cities, sorted by cities.id
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC;
