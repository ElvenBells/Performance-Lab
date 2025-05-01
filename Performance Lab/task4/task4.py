import sys

with open(sys.argv[1], 'r') as f:
    nums = list(map(int, f.read().split()))

sorted_nums = sorted(nums)
median = sorted_nums[len(nums) // 2]
moves = sum(abs(num - median) for num in nums)

print(moves)