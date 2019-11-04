CREATE TABLE artists (
	artistID INTEGER PRIMARY KEY, 
    artistName TEXT
);

CREATE TABLE albums (
	albumID INTEGER PRIMARY KEY, 
    albumName TEXT,
    artistID INTEGER
);

CREATE TABLE songs (
	songID INTEGER PRIMARY KEY,
    trackID INTEGER,
    trackLength TIME,
    aName TEXT
);