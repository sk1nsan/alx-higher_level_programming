-- lists all the cities of California that can be found in the database
SELECT title, genre_id  FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY title, genre_id;
