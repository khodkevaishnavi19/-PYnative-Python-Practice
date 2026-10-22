# Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, and their sum
curr = 0
pre = 0
sum_nums = 0

for i in range(10):
    curr = i
    sum_nums = curr + pre

    print("Current number is:", curr,
          "Previous Number is:", pre,
          "Sum:", sum_nums)

    pre = curr
