
# Problem Statement: Given an integer N, return the number of digits in N

N = int(input("Enter the number :"))

# count = 0 
# for i in range(1,len(str(N))+1):
#     count+=1
# print("The no of digits in the input are: ",count)




count = 0 
for i in range(1,len(str(N))+1):
    if(N%i==0):
        count+=1
print("The no of digits evenly: ",count)

