-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--CREATE DATABASE tournament;

CREATE TABLE players (pid SERIAL primary key, 
	player_name TEXT not null);

CREATE TABLE matches (mid SERIAL primary key, 
	pid_a INTEGER not null references players(pid), 
	pid_b INTEGER not null references players(pid),
	result INTEGER not null); --0 = draw, otherwise will store pid_a or pid_b to represent the winner 

CREATE TABLE tournament (tid SERIAL primary key);

CREATE TABLE tournament_matches (tid INTEGER, foreign key (tid) references tournament(tid), 
	mid INTEGER not null references matches(mid));

CREATE TABLE tournament_players (tid INTEGER, foreign key (tid) references tournament(tid), 
	pid INTEGER, foreign key (pid) references players(pid));

CREATE VIEW count_players AS select count(*) from players;

CREATE VIEW standings AS 
select players.pid, players.player_name,
(select count(*) from matches where matches.result = players.pid) as wins, 
(select count(*) from matches where matches.pid_a=players.pid or matches.pid_b = players.pid) as matches_played 
FROM players LEFT OUTER JOIN matches ON (players.pid = matches.pid_a OR players.pid = matches.pid_b)
order by wins desc; 

--CREATE VIEW pairings AS
--select players.pid as matchup_a, players.player_name as matchup_a_name, select players.pid as matchup_b, players.player_name as matchup_b_name
