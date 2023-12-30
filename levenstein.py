def levenstein(a, b):
    la = len(a) + 1
    lb = len(b) + 1
    dist=[[0 for _ in range(lb)] for _ in range(la)]

#dist[0][1] = dist('','j' ) = 1 = dist(a[0:0], b[0:1])
#dist[4][3] = dist('huhgh','jij') = = dist(a[0:5], b[0:3]) final result

    for j in range(lb):
        dist[0][j] = j 

    for i in range(la):
        dist[i][0] = i 

    def pri(la,lb,a,b,dist):
        print( " " * (la + 2), end = " ")
        for j in range(lb): 
            print(str(b[0:j]), end = " ")

        print()

        for i in range(la): 
            print(str(a[0:i]), end = " ")
            print( " " * (la - i), end = " ")
            for j in range(lb): 
                print(str(dist[i][j]), end = " ")    
            print()

    #pri(la,lb,a,b,dist)
            
    def pr(la,lb,a,b,dist):    
        for i in range(la):
            for j in range(lb):
                print(" distance between  " + str(a[0:i]) +  "  and  " + str(b[0:j])+ ' is =' + str(dist[i][j]))
    #pr(la,lb,a,b,dist)
                
    for j in range(1,lb):   
        for i in range(1,la):          
            curr = a[i-1]            
            rez = len(b) + len(a)
            for k in range(j):            
                if b[k] == curr:
                    rez_kandidat = dist[i-1][k] + (j - 1 - k)
                else:
                    rez_kandidat = dist[i-1][k] + (j - 1 - k) + 1
                if rez > rez_kandidat:
                    rez = rez_kandidat
            dist[i][j] = rez    

    return dist[la-1][lb-1]    

a = '4545454' 
b = '4545d54' 
print(" distance between  " + str(a) +  "  and  " + str(b)+ ' is =' + str(levenstein(a, b)))