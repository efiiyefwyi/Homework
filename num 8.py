first_max = int(input())
second_max = int(input())

if second_max > first_max:
    first_max, second_max = second_max, first_max

num = int(input())
while num != 0:
    if num > first_max:
        second_max = first_max
        first_max = num
    elif num > second_max and num != first_max:
        second_max = num
    num = int(input())

print(second_max)