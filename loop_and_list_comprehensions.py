def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
def has_lucky_number(nums):
    for num in nums:
        if num % 7 == 0:
            return True
    # We've exhausted the list without finding a lucky number
    return False

#print(has_lucky_number([1,2,3,7]))
#print(has_lucky_number([]))

# [1, 2, 3, 4] > 2
def elementwise_greater_than(L, thresh):
    answer = []
    for l in L:
        if l > thresh:
            answer.append(True)
        else:
            answer.append(False)

    return answer

def elementwise_greater_than2(L, thresh):
    return [ele > thresh for ele in L]

#print(elementwise_greater_than([1,2,3,4], 2))

def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    #iterate over all indices of a list, except the last one
    for i in range(len(meals)-1): 
        if meals[i] == meals[i+1]:
            return True
    return False

#print(menu_is_boring(["a", "b", "c", "d", "d", "e"]))

import random

def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    estimate_average_slot_payout(1)
    -1
    estimate_average_slot_payout(1)
    0.5
    """
    return round((random.randint(0,1) -1)/n_runs, 5)

print(estimate_average_slot_payout(5))