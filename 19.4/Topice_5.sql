SELECT DISTINCT language 
FROM movies;

SELECT DISTINCT year 
FROM movies 
WHERE genre IN ('Drama', 'Action');

SELECT DISTINCT year 
FROM movies 
WHERE genre IN ('Drama', 'Action');

SELECT DISTINCT genre, language 
FROM movies 
ORDER BY language;

SELECT COUNT(DISTINCT genre) AS distinct_genre_count 
FROM movies;
