def NumOfOption(priceOfJeans, priceOfShoe, priceOfSkirt, priceOfTop, budged):
    total = 0
    array = []
    if len(priceOfJeans)==1:
        total +=priceOfJeans[0]
    if len(priceOfShoe)==1:
        total +=priceOfShoe[0]
    if len(priceOfSkirt)==1:
        total +=priceOfSkirt[0]
    if len(priceOfTop)==1:
        total +=priceOfTop[0]
    if total> budged:
        return 0
    if len(priceOfJeans)>1:
        array.append(priceOfJeans)
    if len(priceOfShoe)>1:
        array.append(priceOfShoe)
    if len(priceOfSkirt)>1:
        array.append(priceOfSkirt)
    if len(priceOfTop)>1:
        array.append(priceOfTop)
    if len(array) == 0 and budged>= total:
        return 1
    count = 0
    def dfs(index, budged, )


priceOfJeans= [2,3]
priceOfShoe= [4]
priceOfSkirt = [2,3]
priceOfTop = [1,2]
budged = 10

NumOfOption(priceOfJeansm, priceOfShoe, priceOfSkirt, priceOfTop, budged)