import sys
def dynamic_matrix_chain_multiplication(dimensions: list[int]):
    n = len(dimensions) - 1
    # creating a table of length n*n to store the results
    tab = [[None for _ in range(n)] for _ in range(n)]

    # There is no multiplication required for single matrix
    for i in range(n):
        tab[i][i] = 0

    # for storing the sequence which produced minimum multiplications
    s = [[None for _ in range(n - 1)] for _ in range(n - 1)]

    for chain_length in range(1, n):
        for i in range(n - chain_length):
            j = i + chain_length
            min_multiplications = sys.maxsize
            for k in range(i + 1, j + 1):
                current_multiplications = (
                    tab[i][k - 1]
                    + tab[k][j]
                    + dimensions[i] * dimensions[k] * dimensions[j + 1]
                )
                if current_multiplications < min_multiplications:
                    min_multiplications = current_multiplications
                    tab[i][j] = min_multiplications
                    s[i][j - 1] = k
    print(s)
    return tab[0][n - 1]

if __name__ =="__main__":
    dimensions = [5, 4, 6, 2, 7]
    
    print(dynamic_matrix_chain_multiplication(dimensions))