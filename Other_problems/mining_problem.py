#If the current number of robots can meet or exceed the remaining requirement
# faster by mining, then mine with all robots
# Otherwise  prioritize cloning to rapidly expand the fleet size

# The idea is that out number of robots growth is faster (it is exponential) because we are multiplying 
# number of robots x 2 each day 

def mining_problem(n):
    days = 0
    robots = 1  
    grams_mined = 0  
    
    while grams_mined < n:
        if robots >= (n - grams_mined):
            days += 1
            grams_mined += robots
        else:
            robots *= 2
            days += 1
    
    return days



n = 1000000

print(mining_problem(n))



