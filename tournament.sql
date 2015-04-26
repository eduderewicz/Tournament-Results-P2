-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE DATABASE tournament;

\c tournament;
--connect to database to create tables and views inside the tournament database

CREATE TABLE players (pid SERIAL primary key, 
	player_name TEXT not null);
-- could hold more player related info, e.g. address, email, etc

CREATE TABLE matches (mid SERIAL primary key, 
	pid_a INTEGER not null references players(pid), 
	pid_b INTEGER not null references players(pid),
	result INTEGER not null); --0 = draw, otherwise will store pid_a or pid_b to represent the winner 




CREATE VIEW count_players AS select count(*) from players;

CREATE VIEW standings AS 
select players.pid, players.player_name,
(select count(*) from matches where matches.result = players.pid) as wins, 
(select count(*) from matches where matches.pid_a=players.pid or matches.pid_b = players.pid) as matches_played 
FROM players LEFT OUTER JOIN matches ON (players.pid = matches.pid_a OR players.pid = matches.pid_b)
order by wins desc; 
--left outer join ensures players with 0 matches played have a result



--This would be important if we wanted to track more than 1 tournament (extra credit portion)
--CREATE TABLE tournament (tid SERIAL primary key);
-- could hold more tournament specific info such as location, time, venue, etc

--IGNORE below here______
--CREATE TABLE tournament_matches (tid INTEGER, foreign key (tid) references tournament(tid), 
--	mid INTEGER not null references matches(mid));

--CREATE TABLE tournament_players (tid INTEGER, foreign key (tid) references tournament(tid), 
--	pid INTEGER, foreign key (pid) references players(pid));

