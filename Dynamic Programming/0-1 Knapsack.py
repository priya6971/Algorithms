# Dynamic Programming approach - Bottom Up Approach
# Method definition of 0-1 Knapsack algorithm
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    x = [0 for i in range(n)]
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    res = K[n][w]
    print(res)
    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            break
        # either the result comes from the
        # top (K[i-1][w]) or from (val[i-1]
        # + K[i-1] [w-wt[i-1]]) as in Knapsack
        # table. If it comes from the latter
        # one/ it means the item is included.
        if res == K[i - 1][w]:
            continue
        else:
            # This item is included.
            x[i-1] = 1
            # Since this weight is included
            # its value is deducted
            res = res - val[i - 1]
            w = w - wt[i - 1]
    print("Items to be picked to maximize the profit")
    for i in range(n):
        print(x[i], end = " ")
# Driver program to test above function
val = [1, 2, 5, 6]
wt = [2, 3, 4, 5]
W = 8
n = len(val)
knapSack(W, wt, val, n)