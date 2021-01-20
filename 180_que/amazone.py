def movie(time, n, arr):
    endtime = time-30
    res =[0,0]
    restime=0
    for i in range(len(arr)):
       for j in range(i+1, len(arr)):
           if arr[i]+arr[j]<=endtime and restime<=arr[i]+arr[j]:
                restime = arr[i]+arr[j]

                res[0], res[1]=i, j
            
    return tuple(res)
    
def IDsOfmovies(flightDuration, numMovies, movieDuration):
    endtime = flightDuration-30
    res =[0,0]
    restime =0
    for i in range(len(movieDuration)):
        for j in range(i+1,len(movieDuration)):
            if movieDuration[i]+movieDuration[j]<=endtime and restime<=movieDuration[i]+movieDuration[j]:
                restime = movieDuration[i]+movieDuration[j]
                res[0], res[1]=i, j
    
    return tuple(res)


print movie(250,5, [100,180,40,120,10])
print IDsOfmovies(250,5, [100,180,40,120,10]) 220
