def knapsack_fractional(weights, profits, capacity):
    length = len(weights)
    best_combination = [0] * length
    greatest_profit = 0.0
    remaining_capacity = 0.0

    total_iterations = 2 ** length

    for i in range(total_iterations):
        temp_combination = [0] * length
        temp_profit = 0.0
        temp_capacity = capacity
        n = i

        for j in range(length):
            curr_binary = n % 2
            n = n // 2

            if curr_binary == 1:
                if weights[j] <= temp_capacity:
                    temp_combination[j] = 1
                    temp_profit += profits[j]
                    temp_capacity -= weights[j]

        if temp_capacity > 0: # if there is some space left, filling with fractional weights
            frac_best_combination = temp_combination[:]
            frac_best_profit = temp_profit

            for k in range(length):
                if temp_combination[k] == 0:

                    fraction = min(1, temp_capacity / weights[k])
                    frac_temp_profit = temp_profit + fraction*profits[k]

                    if frac_temp_profit > frac_best_profit:
                        frac_best_profit = frac_temp_profit
                        frac_best_combination = temp_combination[:]
                        frac_best_combination[k] = fraction

            temp_combination = frac_best_combination
            temp_profit = frac_best_profit
            temp_capacity = 0

        if temp_profit > greatest_profit:
            best_combination = temp_combination[:]
            greatest_profit = temp_profit
            remaining_capacity = temp_capacity

    return best_combination, remaining_capacity, greatest_profit