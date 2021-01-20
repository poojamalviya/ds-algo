def TowerOfHanoi(n, frm, to, aux):
    if n== 1:
        print ("move 1 disk from: "+ frm + " to: " + to)
        return
    TowerOfHanoi(n-1, frm, aux, to)
    print ("move " + str(n) + " disk from: " + frm + " to: " + to)
    TowerOfHanoi(n-1, aux, to, frm)


n = 3
TowerOfHanoi(n, 'A', 'C', 'B') 