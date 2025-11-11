# CMPS 2200 Assignment 3
## Answers

**Name:**Justin Green


Place all written answers from `assignment-03.md` here for easier grading.

1a) 
greedycoins(N):
    count = []
    while N > 0:
        coin = 1
        while coin * 2 <= N:
            coin *= 2
        count.append(coin)
        N -= coin
    return count

1b)
In order to use the most optimal number of coins to convert to dollars, we must always grab the biggest coin that we can afford (greedy structure). Once taking the largest coin, we now have a smaller version of the same problem, where we must keep selecting the largest possible coin until we've reduced down to 0 (optimal substructure). As we select a coin, I add one to the count of total coins that we have used to solve our problem. By selecting the largest possible coin each time, we spend the fewest coins possible.

1c)
The inner loop finds the largest power of 2 <= N. This runs in O(log N) time because it doubles each step. The outer loop runs once per coin used so at most log N + 1 times. Our work comes out to Work O(log N * log N) = O((log N)^2). The span is also O((log N)^2) because each iteration is sequential (depends on the previous subtraction).

2a)
If I want $8 in US currency and I had coin denominations of {1, 4, 6}, this would raise an incorrect solution from the greedy algorithm. The greedy algorithm would select a 6 coin, leaving 2 left over in which it would select a 1 coin then another 1 coin. This returns 3 coins used. The optimal solution would simply be two 4 coins.

2b)
Even if you are selecting the largest possible coin less than N, you still select a coin value, subtract it from N then repeat the process until you have nothing left over. During each step, we are still trying to make change with the smallest number of total coins feasible.

2c)
min_coins(D, N):
    dp = [float('inf')] * (N + 1)
    dp[0] = 0

    for n in range(1, N + 1):
        for d in D:
            if d <= n:
                dp[n] = min(dp[n], 1 + dp[n - d])

    return dp[N] if dp[N] != float('inf') else None

I used bottom-up to solve this.
Our work is O(Nk) since we compute dp[n] for each n from 1 to N, and for each n we check up to k denominations.
Our span is O(N) because dp[n] depends on all smaller dp[n - d]




