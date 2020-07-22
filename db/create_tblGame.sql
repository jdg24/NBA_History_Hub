CREATE TABLE IF NOT EXISTS tblGame (
    ID serial PRIMARY KEY,
    teamPoints INT NOT NULL,
    opponentPoints INT NOT NULL,
    teamID INT NOT NULL,
    opponentID INT NOT NULL,
    gameDate DATE NOT NULL
);
