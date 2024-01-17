import pandas as pd
import time


def best_share_combination(file_path, budget):
    """
    Function calculating the best shares to buy within the amount of the max budget
    :param file_path: path of the csv file containing the datas
    :param budget: {int} total budget to buy shares
    :return: total_profit: {float} total profit for the selected shares
    :return: selected_shares: list of all the best shares to buy
    :return: total_cost: total cost of shares within the range of the budget
    :return: elapsed_time: time for the optimized.py to resolve the algorithm
    :return: efficiency: {float%} ((y2 - y1) / y1) * 100 gives the % of efficiency
    """
    start_time = time.time()
    data = pd.read_csv(file_path)

    # Filter out shares with a price of 0, negative profits, and within budget
    data = data[(data['price'] != 0) & (data['profit'] >= 0) & (data['price'] <= budget)]

    # Calculate actual profit for each share based on the percentage
    data['actual_profit'] = data['price'] * (data['profit'] / 100)

    # Calculate the ratio of profit to cost
    data['ratio'] = data['actual_profit'] / data['price']

    # Sort shares by ratio in descending order
    sorted_shares = data[data['actual_profit'] > 0].sort_values(by=['ratio', 'actual_profit', 'price'],
                                                                ascending=[False, False, True])

    selected_shares = []
    total_cost = 0
    total_profit = 0

    for _, share in sorted_shares.iterrows():
        if total_cost + share['price'] <= budget:
            selected_shares.append(share['name'])
            total_cost += share['price']
            total_profit += share['actual_profit']

    efficiency = ((total_cost + total_profit) - total_cost) / total_cost * 100
    end_time = time.time()
    elapsed_time = end_time - start_time

    return selected_shares, total_profit, total_cost, elapsed_time, efficiency


file_path1 = 'dataset1_Python+P7.csv'
file_path2 = 'dataset2_Python+P7.csv'
budget = 500

best_combination1, max_profit1, best_cost1, elapsed_time1, efficiency1 = best_share_combination(file_path1, budget)
best_combination2, max_profit2, best_cost2, elapsed_time2, efficiency2 = best_share_combination(file_path2, budget)

print("-"*23)
print("Results for dataset 1")
print("-"*23)
print(f"The best combination of shares to buy is: {best_combination1}")
print(f"Total of shares:", len(best_combination1))
print(f"Total profit: {max_profit1:.2f} euros")
print(f"Total cost: {best_cost1:.2f} euros")
print(f"Total efficiency: {efficiency1:.2f} %")
print(f"Time taken: {elapsed_time1:.4f} seconds\n")

print("-"*23)
print("Results for dataset 2")
print("-"*23)
print(f"The best combination of shares to buy is: {best_combination2}")
print(f"Total of shares:", len(best_combination2))
print(f"Total profit: {max_profit2:.2f} euros")
print(f"Total cost: {best_cost2:.2f} euros")
print(f"Total efficiency: {efficiency2:.2f} %")
print(f"Time taken: {elapsed_time2:.4f} seconds")
