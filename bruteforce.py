from itertools import combinations
import time
import pandas as pd


def best_share_combination(file_path, budget):
    """
    Function calculating the best shares to buy within the amount of the max budget
    :param file_path: path of the csv file containing the datas
    :param budget: {int} total budget to buy shares
    :return: max_profit: {float} total profit for the selected shares
    :return: best_combination: list of all the best shares to buy
    :return: best_cost: total cost of shares within the range of the budget
    :return: elapsed_time: time for the bruteforce.py to resolve the algorithm
    :return: efficiency: {float%} ((y2 - y1) / y1) * 100 gives the % of efficiency
    """
    start_time = time.time()
    data = pd.read_csv(file_path)

    # Calculate actual profit for each share based on the percentage
    data['actual_profit'] = data['price'] * (data['profit'] / 100)

    max_profit = 0
    best_combination = None
    best_cost = 0

    # Generate combinations of shares
    for r in range(1, len(data) + 1):
        for combination in combinations(data.iterrows(), r):
            total_cost = 0
            total_profit = 0

            # Check total cost and profit for each combination
            for index, share in combination:
                total_cost += share['price']
                total_profit += share['actual_profit']

            # Check if the combination is affordable and has maximum profit
            if total_cost <= budget and total_profit > max_profit:
                max_profit = total_profit
                best_combination = [share[1]['name'] for share in combination]
                best_cost = total_cost

    efficiency = ((best_cost + max_profit) - best_cost) / best_cost * 100
    end_time = time.time()
    elapsed_time = end_time - start_time

    return best_combination, max_profit, best_cost, elapsed_time, efficiency


file_path = 'shares.csv'
budget = 500

best_combination, max_profit, best_cost, elapsed_time, efficiency = best_share_combination(file_path, budget)

print(f"The best combination of shares to buy is: {best_combination}")
print(f"Total of shares: {len(best_combination)}")
print(f"Total profit: {max_profit:.2f} euros.")
print(f"Total cost: {best_cost:.2f} euros.")
print(f"Total efficiency: {efficiency:.2f} %")
print(f"Time taken: {elapsed_time:.2f} seconds")
