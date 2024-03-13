-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_genres.name  FROM tv_shows RIGHT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id WHERE title = "Dexter" ORDER BY tv_genres.name;
