CREATE TABLE IF NOT EXISTS tblSeason (
    ID serial PRIMARY KEY,
    seasonYear INT NOT NULL,
    seasonText VARCHAR (10) NOT NULL,
    toScrape BOOLEAN NOT NULL
);
