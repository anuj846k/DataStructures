# def main(n):
#     sum=0
#     for i in range(1,n+1):
#         sum=sum+i
#     print(sum)
# main(5)

# this above one is a iterative approach


# Same question using recursion
def find_sum(n):
    # if n==1:
    #     return 1
    return n+find_sum(n-1)


print(find_sum(5))