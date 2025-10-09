-- now that i have a column with the names of teams and stadiums will run few queries with that

-- 1. list of all home games and their stadiums 
SELECT DISTINCT "STADIUM", "TEAM STADIUM"
FROM matches 
ORDER BY "TEAM STADIUM";

-- 2. count matches played at each team stadium
--CREATE VIEW Team_with_most_matches_played AS
SELECT "TEAM STADIUM", COUNT(*) AS matches_played
FROM matches
GROUP BY "TEAM STADIUM"
ORDER BY matches_played DESC;

--3. running a query for the "match results" column for the team with the most wins
--CREATE VIEW Team_with_most_wins AS
SELECT "STADIUM","TEAM STADIUM", COUNT(*) AS Home_wins
FROM matches
WHERE "MATCH RESULTS"= 'Home win'
GROUP BY "STADIUM","TEAM STADIUM"
ORDER BY Home_wins DESC
LIMIT 10;


--4. Top 5 stadiums with the most draws
--CREATE VIEW top_5_teams_with_most_draws AS  
SELECT "TEAM STADIUM", COUNT(*) AS Draws
FROM matches
WHERE "MATCH RESULTS" ='Draw'
GROUP BY "TEAM STADIUM"
ORDER BY Draws DESC
LIMIT 5;

--5.Top scoring staiums(stadium that the most Goals was scored in)
--CREATE VIEW top_10_scoring_stadiums AS
SELECT "TEAM STADIUM",
        SUM("HOME TEAM GOALS" + "AWAY TEAM GOALS") AS total_goals
FROM matches
GROUP BY "TEAM STADIUM"
ORDER BY total_goals DESC
LIMIT 10; 