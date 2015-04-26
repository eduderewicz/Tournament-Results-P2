#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM matches;")
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM players;")
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    c = conn.cursor()
    c.execute("select * FROM count_players;")
    count = c.fetchone() #retrieve first (only row) from count_players
    conn.commit()
    conn.close()
    return count[0]



def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    
    conn = connect()
    c = conn.cursor()
    name = str(name)
    c.execute("INSERT INTO players (player_name) VALUES (%s);", (name,))
    conn.commit()
    conn.close()
    




def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * from standings;")
   # print c.fetchall()
    standings = c.fetchall()
    conn.commit()
    conn.close()
    #print standingsDB
    return standings
    #print len(standingsDB)

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect()
    c = conn.cursor()
    #records match participants and winner 
    c.execute("INSERT INTO matches (pid_a, pid_b, result) VALUES (%s, %s, %s);", (winner,loser,winner,))
    #database is designed to handle draws, but I did not implement that part of the assignment. 
    # Where possible my design is setup to handle some extra credit but I have not implemented it yet
    #the tests aren't designed for reporting draws and would require rewriting 
    #easiest implementation would be to update this method to reportmatch(player_1, player_2, result) where result = player_1 or player_2 or draw 
    conn.commit()
    conn.close()
    
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT pid, player_name, wins from standings;")
    
    standings = c.fetchall()
    pairings = []
    
    x=0
    while x < (len(standings)-1):
        player1id = standings[x][0]
        player1name = standings[x][1]
        player2id = standings[x+1][0]
        player2name = standings[x+1][1]
        pair = (player1id, player1name, player2id,player2name) 
        # ^ this could be refactored into one line instead of using variables, but the intent is clearer this way
        
        x = x + 2
        pairings.append(pair)
        

    conn.commit()
    conn.close()
    
    return pairings
    


