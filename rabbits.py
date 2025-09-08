def recurrence(n, k):
    population = 0
    for i in range(k-1):
        population += (n-1+n-2)
        n = population
    return population+1 #addind first pair

print(recurrence(5, 3))