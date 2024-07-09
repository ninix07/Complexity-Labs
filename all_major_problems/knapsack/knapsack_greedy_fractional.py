def knapsack_greedy(profits, weights, capacity):
    n= len(weights)
    density= [(profits[i]/weights[i],profits[i],weights[i],i) for i in range(n)]
    density.sort(key= lambda x: x[0],reverse=True)
    indexes= [0]*n
    total_profit=0
    for i in range(n):
        if capacity <= 0:
            break
        profit_density, profit, weight, index= density[i]
        if weight<= capacity:
            total_profit += profit
            capacity -= weight
            indexes[i]=1
        else:
            indexes[i]= capacity/weight
            total_profit += indexes[i] * profit
            capacity = 0
    return indexes[::-1], total_profit    

if __name__ =="__main__":
    # capacity= 8
    # weights=[3,4,9]
    # profits=[5,10,500]
    weights = [2, 2, 3]
    profits = [6, 10, 12]
    capacity = 6
    result = knapsack_greedy(profits, weights, capacity)
    print(f"Items included: {result}")