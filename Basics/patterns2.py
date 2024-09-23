# --------------------------------------DAY4----------------------------------------------------


n= int(input("Enter the number :"))

# Level 2 patterns Questions

# Pattern 12 output

# 1    1
# 12  21
# 123321



# --------------------------------------DAY5----------------------------------------------------


# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     spaces = 2 * (n - i)  
#     for j in range(spaces):
#         print(" ",end=" ")
#     for j in range(i,0,-1):  
#         print(j,end="")
#     print()


# Pattern 13 output


# 1
# 2  3
# 4  5  6
# 7  8  9  10
# 11  12  13  14  15
# 16  17  18  19  20  21
# count=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(count,end=" ")
#         count +=1
#     print()




# Pattern 14 output

 # A
 # A B
 # A B C
 # A B C D
 # A B C D E
 # A B C D E F

# for i in range(1,n+1):
#     for ch in range(ord('A'),ord('A')+i):
#         print(chr(ch),end=" ")
#     print()



# for i in range(1,n+1):
#     for ch in range(ord('A'),ord('A')-i,):
#         print(chr(ch),end=" ")
#     print()





# Pattern 15 output

# A B C D E F
# A B C D E 
# A B C D
# A B C
# A B
# A

for i in range(1,n+1):
    for ch in range(ord('A'),ord('A')+(n-i)+1):
        print(chr(ch),end=" ")
    print()