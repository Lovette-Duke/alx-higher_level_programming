-- lists all genres and counts the number of show in each genre

SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres
JOIN tv_shows
ON tv_genres.show_id = tv_shows.id
GROUP BY genre
ORDER BY number_of_shows;
