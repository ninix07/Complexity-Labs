def make_table(profits, weights,capacity):
    n= len(weights)
    dp_table= [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    for i in range(n+1):
        for w in range(1, capacity + 1):
            if weights[i-1] > w:
                dp_table[i][w]=dp_table[i-1][w]
            else:
                dp_table[i][w]=  max(dp_table[i - 1][w], profits[i - 1] + dp_table[i - 1][w - weights[i - 1]])

    return dp_table

def find_included_item( profits,weights,capacity):
    dp_table= make_table(profits, weights, capacity)
    n= len(weights)
    max_value= dp_table[n][capacity]
    included_tems=[]
    i,w= n,capacity
    while i>0 and w>0 :
        if dp_table[i][w]!= dp_table[i-1][w]:
            included_tems.append(i)
            w-=weights[i-1]
        i-=1

    included_tems.reverse()
    return max_value,included_tems


if __name__ =="__main__":
    weights = [4, 3, 2, 1, 3]
    values = [5, 2, 3, 2, 4]
    capacity = 7

    
    included_items,max_value = find_included_item(values, weights, capacity)

    print(max_value, included_items)
