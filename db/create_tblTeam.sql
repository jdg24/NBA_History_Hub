CREATE TABLE IF NOT EXISTS tblTeam (
    ID serial PRIMARY KEY,
    teamAbbr VARCHAR (5) NOT NULL,
    teamLocation VARCHAR (50) NOT NULL,
    teamName VARCHAR (50) NOT NULL
);