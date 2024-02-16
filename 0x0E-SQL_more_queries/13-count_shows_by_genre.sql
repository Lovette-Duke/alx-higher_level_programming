-- lists all genres and counts the number of show in each genre

SELECT tv_genres.name AS genre, COUNT(*) AS 'number_of_shows'
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows;
