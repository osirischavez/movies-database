CREATE DATABASE moviesdb2;
\c moviesdb2;


CREATE TABLE movies(
	id INT PRIMARY KEY,
	title CHAR(150),
	vote_average REAL,
	vote_count INT);

CREATE TABLE people(
	id INT PRIMARY KEY,

	name CHAR(60));

CREATE TABLE crew(
	id_credit CHAR(30) PRIMARY KEY,
	id_people INT,
	job_crew CHAR(60),
	id_movie INT,
	FOREIGN KEY (id_people) REFERENCES people (id),
	FOREIGN KEY (id_movie) REFERENCES movies (id));

CREATE TABLE actors(
	id_credit CHAR(30) PRIMARY KEY,
	id_people INT,
	id_movie INT,
	FOREIGN KEY (id_people) REFERENCES people (id),
	FOREIGN KEY (id_movie) REFERENCES movies (id));

CREATE TABLE movies_genres(
	id INT PRIMARY KEY,
	name_genres CHAR(40));

CREATE TABLE rel_movies_genres(
	id_genres INT,
	id_movie INT,
	FOREIGN KEY (id_genres) REFERENCES movies_genres (id),
	FOREIGN KEY (id_movie) REFERENCES movies (id));

CREATE INDEX indexcrew1 
ON crew (id_people);
CREATE INDEX indexcrew2 
ON crew (id_movie);
CREATE INDEX indexcrew3 
ON crew (job_crew);
CREATE INDEX indexact1 
ON actors (id_people);
CREATE INDEX indexact2 
ON actors (id_movie);
CREATE INDEX indexrel1 
ON rel_movies_genres (id_genres);
CREATE INDEX indexrel2 
ON rel_movies_genres (id_movie);

