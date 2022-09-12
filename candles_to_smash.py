def to_smash(total_candies, n = 3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    return total_candies % n


# to_smash(91) -> n=3 if to_smash(91, 4) -> n=4