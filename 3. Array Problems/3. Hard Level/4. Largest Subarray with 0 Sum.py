def maxLen(arr):
    n = len(arr)
    prefix_sum = {}  # Dictionary to store first occurrence of each prefix sum
    maxi = 0  # To keep track of maximum length found
    sum = 0  # To store the current prefix sum

    for i in range(n):
        sum += arr[i]  # Update prefix sum
        if sum == 0:
            maxi = i + 1  # If prefix sum is zero, update maxi
        else:
            if sum in prefix_sum:
                maxi = max(maxi, i - prefix_sum[sum])  # Update maxi if sum seen before
            else:
                prefix_sum[sum] = i  # Store first occurrence of this sum
                
    return maxi
arr = [1,-1,3,2,-2,-8,1,7,10,23]
print(maxLen(arr))