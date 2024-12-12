def insertionsort(customList):
    for i in range(1,len(customList)):
        key=customList[i] # selects the first unsorted element and stores it in key
        j=i-1
        while j>=0 and key<customList[j]:
            customList[j+1]=customList[j]
            j-=1
        customList[j+1]=key
    print(customList)




cList=[2,1,4,5,9,10,6,8]

insertionsort(cList)