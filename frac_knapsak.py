class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def fractionalKnapsack(W, arr):
    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True)

    finalvalue = 0.0

    for item in arr:
        if item.weight <= W:
            W -= item.weight
            finalvalue += item.profit
        else:
            finalvalue += item.profit * W / item.weight
            break
    return finalvalue

def input_items():
    arr = []
    num_items = int(input("Enter the number of items: "))
    for i in range(num_items):
        profit = int(input("Enter the profit of item: "))
        weight = int(input("Enter the weight of item: "))
        arr.append(Item(profit, weight))
    return arr

if __name__ == "__main__":
    W = int(input("Enter the knapsack capacity: "))
    arr = input_items()

    # Function call
    max_val = fractionalKnapsack(W, arr)
    print("The maximum value that can be obtained is:", max_val)

