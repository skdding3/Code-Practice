## Queries
SELECT title, director FROM movies;

SELECT * FROM movies where id=6;

SELECT * FROM movies 
where year BETWEEN 2000 AND 2010;

SELECT * FROM movies 
where year NOT BETWEEN 2000 AND 2010;

SELECT * FROM movies
where id < 6;

SELECT * FROM movies
where title LIKE "toy%";

SELECT * FROM movies
where director !="John Lasseter";

SELECT * FROM movies
where title LIKE "WALL-_";

## Filtering and sorting Query results
SELECT DISTINCT director FROM movies
ORDER BY director;

SELECT * FROM movies
ORDER BY year DESC
LIMIT 4;

SELECT * FROM movies
ORDER BY title
LIMIT 5 OFFSET 5;

## Review
SELECT * FROM north_american_cities
WHERE country = "Canada";

SELECT * FROM north_american_cities
WHERE country LIKE "United%"
ORDER BY latitude DESC;

SELECT * FROM north_american_cities
ORDER BY longitude
LIMIT 6;

SELECT * FROM north_american_cities
WHERE country = "Mexico"
ORDER BY population DESC
LIMIT 2;

SELECT * FROM north_american_cities
WHERE country LIKE "United%"
ORDER BY population DESC
LIMIT 2 OFFSET 2;

## INNER JOIN
SELECT * FROM movies
INNER JOIN boxoffice
    ON movies.Id = Movie_id;
    
SELECT * FROM movies
INNER JOIN boxoffice
    ON movies.Id = Movie_id
WHERE domestic_sales<international_sales;

SELECT * FROM movies
INNER JOIN boxoffice
    ON movies.Id = Movie_id
ORDER BY rating DESC;

## OUTER JOIN
SELECT DISTINCT building FROM employees;

SELECT * FROM employees
LEFT JOIN Buildings 
    ON employees.Building = Buildings.Building_name;
    
SELECT DISTINCT building_name, role FROM buildings 
LEFT JOIN employees
  	ON building_name = building;
    
## NULL
SELECT name, role FROM employees
WHERE building IS NULL;

SELECT DISTINCT building_name
FROM buildings 
  LEFT JOIN employees
    ON building_name = building
WHERE role IS NULL;

## with expression 
SELECT title, (domestic_sales + international_sales) / 1000000 AS millions
FROM movies
  JOIN boxoffice
    ON movies.id = boxoffice.movie_id;
    
SELECT title, rating * 10 AS rating_percent
FROM movies
  JOIN boxoffice
    ON movies.id = boxoffice.movie_id;
    
SELECT title, year
FROM movies
WHERE year % 2 = 0;

## with aggregates 
SELECT MAX(years_employed) as Max_years_employed
FROM employees;

SELECT role, AVG(years_employed) as Average_years_employed
FROM employees
GROUP BY role;

SELECT building, SUM(years_employed) as Sum_years_employed
FROM employees
GROUP BY building;

SELECT building, SUM(years_employed) as Sum_years_employed
FROM employees
GROUP BY building;

SELECT role, COUNT(*) as Number_of_artists
FROM employees
WHERE role = "Artist";

SELECT role, SUM(years_employed)
FROM employees
GROUP BY role
HAVING role = "Engineer"; # Having은 그룹 컨디션 

## Inserting rows*/
INSERT INTO movies 
VALUES (4, "Toy Story 4", "El Directore", 2015, 90);

## Updating rows 
UPDATE movies
SET year = 1999
WHERE id = 3;

UPDATE movies
SET title = "Toy Story 3", director = "Lee Unkrich"
WHERE id = 11;

## Deleting rows 
DELETE FROM movies
where year < 2005;

## Create a new table named Database with the following columns 
CREATE TABLE Database (
    Name TEXT,
    Version FLOAT,
    Download_count INTEGER
);

## Add new columns 
ALTER TABLE Movies
  ADD COLUMN Aspect_ratio FLOAT DEFAULT 2.39;
  
ALTER TABLE Movies
  ADD COLUMN Language TEXT DEFAULT "English";
  
## Drop the table 
DROP TABLE movies;