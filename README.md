# Tournament-Results-P2
Project 2 - Code to simulate a basic Swiss style Tournament with match reporting and matchup generating.

Requirements:
Must have PostgreSQL, Vagrant VM

Execute tournament.sql to create the tournament database from within Vagrant vm:  
`\i tournament.sql`  
This will create the tournament database and necessary tables 
Exit psql  
`\q`  
Execute tournament_test.py to run the test cases and simulate adding players, deleting players, 
reporting matches, and generating next match pairings  
`python tournament_test.py`
