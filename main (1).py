count_even = 0
num = int(input())

while num != 0:
    if num % 2 == 0:
        count_even += 1
    num = int(input())

print(count_even)