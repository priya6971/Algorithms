# Sum of Subset Problem using memoization
# Time Complexity - O(total * n) - O(m * n)
def count_sets_dp(arr, total):
    memo = {}
    return memo_dp(arr, total, len(arr)-1, memo)

def memo_dp(arr, total, i, memo):
    key = str(total) + ':' + str(i) 
    if key in memo:
        return memo[key]

    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    elif total < arr[i]:
        to_return = memo_dp(arr, total, i-1, memo)
    else:
        to_return = memo_dp(arr, total - arr[i], i-1, memo) + memo_dp(arr, total, i-1, memo)
    memo[key] = to_return 
    return to_return 

arr = [2, 4, 6, 10]
total = 16
print("Number of possible sets:",count_sets_dp(arr, total))