def merge(customList, l, m, r):
    # Find the lengths of two subarrays
    n1 = m - l + 1
    n2 = r - m
    
    # Create temporary arrays for left and right subarrays
    L = [0] * n1
    R = [0] * n2
    
    # Copy data into the temporary arrays
    for i in range(0, n1):
        L[i] = customList[l + i]
    
    for j in range(0, n2):
        R[j] = customList[m + 1 + j]
    
    # Merge the temporary arrays back into the original customList
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1
    
    # Copy any remaining elements from L (if any)
    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1
    
    # Copy any remaining elements from R (if any)
    while j < n2:
        customList[k] = R[j]
        j += 1
        k += 1

def mergeSort(customList, l, r):
    if l < r:
        m = (l + r) // 2  # Corrected middle index calculation
        mergeSort(customList, l, m)       # Recursively sort the left half
        mergeSort(customList, m + 1, r)   # Recursively sort the right half
        merge(customList, l, m, r)        # Merge the sorted halves
    return customList

# Example list
cList = [2, 1, 4, 5, 9, 10, 6, 8]
print(mergeSort(cList, 0, len(cList) - 1))  # Fix the range to the last index
