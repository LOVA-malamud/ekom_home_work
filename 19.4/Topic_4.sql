SELECT 
    title AS movie_name, 
    genres AS type, 
    release_year AS release_year, 
    rating * 10 AS rating_bucket
FROM netflix_movies
ORDER BY rating_bucket DESC, movie_name ASC;

SELECT title, genres, release_year, rating * 10
FROM netflix_movies
ORDER BY rating * 10 DESC, title ASC;
