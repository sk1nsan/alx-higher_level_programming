--  lists all Comedy shows in the database.
SELECT tv_shows.title FROM tv_shows RIGHT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id WHERE tv_genres.name = 'Comedy' ORDER BY title;
