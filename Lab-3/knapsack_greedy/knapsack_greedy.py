def knapsack_fractional(weights, profits, capacity):
    n = len(weights)
    
    profit_density = [(profits[i] / weights[i], weights[i], profits[i], i) for i in range(n)]


    profit_density.sort(reverse=True, key=lambda x: x[0])

    total_profit = 0.0
    knapsack = [0.0] * n  
    
    for i in range(n):
        if capacity <= 0:
            break
        
        density, weight, profit, original_index = profit_density[i]
        
        if weight <= capacity:
            knapsack[original_index] = 1.0 
            total_profit += profit
            capacity -= weight
        else:
            knapsack[original_index] = capacity / weight 
            total_profit += knapsack[original_index] * profit
            capacity = 0
    
    return knapsack, total_profit



if __name__ =="__main__":
    capacity= 8
    weights=[3,4,9]
    profits=[5,10,500]
    # weights = [2, 2, 3]
    # profits = [6, 10, 12]
    # capacity = 6
    result = knapsack_fractional(weights, profits, capacity)
    print(f"Items included: {result}")