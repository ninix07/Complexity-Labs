def knapsack_0_1(profits, weights, capacity):
    length= len(profits)
    binary_combination=[]
    greatest_profit=0
    rem_capacity=0
    iterations= 2**length
    for i in range(0,iterations):
        temp_binary=[]
        temp_profit=0
        temp_rem_capacity=capacity
        n=i
        for j in range(length):
            curr_bin= n%2
            temp_binary.append(curr_bin)
            temp_profit+= curr_bin*profits[j]
            temp_rem_capacity-= curr_bin*weights[j]
            n=n//2
        if temp_profit > greatest_profit and temp_rem_capacity >=0 :
            greatest_profit=temp_profit
            rem_capacity= temp_rem_capacity
            binary_combination= temp_binary.copy()
    return binary_combination, rem_capacity,greatest_profit

if __name__ =="__main__":
    weights = [2, 2, 2]
    profits = [10, 20, 30]
    capacity = 4
    result = knapsack_0_1( profits, weights, capacity)
    print(f"Items included: {result}")