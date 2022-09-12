def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    return L[1] if len(L) >1 else None

#L = [1, 2, 3]
#print(select_second(L))

def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    return teams[-1][1]

#teams = [["a","b","c"],["a","b","c"],["a","b","c"]]
#print(losing_team_captain(teams))

def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    r = ["Mario", "Bowser", "Luigi"]
    purple_shell(r)
    r
    ["Luigi", "Bowser", "Mario"]
    """
    temp = racers[0]
    racers[0] = racers[-1]
    racers[-1] = temp
    return racers