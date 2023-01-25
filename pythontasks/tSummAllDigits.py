import random

num = random.randint(1000000000,9999999999)

sum = 0

print(num)

for i in str(num):
    sum += int(i)

print(sum)