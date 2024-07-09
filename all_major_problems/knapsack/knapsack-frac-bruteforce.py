def knapsack_frac_bruteforce(weights, profits, capacity):
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
            n=n//2                                                                  #same as 0/1
        if temp_rem_capacity>0:                                                     #checking if there is remaining capacity
            frac_best_combination = temp_binary[:]                                  #initializing fractional combination,profit and rem capacity
            frac_best_profit = temp_profit                                          
            frac_rem_capacity= temp_rem_capacity
            for k in range(length):                                                 #iterate over every element of the binary combination
                if temp_binary[k]==0:                                               #only check 0 for capacity
                    fraction = min(1, temp_rem_capacity / weights[k])               # if the fraction is more than 1 all element can be put there so take 1
                    frac_temp_profit = temp_profit + fraction*profits[k]
                    frac_rem_capacity-=fraction*weights[k]
                    if frac_temp_profit > frac_best_profit:
                        frac_best_profit = frac_temp_profit
                        frac_best_combination = temp_binary[:]
                        frac_best_combination[k] = fraction
            temp_binary = frac_best_combination
            temp_profit = frac_best_profit
            temp_rem_capacity =frac_rem_capacity

        if temp_profit > greatest_profit and temp_rem_capacity==0:
            greatest_profit=temp_profit
            rem_capacity= temp_rem_capacity
            binary_combination= temp_binary.copy()
    return binary_combination, rem_capacity,greatest_profit


if __name__ =="__main__":
    weights = [2, 2, 2]
    profits = [10, 20, 30]
    capacity = 5
    result = knapsack_frac_bruteforce( weights, profits, capacity)
    print(f"Items included: {result}")