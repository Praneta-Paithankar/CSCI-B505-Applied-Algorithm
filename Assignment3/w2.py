# Matrix = [[0 for x in range(w)] for y in range(h)]

def find_subset(numbers,sum):
    n=len(numbers)+1
    mat =[[0 for x in range(sum+1)] for y in range(n)]
    #mat no sum
    # sum ==0
    for i in range(n):
        mat[i][0]=True


    # n==0 and sum!=0
    for i in range(sum+1):
        mat[0][i]=False

    #otherm ,
    for i in range(1,n):
        for j in range(1,sum+1):
            if j-numbers[i-1]>=0:
                mat[i][j]=mat[i-1][j] or mat[i-1][j-numbers[i-1]]
            else:
                mat[i][j]=mat[i-1][j]

    return mat[len(numbers)][sum]

numbers=[5,8]
a=find_subset(numbers,7)
print a
