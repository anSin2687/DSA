prices = [7,1,5,3,6,4]

profit = 0
min = prices[0]
for i in range(len(prices)-1):
    if prices[i] < min:
        min = prices[i]
    elif profit < (prices[i] - min):
        print(prices[i] - min)
        profit = prices[i] - min