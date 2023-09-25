def maxProfit(prices):
    buy = 0
    sell = 0
    res = 0
    n = len(prices)
    for i in range(1, n):
        print(buy, sell)
        if prices[buy] => prices[i]:
            if prices[sell] - prices[buy] > 0:
                res += prices[sell] - prices[buy]
            buy = sell = i
        if prices[sell] < prices[i]:
            sell = i
        if (prices[buy] < prices[i] < prices[sell]):
            res += prices[sell] - prices[buy]
            buy = sell = i  
    if prices[sell] - prices[buy] > 0:
        res += prices[sell] - prices[buy]
    return res

print(maxProfit([1,2,4,2,5,7,2,4,9,0]))
