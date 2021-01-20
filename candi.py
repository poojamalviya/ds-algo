def destributeCandi(candies, num_people):
    res =[0]* num_people
    give = 1
    while(candies > 0):
        for i in range(0, num_people):
            if candies-give <= 0:
                print candies, give, "--"
                res[i] =candies
                return res
            if candies >= give:
                print candies, give
                res[i] = give
                candies -= give
                give = give +1
    

    return res







candies = 7
num_people = 4

print destributeCandi(candies, num_people)
