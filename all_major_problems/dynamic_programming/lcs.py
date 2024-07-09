def LCS_dp(X,Y):
    m= len(X)
    n=len(Y)
    L=[[0 for _ in range(n+1)] for  _ in range(m+1)]
    subsequence=""
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
   
    i,j=m,n
    while i >0 and j >0:
            if L[i][j]!=max(L[i-1][j],L[i][j-1]):
                subsequence += X[i - 1]
                i -= 1
                j -= 1
            elif L[i - 1][j] >= L[i][j - 1]:
                i -= 1
            else:
                j -= 1

    return L[m][n], subsequence[::-1]

if __name__ =="__main__":
    X = "atmosphere"
    Y = "stratosphere"
    print("Length of LCS is ", LCS_dp(X, Y)) 
