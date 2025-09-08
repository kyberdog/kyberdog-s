def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        nums = [0,1,1]
        for i in range(n-3):
            # -3 because we already have 3 fibonacci numbers in array
            nums.append(sum(nums))
        return nums[n-1]
    if n < 0:
        return "impossible"
