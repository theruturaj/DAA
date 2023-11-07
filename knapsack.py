def solve_knapsack():
    num_items = int(input("Enter the number of items: "))
    val = []
    wt = []

    for i in range(num_items):
        value = int(input(f"Enter the value of item {i + 1}: "))
        weight = int(input(f"Enter the weight of item {i + 1}: "))
        val.append(value)
        wt.append(weight)

    W = int(input("Enter the capacity of the knapsack: "))
    n = num_items - 1

    def knapsack(W, n):
        # base case
        if n < 0 or W <= 0:
            return 0

        # Higher weight than available
        if wt[n] > W:
            return knapsack(W, n - 1)

        else:
            return max(val[n] + knapsack(W - wt[n], n - 1), knapsack(W, n - 1))
            # max(including, not including)

    print(knapsack(W, n))

if __name__ == "__main__":
    solve_knapsack()