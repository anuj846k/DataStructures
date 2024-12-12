#  Bubble sort 
def BubbleSort(customList):
    for i in range(len(customList)-1):    # the outer loop make sure the largest unsorted element is moved to its correct position.
        for j in range(len(customList)-i-1): # actually compares and swapes the adjacent elements 
            if customList[j]>customList[j+1]:
                customList[j],customList[j+1]=customList[j+1],customList[j]
    print(customList)
    
cList=[2,3,4,6,1,5,10,0]
BubbleSort(cList)




# Explanation:
# The outer loop controls how many times we need to repeat the sorting process 
# outer loop ensures we keep making passes until the entire array is sorted.



# The Inner loops does the pairwise comparisons and swaps
#  for j in range(len(customList)-i-1): it runs the inner loop and ignore the largest element on every loop 
# without outer loop  the inner loop will run only once and The rest of the elements would remain out of order.
