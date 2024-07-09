def knapsack_non_fractional(weights, profit, capacity):
    length = len(weights)
    binary_combination = []
    greatestProfit = 0
    total_iterations = 2 ** length
    
    for i in range(total_iterations):
        temp_binary_combination = []
        temp_profit = 0
        temp_capacity = capacity
        n = i
        
        for j in range(length):
            temp_binary_combination.append(n % 2)
            temp_profit += (n % 2) * profit[j]
            temp_capacity -= (n % 2) * weights[j]
            n = n // 2
        if temp_profit > greatestProfit and temp_capacity >= 0:
            binary_combination = temp_binary_combination.copy()
            greatestProfit = temp_profit
            
    
    return binary_combination
        

if __name__ =="__main__":
    weights = [2, 2, 2]
    profits = [10, 20, 30]
    capacity = 4
    result = knapsack_non_fractional(weights, profits, capacity)
    print(f"Items included: {result}")