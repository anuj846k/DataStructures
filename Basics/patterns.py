# Given n an integer print the following pattern:

# --------------------------------------DAY1----------------------------------------------------



#Pattern 1 Output: 
# * * *
# * * *
# * * *
n = int(input("Enter the number :"))
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()



#Pattern 2 Output: 
# * 
# * * 
# * * * 
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()  



#Pattern 3 Output: 
# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6

# for i in range(1,n+1):
#     for j in range(1, i+1):
#         print(j,end=" ")
#     print()    


# Pattern 4 Output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6

# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end=' ')
#     print()    



# Pattern 5 Output:
# * * * * * *
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()    


# --------------------------------------DAY2----------------------------------------------------


# Pattern 6 Output:
# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2 
# 1

# for i in range(n,0,-1):
#     for j in range(i):   #This will run till i-1
#         print(j+1,end=" ")   
#     print()



    
# Pattern 7 Output
#   *  
#  *** 
# *****

# for i in range(0,n):
#     for j in range(0,n-i-1):
#         print(" ",end=" ")

#     for j in range(0,(2*i+1)):
#         print("*",end=" ")
    
#     for j in range(0,n-i-1):
#         print(" ",end="")

#     print()



# Pattern 8 Output
# *****  
#  ***
#   *  


# for i in range(0,n):
#     for j in range(0,i):
#         print(" ",end=" ")

#     for j in range(0,(2*n-(2*i+1))):
#         print("*",end=" ")
    
#     for j in range(0,i):
#         print(" ",end="")

#     print()





# Pattern 9 Output

#   *  
#  ***
# ***** 
# *****  
#  ***
#   *  


# for i in range(0,n):
#     for j in range(0,n-i-1):
#         print(" ",end=" ")

#     for j in range(0,(2*i+1)):
#         print("*",end=" ")
    
#     for j in range(0,n-i-1):
#         print(" ",end="")

#     print()

# for i in range(0,n):
#     for j in range(0,i):
#         print(" ",end=" ")

#     for j in range(0,(2*n-(2*i+1))):
#         print("*",end=" ")
    
#     for j in range(0,i):
#         print(" ",end="")

#     print()


# --------------------------------------DAY3----------------------------------------------------




# Pattern 10 Output
#   *  
#   **
#   ***  
#   **
#   *  


# for i in range(1,(2*n-1)+1):
#     if i>n:
#         for j in range(1,(2*n-i)+1):
#             print("*",end=" ")
#     else:
#         for j in range(1,i+1):
#             print("*",end=" ")
#     print() 





# Pattern 11 Output

# 1
# 01
# 101
# 0101
# 10101
# 010101


for i in range(1,n+1):
    for j in range(1,i+1):
        if((i+j)%2 ==0):
            print(0,end=" ")
        else:
            print(1,end=" ")
                        
    print()         









# Extra Questions 

# THis is the output
# 1 * * * *
# 1 2 * * * 
# 1 2 3 * * 
# 1 2 3 4 *
# 1 2 3 4 5



# for i  in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     for j in range(1,(n-(i-1))):
#         print("*",end=' ')
#     print()    


# This is the output
# 1 
# **
# 1 2 3
# * * * * 
# 1 2 3 4 5


# DOUBT
# for i in range(1, n+1):
#     if i % 2 != 0:
#         for j in range(1, i+1):
#             print(j, end=" ")
#     else:
#         for j in range(0, i):
#             print("*", end=' ')
#     print()