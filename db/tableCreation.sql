/*
tblTeam
Id - identify
abbr - vc 5
location - vc 5
name - vc 5
*/

CREATE TABLE IF NOT EXISTS tblTeam (
    ID serial PRIMARY KEY,
    teamAbbr VARCHAR (5) NOT NULL,
    teamLocation VARCHAR (50) NOT NULL,
    teamName VARCHAR (50) NOT NULL
);

CREATE TABLE IF NOT EXISTS tblGame (
    ID serial PRIMARY KEY,
    teamPoints INT NOT NULL,
    opponentPoints INT NOT NULL,
    teamID INT NOT NULL,
    opponentID INT NOT NULL,
    gameDate DATE NOT NULL
);

INSERT INTO tblTeam (teamAbbr, teamLocation, teamName) VALUES 
('LAL', 'Los Angeles','Lakers'), ('BOS', 'Boston', 'Celtics');

INSERT INTO tblGame (teamPoints, opponentPoints, teamID, opponentID, gameDate) VALUES
(100,118,6,7,'4/1/2018');
SELECT * FROM tblGame;

SELECT
    team.teamlocation,
    team.teamname,
    game.teampoints,
    opponent.teamlocation as opponentlocation,
    opponent.teamname as opponentname,
    game.opponentpoints
FROM tblGame game
INNER JOIN tblTeam team 
    ON game.teamID = team.id
INNER JOIN tblTeam opponent
    ON game.opponentID = opponent.id;