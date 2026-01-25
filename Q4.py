# Q4.py
# Correctly removes even numbers from a list

def remove_even(nums):
    result = []
    for num in nums:
        if num % 2 != 0:
            result.append(num)
    return result


# 🔽 FUNCTION CALL (CHANGED INPUT)
nums = [12, 15, 18, 21, 24, 27, 30]
print(remove_even(nums))
